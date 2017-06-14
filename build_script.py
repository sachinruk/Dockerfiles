import os
import sys

dirs = os.listdir('.')
dirs = [name for name in dirs if (name!="Miniconda3" and name[0]!=".")]
dirs = ["Miniconda3"] + dirs # ensure that miniconda3 is first

DOCKER_REPO="sachinruk/"
TAG = str(sys.argv[1])

for image in dirs:
    DOCKER_IMAGE=DOCKER_REPO + image.lower() + ":" + TAG
    os.system("docker build -t " + DOCKER_IMAGE + "./" + image + "/")
    os.system("docker push " + DOCKER_IMAGE)
