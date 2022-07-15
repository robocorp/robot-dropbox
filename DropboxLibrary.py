#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dropbox

def upload_to_dropbox(access_token, local_file, remote_file):
    dbx = dropbox.Dropbox(access_token)
    with open(local_file, 'rb') as f:
        dbx.files_upload(f.read(), remote_file)


def download_from_dropbox(access_token, remote_file, local_file):
    dbx = dropbox.Dropbox(access_token)
    with open(local_file, "wb") as f:
        _, res = dbx.files_download(remote_file)
        f.write(res.content)
