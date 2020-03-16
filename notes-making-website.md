---
pagetitle: Building this website
date: 26-July-2017
---


## Building this website 

I wrote this page to document the process of creating this website.
I mainly took the help of [pandoc](https://pandoc.org/) to simplify the entire process:
Pandoc is a very useful document converter and a handy tool for creating the 
html syntax of the website. 
After creating the necessary files (locally), I used 
[Github pages](https://pages.github.com/) for hosting the website.

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
overall code. Finally the [solarized-light](http://thomasf.github.io/solarized-css/)
css theme was created for styling the page content in conjuction with my custom
css file for more fine grained control (font-family, font-szie, image sizes etc).

To avoid writing the long pandoc command for each file, I wrote a simple bash 
script to run the command on all the markdown files which made
modifying the website content very convinient. You can check out the files at the
[github repository](https://github.com/ninception/ninception.github.io) for this website. 

~~~
pandoc \
	-H "$HEADER" \
	-B "$BEFORE" \
	-A "$AFTER" \
	-V author-meta="$AUTHOR" \
	-s --template "$TEMPL" \
	-f markdown -t html5 $mf -o $filename.html		
~~~


Pandoc can also be used to do many other things like creating neat looking pdf
documents (through a latex backend), docx files etc. It allows to control the
structure of the output document through templates. I use some slightly modified
templates (along with a custom pandoc css file for html output) which are 
available in my [dotfiles](https://github.com/kninad/dotfiles) repository.















