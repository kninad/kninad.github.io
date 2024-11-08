---
title: Building a website with pandoc
date: 2018-05-19
---

I wrote this page to document the process of creating this website.
I took the help of [pandoc](https://pandoc.org/) to simplify the entire process.
Pandoc is a very useful document converter and a handy tool for creating the 
html syntax of the website from a markdown file.
After creating the necessary files (locally), I used 
[Github pages](https://pages.github.com/) for hosting the website. 
Primary references for design: 
[this](http://bettermotherfuckingwebsite.com/), 
[this](https://bestmotherfucking.website/) and 
[this](https://thebestmotherfucking.website/) (although I take some
liberty to break some of the commandments described in them).

Each page of this website was written in [markdown](http://pandoc.org/MANUAL.html#pandocs-markdown)
and hence it was very easy to
write or modify the content and track the changes using git. 
The basic pandoc command for converting the markdown 
file to html will only output a plain html file. 
Although pandoc supports writing html syntax in the markdown file,
its usually not recommended as its better to keep the markdown file clean.

For further modifications, pandoc supports passing 
custom html files which can be added
to three positions (header, before-body and after-body) in the final html code 
for the page. Additionally, one can play around with the pandoc's default html 
template 
for gaining control over the placement of certain elements (like div) in the 
overall code. Finally a slightly modified version of 
[this css file](https://gist.github.com/killercup/5917178) 
was used for styling the website. It took care of making the 
website look a bit nice and tidy.

To avoid writing the long pandoc command for each file, I wrote a simple bash 
script to run the command on all the markdown files which made
modifying the website content very convinient.

```bash
#!/bin/bash

Rootdir="."
AUTHOR="Ninad"
CSS="${Rootdir}/css/pandoc.css"

for mf in $Rootdir/*.md
do
	filename="${mf%.*}"
	echo "Converting $mf to $filename.html" #Pandoc command for conversion to html:		
	pandoc \
        --css "$CSS"
		-V author-meta="$AUTHOR" \
		-f markdown -t html5 $mf -o $filename.html		
done	
```

## 2023 Update (Makefiles!)

The above process kind of works but it makes a strong assumption that all the
files are in a single directory without any nesting. However this is not an ideal
layout if we want to separate content like blog, projects etc. Additionally, it
re-generates *all* the files without a check whether something has changed or
not! To counter the above two points we can setup a simple `Makefile` based
approach to build the website.

This Makefile still only process documents in the current directory but if we
have such a makefile in every sub-directory taking care that each of the nested
makefiles have `all, clean` targets, then this kind of workflow will work.

- Collect current dir markdown files `SOURCES = $(wildcard *.md)`
- Create html targets using pattern substitution: `$(patsubst %.md,%.html,$(SOURCES))`
- Have a `all` target where we also go into the sub-dirs (here we only have `blog`)
  and run `make` on their respective `all` targets
- The actual `pandoc` command is quite straightforward:
  - I have a lua filter to convert all internal markdown links to html
  - Using a specific css file (note, path to it will change in the Makefile in sub-dirs)
  - Add a navbar and footer
- The `clean` target also has a `cd subdir && make $@` to automate the cleaning
  using the sub-dir's Makefile (remember we need to add `clean` in it as well).

Thus we need a single command to build out the entire website: `make all` and a
single command to clean all generated files: `make clean`
  

```makefile
STRING1 = "Last updated on "
STRING2 = "Created using [pandoc]\(http://pandoc.org/\)."

SOURCES = $(wildcard *.md)
HTMLs = $(patsubst %.md,%.html,$(SOURCES))
# See the A B website (youtube video) for sep shell scripts for blog portion
TEMPFILE = sdfgsdfs7fs8d7tfgsduifgsdi5234j

.PHONY : all
all: $(HTMLs)
	echo "Building the blog using its Makefile"
	@cd blog && make $@

%.html: %.md
	@cat $< > $(TEMPFILE)
	@echo "\n <hr / id="hr_footer">*<span class="footer">$(STRING1) `stat -c %Y Makefile | date +'%b %d, %Y'`. $(STRING2)*</span>" >> $(TEMPFILE)
	@pandoc --lua-filter=./static/links-to-html.lua -c ./static/css/pandoc.css -B navbar.html --mathjax -t html5 --standalone -i $(TEMPFILE) -o $@
	@rm -f $(TEMPFILE)

.PHONY : clean
clean:
	rm -f $(HTMLs)
	cd blog && make $@
```

