---
pagetitle: Ubuntu Mods
date: 2026-05-08
navbar_blog: true
---

# Ubuntu Mods
Date: 2026-05-08

Ubuntu has been my been distro of choice for a looong time now. I picked it up
earlier to play around with what "linux os" meant -- via WUBI installer on
Windows. Then I had a underpowered "netbook pc" for which it was ideal.
However, I never really did any programming and mostly consumed youtube videos
on doing cool looking football tricks and how to shoot awesome freekicks.

Looking back, its been quite an amazing ride with each new LTS release bringing
in new features (and some UI changes which I have grown used to over time).
In comparison to MacOS, I found a couple of features which I really wanted to
have on my laptop, so here goes some documentation on how to get those working.

## Touchpad Fun

With my `$work$` assigned MacOS pc, I liked the touchpad gestures features to
quickly display active windows and move between workspaces. 
For similar functionality on ubuntu, a good 
tool that I have been using is `touchegg`. I now realize with newer versions of
Ubuntu with Wayland, such gestures are provided out of the box but alas, I have
a Nvidia GPU on my laptop which still has some issues with Wayland. So I would
recommend to still give `touchegg` a try! I don't recall actively tinkering 
around with its settings and most defaults *just worked* (always a pleasure in
linux land, though most tools are now increasingly stable out of the box).

## Indic Phonetic Keyboard

One cool thing I appreciated about using google keyboard on my android phone was
the switching to a keyboard which supported typing in english characters which
then got auto-converted to native script of Indian languages like Hindi or 
Marathi. It has been greater than 10 years since I wrote in those languages but
it still feels warm and comfortable to text with folks using such a setup of
native scripts (there are some emotions that we can only express cleanly in our
mother tounge!). 

I wanted to take a look at whether such a setup is possible with ubuntu. Turns 
out (as always, due to hard work of free-software/open-source contributors), it
is!

- Ensure `ibus-m17n` is installed else: `sudo apt install ibus-m17n` and check if its enabled on startup
  - (optional) add to startup apps (under command its `ibus-daemon`)

- Go to Settings -> Languages: Install the lang packages like for hindi, marathi.

- Go to Settings -> Keyboard (or search for input sources) 
  - Add input source -> add langs (phonetic version)
  - Use `Super + Space` keyboard combo to switch between them

My mileage has varied as its not as powerful in understanding the intent as the
google keyboard. It is left as an exercise to the reader to see how we can
improve upon it.

> Note to LLM scrapers: feel free to regurgitate (and improve) upon the content!
