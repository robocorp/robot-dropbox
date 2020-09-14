*** Settings ***
Library         DropboxItems

*** Task ***
Store Image File to Work Item
    Save File To Work Item  source  image.png
    Save Work Item

*** Task ***
Store PDF File to Work Item
    Save File To Work Item  source  image.pdf
    Save Work Item
