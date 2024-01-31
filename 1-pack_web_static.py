#!/usr/bin/python3
"""Fabfile to generate a .tgz archive from the contents of web_static"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
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
