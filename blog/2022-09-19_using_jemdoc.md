---
pagetitle: Jemdoc setup
date: 2022-09-19
navbar_blog: true
---

# Jemdoc Updates
Date: 2022-09-19

Recently, I tried to use jemdoc to create simple html pages. I was introduced to jemdoc long back but was using pandoc to generate html files for the website. The attractive property of jemdoc is that it only requires a working version of Python and no other dependencies. Jemdoc has some forks which have been updated recently and may be particularly useful:

- [Jemdoc and MathJax](https://github.com/wsshin/jemdoc_mathjax )
- [Jemdoc with Newdesign](https://github.com/szl2/jemdoc-new-design) (forked from above)

I usde the Newdesign repository since it includes a couple of quality of life improvements like responsiveness to screen size and menubar. The basic process about using the repository is well documented [here](https://szl2.github.io/jemdoc-new-design/www/index.html) and even the README is good to get started. It also includes the updated `jemdoc` Python 3+ script.

Jemdoc has a simple markdown-like syntax to write different elements of a webpage like headers, lists, links, code and images. Then the `jemdoc.py` python script is used to parse each `.jemdoc` file (where the content is) to convert the equivalent `.html`. There is a support to add a simple menu/sidebar for navigation using a `MENU` file. Using this we can have a simple working example.


## Tweaks to Note
Using modelines: At the top level of the jemdoc file, we can have special line starting with `# jemdoc:` denoting a modeline. A modeline includes meta info for a page like which menu file to use, the html name for the page, title etc. Interestingly, if you want to demarcate content into folders, just put the jemdoc files as is but modify the modeline as follows:

~~~
{}{}
# jemdoc: menu{MENU}{file.html}{../}, title{TITLE}, nodefaultcss, addcss{../css/main.css}
~~~

The `{..//}` indicates where the root directory for the html links in the provided `MENU` file. Hence whatever MENU file is in the project root, can simply be copied as is in the sub-dirs by adding the `{..//}` to each jemdoc file's modeline in the sub-dirs.

`title{TITLE}` gives a custom title to the webpage's generated html. `nodefaultcss` removes the css file provided by the `mysite.conf` configuration file. Then you can point to the actual path for the css file, and here since we are talking about files in a subdir, we go one level up as: `{../css/main.css}`.

Finally the /interior/, subdir files are translated to html using the code snippet below (notice the use of relative paths to jemdoc, and conf files). I plan to eventually transition to a `Makefile` based build process with some code to traverse through the entire src directory and generate html files. The current limitation is that I need to run the below command for /each/ subdir.

~~~
{}{}
python ../../jemdoc -c ../mysite.conf  *.jemdoc
~~~


## CSS Style file changes

- Moved the main content div to the left instead of `auto` margin
- Removed the bright yellow background for `blockcontent` and color for its title
- Increased the font sizes for better readability of text
- Changed the font family to be serif (personal preference)
- Subtle changes to background colors
