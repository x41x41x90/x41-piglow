x41-piglow
==========

Code for piglow, which will randomize each color, slowly go all the way bright, backdown, randomize, and go again.

Using the library from here: 

https://github.com/Boeeerb/PiGlow

web_dir:

These are tossed into /var/www with the proper php things

colors:

These are used for changing the color of the piglow. 
clear is for "resetting" the colors to nothing.
"kill" is for killing random colors


Root from web:
This wasn't written for security, but written as something neat. Assuming 
you're using this on your home network that isn't Internet accessable,
edit '/etc/sudoers' and add the following line to the end:

www-data ALL=(ALL) NOPASSWD: ALL

www-data needs access to the GPIO pins, which needs root to access.
