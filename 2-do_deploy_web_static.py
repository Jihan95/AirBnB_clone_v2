#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""
import os
from fabric.api import run, put, env
env.hosts = ['52.3.243.155', '35.153.66.84']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'
env.use_ssh_config = True


def do_deploy(archive_path):
    """
    distributes an archive to my web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = os.path.basename(archive_path)
        folder_name = file_name.split('.')[0]
        release_path = f'/data/web_static/releases/{folder_name}/'
        tmp_path = f'/tmp/{file_name}'
        current_path = '/data/web_static/current'

        put(archive_path, tmp_path, use_sudo=True)

        run(f"rm -rf {release_path}", warn_only=True)
        run(f"mkdir -p {release_path}", warn_only=True)

        result = run(f'tar -xzvf {tmp_path} -C {release_path}', warn_only=True)
        if result.failed:
            return False

        result = run(f'rm {tmp_path}', warn_only=True)
        if result.failed:
            return False

        run(f'mv {release_path}/web_static/* {release_path}', warn_only=True)
        run(f'rm -rf {release_path}/web_static', warn_only=True)

        result = run(f'rm -rf {current_path}', warn_only=True)
        if result.failed:
            return False

        result = run(f'ln -sf {release_path} {current_path}', warn_only=True)
        if result.failed:
            return False
        print("New version deployed!")
        return True

    except Exception:
        return False
