#!/usr/bin/python3
"""
This is the 3-deploy_web_static.py module
"""


from fabric.api import *
from datetime import datetime
import os
env.hosts = ['52.91.182.154', '34.202.164.102']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/id_rsa"


def do_pack():
    """ Compressing the web_static files into .tgz """
    try:
        current_date = datetime.now()
        year = str(current_date.year)
        month = str(current_date.month)
        day = str(current_date.day)
        hour = str(current_date.hour)
        min = str(current_date.minute)
        sec = str(current_date.second)
        file_n = "web_static_" + year + month + day + hour + min + sec + ".tgz"
        local("mkdir -p versions")
        local("tar -cvzf versions/" + file_n + " web_static")
        path = "versions/" + file_n
        return path
    except Exception:
        return None


def do_deploy(archive_path):
    """ This is the function for deploying the content """
    if os.path.exists(archive_path) is False:
        return False
    try:
        p = "/data/web_static/releases/"
        file_name = archive_path.split('/')[1]
        no_ext = file_name.split('.')[0]
        sym_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/" + no_ext + "/")
        run("tar -xzf /tmp/" + file_name + " -C " + p + no_ext + "/")
        run("rm -rf /tmp/" + file_name)
        run("mv " + p + no_ext + "/web_static/* " + p + no_ext + "/")
        run("rm -rf /tmp/" + file_name)
        run("rm -rf /data/web_static/releases/" + no_ext + "/web_static")
        run("rm -rf " + sym_link)
        run("ln -s /data/web_static/releases/" + no_ext + "/ " + sym_link)
        return True
    except Exception:
        return False


def deploy():
    """ Full deployment """
    path = do_pack()
    if path is None:
        return False
    r_value = do_deploy(path)
    return r_value
