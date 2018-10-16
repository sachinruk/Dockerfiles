FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04
ARG PYTHON_VERSION=3.6
RUN apt-get update && apt-get install -y --no-install-recommends \
         build-essential \
         cmake \
         git \
         curl \
         vim \
         ca-certificates \
         libjpeg-dev \
         libpng-dev \
         libsm6 \
         libxext6 \
         libxrender-dev \
     && rm -rf /var/lib/apt/lists/*

RUN curl -qsSLkO \
      https://repo.continuum.io/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh \
    && bash Miniconda3-4.5.4-Linux-x86_64.sh -b \
    && rm Miniconda3-4.5.4-Linux-x86_64.sh

ENV PATH=/root/miniconda3/bin:$PATH

# RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
#      chmod +x ~/miniconda.sh && \
#      ~/miniconda.sh -b -p /opt/conda && \
#      rm ~/miniconda.sh && \
#      /opt/conda/bin/conda install -y python=$PYTHON_VERSION numpy pyyaml scipy ipython mkl mkl-include cython typing && \
#      /opt/conda/bin/conda install -y -c pytorch magma-cuda90 && \
#      /opt/conda/bin/conda clean -ya
# ENV PATH /opt/conda/bin:$PATH
# This must be done before pip so that requirements.txt is available
RUN conda install -y pytorch torchvision -c pytorch

RUN conda install -y \
    numpy \
    h5py \
    pandas \
    matplotlib \
    seaborn \
    scikit-learn \
    pandas
RUN conda install -c conda-forge jupyterlab
RUN pip install opencv-contrib-python

RUN conda clean --yes --tarballs --packages --source-cache

COPY jupyter_notebook_config.py /root/.jupyter/

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

CMD jupyter lab --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=