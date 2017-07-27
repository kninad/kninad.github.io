---
pagetitle: vim & tmux
date: 15-July-2017
---

### Vim and tmux
###### 15-July-2017

A very good resource for taking up vim is vimtutor which can accessed in a
terminal and comes with vim.
For customizing vim, edit the .vimrc file in the home directory. Some useful
links for vim:

- [vim cheatsheet](http://www.viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html)

- [vimrc guide](https://dougblack.io/words/a-good-vimrc.html)

Since vim is terminal based, a terminal multiplexer like 
[tmux](https://github.com/tmux/tmux/wiki)
helps a lot while programming with vim since multiple terminal tabs can be problematic. 
I found this
[guide](http://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/) 
to tmux 
quite good. There is also a [book](https://leanpub.com/the-tao-of-tmux/read) for
 tmux!


Noting down some useful vim keystrokes:

---

#### Navigation

h -- go left

j -- go down

k -- go up

l -- go right

---

#### Saving files

:w -- write (save) the file

:wq -- write and quit

:q! -- force quit

i -- Will enable the insert mode for editing files

ESC -- Will exit inset mode (and go back to normal mode)

---

#### Operators

Operators can be combined with the motion keys to produce different kinds of 
commands. You can guess what the motion keys are from the commands below.
Add a number in between to repeat the command.

de -- delete upto end of word (d stands for delete)

dd -- delete the whole line (kind of like CUT)

d0 -- delete upto start of line

d$ -- delete upto end of line

A -- append at the end of sentence

ce -- change until end of word

x -- acts as a delete key in insert mode

r -- replace key

p -- put prev deleted text after cursor

---

#### Undo

u -- undo the previous command

U -- fix the whole line as it was

<Ctrl-R\> -- undo the undos

---
