#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir

env.hosts = ['34.139.124.220','34.74.25.112']
env.user = 'ubuntu'

def do_pack():
    """
    return the archive has been correctly generated
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_path = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except:
        return None
