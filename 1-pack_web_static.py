#!/usr/bin/python3
<<<<<<< HEAD
""" module doc
"""
from fabric.api import task, local
from datetime import datetime


@task
def do_pack():
    """ method doc
        sudo fab -f 1-pack_web_static.py do_pack
    """
    formatted_dt = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(formatted_dt)
    print("Packing web_static to {}".format(path))
    if local("{} && tar -cvzf {} web_static".format(mkdir, path)).succeeded:
        return path
    return None
"""
    pack all content within web_static
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
        pack all content within web_static
        into a .tgz archive
        The archive will be put in versions/
    """
    if not os.path.exists("versions"):
        local("mkdir versions")
    now = datetime.now()
    name = "versions/web_static_{}.tgz".format(
        now.strftime("%Y%m%d%H%M%S")
    )
    cmd = "tar -cvzf {} {}".format(name, "web_static")
    result = local(cmd)
    if not result.failed:
        return name
