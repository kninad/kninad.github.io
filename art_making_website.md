---
pagetitle: Building this website
---

### Building this website 

##### [Home](index.html) |  [Articles](articles.html) | [Projects](projects.html) | [Misc](misc.html) 

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

~~~
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
~~~


