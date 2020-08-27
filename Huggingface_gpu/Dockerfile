FROM nvidia/cuda:10.2-cudnn8-runtime-ubuntu16.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -qsSLkO \
    https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm Miniconda3-latest-Linux-x86_64.sh

ENV PATH=/root/miniconda3/bin:$PATH

RUN echo $(python --version)

RUN conda install -y \
    jupyter \
    numpy \
    h5py \
    pandas \
    matplotlib \
    seaborn \
    scikit-learn

RUN conda install pytorch torchvision cudatoolkit=10.2 -c pytorch

RUN pip install transformers

RUN conda clean --yes --tarballs --packages --source-cache

COPY jupyter_notebook_config.py /root/.jupyter/
COPY custom.js /root/.jupyter/

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

CMD jupyter lab --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=