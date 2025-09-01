---
pagetitle: Linux Setup
date: 2015-05-05
navbar_blog: true
---


# Linux Setup

Date: 2015-05-05

## Back story
My first Linux based os was Ubuntu 10.04 lts which I installed on my home computer using wubi 
(it basically made ubuntu an 'installed program' on windows). 
But this was just an exploration phase after I had come to know about 
Linux and the GNU project. 
In first semester in undergrad at iitk I used the computer center 
labs (CentOS, gnome 2) and also we had to write C programming assignments
on those computers. 

## Motivation
In my second semester, I became more sucked into all the different DEs!
After that semester I became so comfortable and used to the way of things
in a linux os that I installed ubuntu on my personal laptop (dual boot) 
and as soon my Windows os crashed right before an end semester exam, 
I decided to use linux almost exclusively and henceforth only booted 
into windows for games (fifa/cs). 

I think once a person gets used to the environment a linux based os 
, it can be easily used for everyday computing tasks and I have even 
managed to convince my father to make the switch 
(ofcourse after he longer had use for ms-office)! 
This is especially in today's web centric world where we use our browser
 most of the time. 

Another motivation was the availability of programming tools which were
 present by default in any installation along with the shell. 
I still use the standard 'noob' distro i.e ubuntu (with Mate desktop environment) 
as it suits my needs perfectly! Some mental notes put down:

## Useful non-default programs

- LaTeX editor: Texmaker
- Calibre: ebook management
- Numix theme/icons for making desktop 'pretty'
- Tmux: terminal tabbing/windows
- Redshift: reduce blue intensity of screen light (during dark hours)

### Things to keep in mind

- Days of distro-hopping (same goes for DE) are over. Go with what works best and makes you productive. 
- Preferably download os .iso file over torrent and remember to check hashes. 
- Use the file backup utilities to prevent catastrophe!!! 
- Suspend issue: install nvidia driver with `acpi_sleep=nonvs` in grub + kernel update
- Screen tearing: again drive + compositor like compiz helps
- Battery Life: Install TLP / switch off nvidia gpu
- Debian not added as sudo: You have to login as root and add your user as sudo. `#adduser username sudo`
- Fonts: In Debian 8, fonts did not look 'pretty' by default. [Fonts wiki](https://wiki.debian.org/Fonts) will help. Also check anti-aliasing settings, font rendering.

