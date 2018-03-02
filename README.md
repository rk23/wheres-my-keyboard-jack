# OLKB Keyboards Order Checker aka Where's my keyboard, Jack?

In lieu of either searching for my order number and caluclating the remaining orders from my own, or asking the one and only Jack Humbert my order's position in line, I wrote a script to do it for me. 

`python wheres_my_keyboard.py`

This will call reddit's API to find the appropriate post, scan and parse out all order numbers with respective replies, then sort and take the last posted order number as the latest. I then subtract that from my order number to get my spot. Crude, and the dude himself said some orders get paired together / cancelled so it's likely a closer than presented but hey, close enough.

You just have to fill in your reddit api credentials in the praw.ini file, and your order number in the wheres_my_keyboard.py file.
