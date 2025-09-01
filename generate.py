import os, shutil, re, markdown, yaml
from jinja2 import Environment, FileSystemLoader

# ---------------- Config ----------------

with open("config.yaml", "r", encoding="utf-8") as f:
    CONFIG = yaml.safe_load(f)

CONTENT_DIR = CONFIG.get("CONTENT_DIR", "content")
OUTPUT_DIR = CONFIG.get("OUTPUT_DIR", "output")
THEME_DIR = CONFIG.get("THEME_DIR", "themes/simple")
STATIC_DIR = CONFIG.get("STATIC_DIR", "static")
SITE_TITLE = CONFIG.get("SITE_TITLE", "My Site")

env = Environment(loader=FileSystemLoader(THEME_DIR))

# ---------------- Utility Functions ----------------

def extract_first_h1(md_text):
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return None

def make_relative_link(target, current_dir):
    """Compute relative path from current_dir to target file."""
    rel = os.path.relpath(target, start=current_dir)
    return rel.replace("\\", "/")

def parse_front_matter(md_text):
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            fm_yaml = parts[1]
            content = parts[2].lstrip("\n")
            fm = yaml.safe_load(fm_yaml)
            return fm or {}, content
    return {}, md_text


def preprocess_images(md_text):
    """
    Process Markdown images to add optional width/height.
    Ignores titles entirely.
    Syntax: ![Alt Text](path | WxH)
    """
    def repl(match):
        alt = match.group(1)
        path_info = match.group(2).strip()

        img_path = path_info
        width_attr = ""
        height_attr = ""

        if "|" in path_info:
            img_path, size_info = path_info.split("|", 1)
            img_path = img_path.strip()
            size_info = size_info.strip()
            if "x" in size_info:
                w, h = size_info.split("x")
                width_attr = f' width="{w.strip()}"'
                height_attr = f' height="{h.strip()}"'

        # Return Markdown image with width/height stored as HTML attributes
        # We’ll convert Markdown → HTML normally; width/height will be applied in post-processing
        return f'![{alt}]({img_path}){{width="{width_attr.strip()}" height="{height_attr.strip()}"}}'

    return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', repl, md_text)





def markdown_to_html(md_text, current_dir):
    # Preprocess images for sizes
    # md_text = preprocess_images(md_text)

    # html_content = markdown.markdown(md_text, extensions=["fenced_code", "tables", "attr_list"])
    # # Fix internal .md links
    # html_content = html_content.replace(".md\"", ".html\"")
    # return html_content

    def fix_md_links(html_content, current_dir):
        """
        Replace Markdown links ending in .md with .html and adjust relative paths.
        current_dir: the folder of the current HTML file, relative to OUTPUT_DIR
        """
        def repl(match):
            href = match.group(1)
            if href.endswith(".md"):
                href_html = href.replace(".md", ".html")
                return f'href="{href_html}"'
            return match.group(0)

        return re.sub(r'href="([^"]+)"', repl, html_content)

    # Convert Markdown → HTML
    html_content = markdown.markdown(md_text, extensions=["fenced_code", "tables", "attr_list"])
    html_content = fix_md_links(html_content, current_dir)
    # Convert internal .md links → .html
    def replace_md_link(match):
        md_path = match.group(1)
        html_path = md_path.replace(".md", ".html")
        return f'href="{html_path}"'

    html_content = re.sub(r'href="([^"]+)\.md"', replace_md_link, html_content)

    return html_content



def load_menu():
    """Load menu from menu.yaml or auto-generate top-level content/folder links."""
    if os.path.exists("menu.yaml"):
        with open("menu.yaml", "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    menu = []
    for entry in sorted(os.listdir(CONTENT_DIR)):
        path = os.path.join(CONTENT_DIR, entry)
        if os.path.isfile(path) and entry.endswith(".md"):
            menu.append({
                "name": os.path.splitext(entry)[0].title(),
                "link": entry.replace(".md", ".html")
            })
        elif os.path.isdir(path):
            index_md = os.path.join(path, "index.md")
            if os.path.exists(index_md):
                menu.append({
                    "name": entry.title(),
                    "link": os.path.join(entry, "index.html").replace("\\","/")
                })
    return menu

def render(content_html, title, menu, current_dir, fm=None, current_page_path=None):
    template = env.get_template("base.html")

    rel_static = make_relative_link(
        os.path.join(OUTPUT_DIR, os.path.basename(STATIC_DIR)),
        current_dir
    )

    rel_menu = []
    for item in menu:
        link_path = os.path.join(OUTPUT_DIR, item["link"])
        rel_link = make_relative_link(link_path, current_dir)
        rel_menu.append({
            "name": item["name"],
            "link": rel_link,
            "active": current_page_path == item["link"] or current_page_path == rel_link
        })

    return template.render(
        site_title=SITE_TITLE,
        title=title,
        content=content_html,
        menu=rel_menu,
        meta=fm or {},
        static_path=rel_static
    )


def process_file(src, dst, menu):
    """Convert a Markdown file to HTML and write output."""
    rel_dst_dir = os.path.dirname(dst)
    rel_dst_path = os.path.relpath(dst, OUTPUT_DIR).replace("\\","/")
    with open(src, "r", encoding="utf-8") as f:
        md_text = f.read()
    fm, content_md = parse_front_matter(md_text)

    title = fm.get("title") or extract_first_h1(content_md) or os.path.splitext(os.path.basename(src))[0].title()
    html_content = markdown_to_html(content_md, rel_dst_dir)
    page_html = render(html_content, title, menu, rel_dst_dir, fm, current_page_path=rel_dst_path)
    os.makedirs(rel_dst_dir, exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(page_html)

def copy_static():
    """Copy static assets (CSS, JS, images, etc.) to output folder."""
    if os.path.exists(STATIC_DIR):
        dest = os.path.join(OUTPUT_DIR, os.path.basename(STATIC_DIR))
        shutil.copytree(STATIC_DIR, dest, dirs_exist_ok=True)
        print(f"✅ Copied static folder to {dest}")



# ---------------- Build ----------------

def build():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)

    menu = load_menu()

    for root, _, files in os.walk(CONTENT_DIR):
        rel_path = os.path.relpath(root, CONTENT_DIR)
        for file in files:
            if file.endswith(".md"):
                src = os.path.join(root, file)
                dst = os.path.join(OUTPUT_DIR, rel_path, file).replace(".md", ".html")
                process_file(src, dst, menu)

    # copy_content_assets()
    copy_static()
    print(f"✅ Site built into {OUTPUT_DIR}")

if __name__ == "__main__":
    build()
