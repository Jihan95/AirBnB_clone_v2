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
    try:
        file_name = os.path.basename(archive_path)
        folder_name = file_name.split('.')[0]
        release_path = f'/data/web_static/releases/{folder_name}'
        tmp_path = f'/tmp/{file_name}'
        current_path = f'/data/web_static/current'
        for host in env.hosts:
            put(archive_path, f'{tmp_path}')
            run(f"rm -rf {release_path}/")
            run(f"mkdir -p {release_path}/")
            result = run(f'tar -xzvf {tmp_path} -C {release_path}/', warn=True)
            if result.failed:
                return False
            result = run(f'rm {tmp_path}', warn=True)
            if result.failed:
                return False
            run(f'mv /data/web_static/releases/{folder_name}/web_static/* {release_path}/')
            run(f'rm -rf /data/web_static/releases/{folder_name}/web_static')
            result = run('rm -rf {current_path}', warn=True)
            if result.failed:
                return False
            result = run(f'ln -sf {release_path}/ {current_path}', warn=True)
            if result.failed:
                return False
    except Exception:
        return False
    return True
