FROM sachinruk/miniconda3

RUN conda install -y \
    numpy \
    pandas

RUN pip install urllib3 elasticsearch
RUN conda clean --yes --tarballs --packages --source-cache

VOLUME /notebook
WORKDIR /notebook

RUN apt-get update && apt-get instal -y --no-install-recommends openssh-server
