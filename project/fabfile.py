from __future__ import with_statement
from fabric.api import settings, run, cd

def deploy(mode="production"):
    code_dir = '/srv/vhosts/blogs/'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone git@github.com:azpm/azpm-www-blogs.git %s" % code_dir)
            run("setfacl -m d:g:http_srv:rwx %slogs")

    with cd(code_dir):
        run("git pull")

    load_config(mode)
    restart_site()

def restart_site():
    working_dir = '/srv/vhosts/blogs/public'
    with cd(working_dir):
        run("touch run.wsgi")

def load_config(mode="production"):
    working_dir = '/srv/vhosts/'
    with cd(working_dir):
        run("cp deployment/{0:>s}/blogs/local_settings.py blogs/project/".format(mode))