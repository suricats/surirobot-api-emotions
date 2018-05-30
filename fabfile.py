import time
import os

from fabric.api import env, local, require, run, prompt, cd
from fabric.colors import green

# globals
env.prj_name = 'mrsatan'  # no spaces!
env.use_ssh_config = True
env.forward_agent = True
env.timeout = 30

try:
    SSH_USER = os.environ["FABRIC_SSH_USER"]
except KeyError:
    raise ValueError("FABRIC_SSH_USER not found in environment.")


def production():
    """ sets env for production. """
    env.hosts = ['cerdan']
    env.user = SSH_USER
    env.homepath = '/home/%(user)s' % env
    env.prj_path = '/var/projects/%(prj_name)s' % env
    env.base_url = 'mrsatan.seelk.io'
    env.env = "prod"

    env.refspec = 'master'
    env.project_name = 'mrsatan'
    env.docker_compose_file = 'docker-compose.yml'


def deploy(refspec='', project_name='', docker_user='', docker_passwd=''):
    """
    Pull the environment refspec (or other if specified), build the docker-compose
    image, stop the previously running and up it.
    """
    start_time = time.time()
    require('hosts', provided_by=[staging, production])
    require('prj_path')
    require('refspec')
    require('project_name')
    require('docker_compose_file')
    refspec = refspec or env.refspec
    project_name = project_name or env.project_name
    docker_compose = 'docker-compose -p {} -f {} '.format(project_name, env.docker_compose_file)
    with cd('%(prj_path)s' % env):
        run('git fetch origin %s -v' % refspec)
        run('git reset --hard origin/%s' % refspec)
        run("docker login registry.seelk.io -u {} -p {}".format(docker_user, docker_passwd))
        run(docker_compose + 'pull')
        run(docker_compose + 'stop')
        run(docker_compose + 'up -d')
        print("Deployment time: %s seconds" % (time.time() - start_time))