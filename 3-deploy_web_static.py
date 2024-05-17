#!/usr/bin/python3
"""
a Python sctript to pack files in web stack folder
"""
import os
import fabric.api as fab
from datetime import datetime
from fabric.api import run, put, env,task, runs_once
env.hosts = ['52.3.243.155', '35.153.66.84']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'
env.use_ssh_config = True

@runs_once
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

@task
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

@task
def deploy():
    """
     a Fabric script (based on the file 2-do_deploy_web_static.py) that
     creates and distributes an archive to your web servers, using the function
     deploy
    """
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
