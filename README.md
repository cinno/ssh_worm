ssh_worm
========

An ssh worm written in Python

## The essentials

There is a .list file provided which is a list of passwords that the worm will
use to bruteforce the SSH login. You can use your own if you don't like the 
one I have provided.

The worm just tries to bruteforce the login for root on any machine in its 
private network that has SSH running.

## Compile to executable

You should use Pyinstaller to make this into a stand alone executable so you 
don't have to worry about portability to another machine (does it have the 
necessary libraries, etc.). The command to use wthin the Pyinstaller dir is:
./pyinstaller.py --onefile ../ssh_worm/worm.py This will create a worm dir
and the executable is within the dist directory.
