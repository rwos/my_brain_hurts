my_brain_hurts
==============

What?
-----

A small brainfuck interpreter written in python.

How?
----

It reads the source from standard input. Use it like so:

    cat SOURCE_FILE | python my_brain_hurts.py

or like so, for interactive programs (this might only work in bash):

    (cat SOURCE_FILE && cat) | python my_brain_hurts.py

Limits?
-------

It only reads the first 369.47 MB of the source. But if you ever
reach this limit with brainfuck code, you have much bigger problems
than that. Consult a brain surgeon.

Brainfuck interpreters historically have a 30,000 cells memory. I am very
happy to announce that this one - despite its small size - breaks
this limit and gives you a whooping 32,768 cells. Now, how is that?

Why?
----

I wrote it to teach myself Python, to see whether unreadable python code
is possible (spoiler-alert: yes), and for fun.

Who?
----

Richard Wossal <richard@r-wos.org> - 26th Sep. 2011
and some [reddit users](http://redd.it/ksawz)

Free Software?
--------------

Do with it whatever you want - but don't blame me if your house
explodes, your hard-drive melts or your brain hurts.

