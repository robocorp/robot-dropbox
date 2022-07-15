*** Settings ***
Library  RPA.Robocorp.Vault
Library  DropboxLibrary.py

*** Task ***
Upload File To Dropbox
  ${dropbox_secret}=  Get Secret  Dropbox
  Upload to Dropbox  ${dropbox_secret}[Access token]  DropboxLibrary.py  /UL1.py

*** Task ***
Download File From Dropbox
  ${dropbox_secret}=  Get Secret  Dropbox
  Download from Dropbox  ${dropbox_secret}[Access token]  /UL1.py  DropboxLibrary2.py


