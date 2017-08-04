---
pagetitle: Building this website
date: 26-July-2017
---


### Building this website
###### 26-July-2017

I wrote this page to document the process of creating this website.
I took the help of two main tools to simplify the entire process:
[pandoc](https://pandoc.org/) and [bootstrap](http://getbootstrap.com/). 
Pandoc is a very useful document converter and a handy tool for creating the 
html code of the website and bootstrap is used for styling the website, especially
the side navigation bar. 
After creating the necessary files (locally), I used 
[Github pages](https://pages.github.com/) for hosting the website.

Each page of this website was written in pandoc's [markdown](http://pandoc.org/MANUAL.html#pandocs-markdown)
and hence it was very easy to
write or modify the content and track the changes using git. 
The basic pandoc command for converting the markdown 
file to html will only output a plain html file. 
Although pandoc supports writing raw html code in the markdown file, but 
its not recommended as its better to keep the markdown file clean.

For further modifications, pandoc supports passing html files which can be added
to three positions (header, before-body and after-body) in the final html code 
for the page. Additionally, one even play around with the default html template 
for gaining control over the placement of certain elements in the html code.
I added the simple navigation sidebar at the top using bootstrap and made some 
modifications to it using a custom css file. Finally I wrote a bash script to run 
the pandoc command on all the markdown files which made re-publishing / 
modifying the website very convinient. You can check out the files at my github
[repo](https://github.com/ninception/ninception.github.io) for this website. 

~~~
#!/bin/bash

AUTHOR="Ninad"
HEADER="./_includes/head.html"
BEFORE="./_includes/before-body.html"
AFTER="./_includes/after-body.html"
TEMPL="./_includes/my_template.html"

for mf in ./*.md
do
	filename="${mf%.*}"
	echo "Converting $mf to $filename.html" #Pandoc command for conversion to html:		
	pandoc \
		-H "$HEADER" \
		-B "$BEFORE" \
		-A "$AFTER" \
		-V author-meta="$AUTHOR" \
		-s --template "$TEMPL" \
		-f markdown -t html5 $mf -o $filename.html		
done

# Can even use a custom template with:
# --template default_mod.html 
# -s stands for standalone
# --css mycssfile.css (css linking already done in HEADER 
~~~

---
