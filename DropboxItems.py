#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import random
import dropbox
from RPA.Robocloud.Items import Items
from RPA.Robocloud.Secrets import Secrets


class DropboxItems(Items):
    def __init__(self):
        super().__init__()
        self.dbx = dropbox.Dropbox(
            Secrets().get_secret("Dropbox")["ACCESS_TOKEN"])

    def set_work_item_file(self, name, filename):
        dbxid = self._upload_to_dropbox(filename)
        self.set_work_item_variable(name, [filename, dbxid])

    def get_work_item_file(self, name):
        filename, dbxid = self.get_work_item_variable(name)
        self._download_from_dropbox(dbxid, filename)

    def _upload_to_dropbox(self, filename):
        dbxid = "/%s_%s" % (
            self.current.item_id, 
            ''.join([random.choice(string.ascii_lowercase) for i in range(32)]))

        with open(filename, 'rb') as f:
            dbx.files_upload(f.read(), dbxid)

        return dbxid

    def _download_from_dropbox(self dbxid, filename):
        with open(filename, "wb") as f:
            metadata, res = dbx.files_download(dbxid)
            f.write(res.content)
