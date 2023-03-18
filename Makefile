STRING1 = "Last updated on "
STRING2 = "Created using [pandoc]\(http://pandoc.org/\)."


RESOURCEDIR = "css"
PAPERSDIR = "Papers"
VARIOUSDIR = "Various"
PICSDIR = "Pics"
TARGETDIR = "public"


SOURCES = $(wildcard *.md)
HTMLs = $(patsubst %.md,%.html,$(SOURCES))
BLOG_SOURCES = $(wildcard blog/*.md)
BLOG_HTMLs = $(patsubst %.md,%.html,$(BLOG_SOURCES))
# See the A B website (youtube video) for sep shell scripts for blog portion
TEMPFILE = sdfgsdfs7fs8d7tfgsduifgsdi5234j

all: $(HTMLs)

%.html: %.md
	cat $< > $(TEMPFILE)
	echo "\n <hr / id="hr_footer">*<span class="footer">$(STRING1) `stat -c %Y Makefile | date +'%b %d, %Y'`. $(STRING2)*</span>" >> $(TEMPFILE)
	pandoc --lua-filter=./static/links-to-html.lua -c ./static/css/pandoc.css -B navbar.html --mathjax -t html5 --standalone -i $(TEMPFILE) -o $@
	rm -f $(TEMPFILE)

clean:
	rm -f $(HTMLs)
	rm -f $(BLOG_HTMLs)