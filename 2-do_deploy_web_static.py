#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""
import os
from fabric.api import run, put, env
env.hosts = ['52.3.243.155', '35.153.66.84']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'


def do_deploy(archive_path):
    """
    distributes an archive to my web servers
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.split('.')[0]
    release_path = f'/data/web_static/releases/{folder_name}'
    tmp_path = f'/tmp/{file_name}'
    current_path = f'/data/web_static/current'
    for host in env.hosts:
        put(archive_path, '/tmp/')
        result = c.run(f'tar -xzvf {tmp_path} -C {release_path}', warn=True)
        if result.failed:
            return False
        result = run(f'rm /tmp/{file_name}', warn=True)
        if result.failed:
            return False
        result = run('rm -f {current_path}', warn=True)
        if result.failed:
            return False
        result = run(f'ln -sf {release_path} {current_path}', warn=True)
        if result.failed:
            return False
    return True
