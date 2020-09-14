#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
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

    def save_file_to_work_item(self, name, filename):
        if filename.endswith(".txt") and os.path.getsize(filename) < 10000:
            with open(filename, "rb") as f:
                self.set_work_item_variable(name, ["EMBED", filename, f.read()])
        else:
            dbxid = self._upload_to_dropbox(filename)
            self.set_work_item_variable(name, ["DROPBOX", filename, dbxid])

    def load_file_from_work_item(self, name):
        backend, filename, data = self.get_work_item_variable(name)
        if backend == "EMBED":
            with open(filename, "wb") as f:
                f.write(data)
        else:
            self._download_from_dropbox(data, filename)

        return filename

    def _upload_to_dropbox(self, filename):
        dbxid = "/%s_%s" % (
            self.current.item_id, 
            ''.join([random.choice(string.ascii_lowercase) for i in range(32)]))

        with open(filename, 'rb') as f:
            self.dbx.files_upload(f.read(), dbxid)

        return dbxid

    def _download_from_dropbox(self, dbxid, filename):
        with open(filename, "wb") as f:
            _, res = self.dbx.files_download(dbxid)
            f.write(res.content)
