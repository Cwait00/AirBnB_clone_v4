#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"

def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """

    number = 1 if int(number) == 0 else int(number)

    # Local clean-up
    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs -I {{}} rm -- {{}}".format(number + 1))

    # Remote clean-up
    with cd("/data/web_static/releases"):
        run("ls -tr | tail -n +{} | xargs -I {{}} rm -rf -- {{}}".format(number + 1))

if __name__ == "__main__":
    do_clean()
