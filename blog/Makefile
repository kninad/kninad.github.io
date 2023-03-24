STRING1 = "Last updated on "
STRING2 = "Created using [pandoc]\(http://pandoc.org/\)."

SOURCES = $(wildcard *.md)
HTMLs = $(patsubst %.md,%.html,$(SOURCES))
# See the A B website (youtube video) for sep shell scripts for blog portion
TEMPFILE = sdfgsdfs7fs8d7tfgsduifgsdi5234j

.PHONY : all
all: $(HTMLs)

%.html: %.md
	@cat $< > $(TEMPFILE)
	@echo "\n***\n\n<span class="footer">*$(STRING1) `stat -c %Y Makefile  | date +'%b %d, %Y'`. $(STRING2)*</span>" >> $(TEMPFILE)
	@pandoc --toc --toc-depth 2 --lua-filter=../static/links-to-html.lua -c ../static/css/pandoc.css -B ../static/navbar_L2.html --mathjax -t html5 --standalone -i $(TEMPFILE) -o $@
	@rm -f $(TEMPFILE)

.PHONY : clean
clean:
	rm -f $(HTMLs)