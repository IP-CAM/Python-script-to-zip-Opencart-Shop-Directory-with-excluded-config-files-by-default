# Python script to zip OpenCart shop directory with excluded config files by default

This script add OpenCart shop directory to zip archive with default excluded config files. Tested only in
Python 3.9, OS Windows 10. Use it for you own risk.

## How to use

First, download and install [Python](https://www.python.org/downloads/) to you OS, then copy _
zip_shop.py_ to you OpenCart directory, and open that directory in terminal.

Input in terminal:

`python zip_shop.py`

and wait until python compress you folder to zip file.

## Use with gui

With GUI( Graphic User Interface ) you may choose the folder contains OpenCart shop and check exclude
config files or not.

First, open repository folder in you terminal and install dependencies from requirements.txt file:

`pip install -r requirements.txt`

and then run zip_shop_with_gui.py

`python zip_shop_with_gui.py`
