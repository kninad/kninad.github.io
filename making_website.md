---
pagetitle: Building this website
---

### Building this website

I wrote this page to document the process of creating this website.
I took the help of two main tools to simplify the entire process:
[pandoc](https://pandoc.org/)and [bootstrap](http://getbootstrap.com/). 
Pandoc is a very useful document
converter which is handy tool for creating the html code for the website and Bootstrap 
is useful for styling the website. After locally creating the necessary files,
I used [Github pages](https://pages.github.com/)
for hosting the website.

Each page of this website was written in [markdown](http://pandoc.org/MANUAL.html#pandocs-markdown)
and hence it was very easy to
write or modify the content and also to track the changes using git. 
The basic pandoc command for converting the markdown 
file to html will only output a plain html file. 
Although pandoc supports writing raw html code in the markdown file itself, but 
its not highly recommended as its better to keep the markdown file clean.

For further modifications, pandoc supports passing html files which can be added
to three positions (header, before-body and after-body) in the final html code 
for the page and one even play around with the default html template.
I added the simple navigation bar(navbar) at the top using bootstrap and made some 
modifications to it using a custom css file. Finally I wrote a bash script to run 
the pandoc command on all the markdown files in a loop which made re-publishing 
the website very convinient.

~~~
#!/bin/bash

AUTHOR="Ninad"
HEADER="./helpers/header.html"
BEFORE="./helpers/before-body.html"
AFTER="./helpers/after-body.html"

for mf in ./*.md
do
	filename="${mf%.*}"
	echo "Converting $mf to $filename.html" #Pandoc command for conversion to html:	
	pandoc	
	-H "$HEADER"  -B "$BEFORE" -A "$AFTER" \
	-V author-meta="$AUTHOR" \
	-f markdown -t html5 -o $filename.html  $mf	
done
~~~


You can check out my files at the [github repo](https://github.com/ninception/ninception.github.io) 
for this website. 


---
