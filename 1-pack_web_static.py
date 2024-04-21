#!/usr/bin/python3
"""
This is the 1-pack_web_static module
"""


from fabric.api import local
from datetime import datetime


def do_pack():
    """ Compressing the web_static files into .tgz """
    current_date = datetime.now()
    year = str(current_date.year)
    month = str(current_date.month)
    day = str(current_date.day)
    hour = str(current_date.hour)
    min = str(current_date.minute)
    sec = str(current_date.second)
    file_name = "web_static_" + year + month + day + hour + min + sec + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf versions/" + file_name + " web_static")
