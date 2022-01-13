#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local
from fabric import *


def do_pack():
    """
    return the archive has been correctly generated
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir versions")
    file_path = "versions/web_static_{}.tgz".format(date)
    exec_ = local("sudo tar -cvzf {} web_static".format(file_path))
    if exec_.succeeded:
        return file_path
    else:
        return None
