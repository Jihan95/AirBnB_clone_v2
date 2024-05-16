#!/usr/bin/python3
"""
a Python sctript to pack files in web stack folder
"""
import os
import fabric.api as fab
from datetime import datetime


def do_pack():
    """
    a Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo,
    """
    files_path = os.getcwd()
    path = os.path.join(os.getcwd(), "versions")
    if not os.path.exists(path):
        os.makedirs(path)
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    filename = f'web_static_{timestamp}.tgz'
    res = fab.local(f'tar -cvzf {path}/{filename} web_static', capture=False)
    if res.succeeded:
        if os.path.exists(f'{path}/{filename}'):
            return f'{path}/{filename}'
    return None
