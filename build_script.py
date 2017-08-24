import os
import sys
import subprocess
from subprocess import call

out = subprocess.check_output("git diff --name-only HEAD~1 HEAD".split())
out = out.decode('ascii').split('\n')[:-1]
dockerfiles = [files for files in out if "Dockerfile" in files]

base_dirs = ["Miniconda3/Dockerfile", "DS_base/Dockerfile"]
base_dirs_in_dockerfiles = [val for val in base_dirs if val in dockerfiles]
dockerfiles = [val for val in dockerfiles if val not in base_dirs_in_dockerfiles]


dirs = base_dirs_in_dockerfiles + dockerfiles
dirs = [d.replace('/Dockerfile','') for d in dirs]
#
DOCKER_REPO="sachinruk/"
TAG = str(sys.argv[1])

def call_cmd(cmd):
    ret_code = call(cmd.split())
    if ret_code != 0:
        print("The following command failed: " + cmd)
        sys.exit(ret_code)

for image in dirs:
    DOCKER_IMAGE=DOCKER_REPO + image.lower().replace('/dockerfile','')
    tagged_version = DOCKER_IMAGE + ":" + TAG
    call_cmd("docker build -t " + DOCKER_IMAGE + " ./" + image + "/")
    call_cmd("docker tag " + DOCKER_IMAGE + " " + tagged_version)
    call_cmd("docker push " + DOCKER_IMAGE)
    print("="*50)
    print(image+ " built!")
    print("="*50)
