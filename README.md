# README

Github repository for my personal webpage: https://kninad.github.io/

Made using Hugo and Kayal theme.


# Usage and Publishing

> Last checked compatability with Hugo Version: `0.139.4`. 
Newer versions `0.14xx` did not work well as hugo showed a warning for kayal theme not being compatible.

I have the hugo binary under `~/Applications/bin/` folder where I keep other third party binaries. Also
have a backup with me for the binary.

## Hugo Config
- Under `config/_default.hugo.toml`
- Keep the `publishDir = "docs"` and github settings to pick up the content from here.


## Workflow

- Edit the markdown files in `content`
- Preview the website using `hugo server` -- will open a local websit
  - default on `localhost:1313`
- To finally push changes to web host, run `hugo`. IMP to run this before pushing!
  - It will publish the website in teh `docs` folder
  - NOTE: This is not the defauly folder it usually publishes in
    - Default is `public` folder), but I changed the `publishDir = "docs"` in `hugo.toml` config.
- I have enabled github to load the website from the `docs` folder of the repo.
- Push the changes to github

Notes:

1. For html CV, I just edit the `content/cv/_index.md` manually as the other resume changes


# Content Notes

## Home
- Research interests: Short summary and advisor info.
- Teaching (TAed courses + mentees)
- Reviewing
- Talks
- Publications and Preprints (Can later move this to a separate page + add link to google
  scholar or related websites)
- Software: link to github repos of important codes? + short description (can be in misc too)


## Research

An entire page dedicated to short summaries of papers and high-level ideas about your researach.
Also acts as a way to organize your papers! Need not include all your pubs. Add relevant images and pdf links to papers. Also can add a wordcloud image at the beginning or end. 


## Misc

- Add stuff about hobbies: music, sketching, football (notes for them) + other thoughts under
  an appropriate section header
  
- Add technical notes under a different subsection. Make sure to add dates to all notes. Can be 
  about some good concepts / demos (encountered while surfing, homeworks etc)

- Can use the MENU file to link notes directly! (see jemdoc homepage)

- Finally, there will be a Useful Links + Footy pic section in Misc

- Can add undergrad and other side projects too!

- Can add some research projects too (CV / NLP / DL stuff under projects done)

- Add in Misc: Prime numbers, mathy stuff, linux/foss ubuntu mate stuff

- Add redshift link to Useful Links under Notes

