FROM ubuntu

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    cmake \
  && rm -rf /var/lib/apt/lists/*

RUN curl -qsSLkO \
      https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-`uname -p`.sh \
    && bash Miniconda3-latest-Linux-`uname -p`.sh -b \
    && rm Miniconda3-latest-Linux-`uname -p`.sh

ENV PATH=/root/miniconda3/bin:$PATH

RUN conda install -y \
    h5py \
    pandas \
    jupyter \
    matplotlib \
    seaborn \
    scikit-learn \
    pandas

RUN conda config --append channels conda-forge
RUN conda install -y pytorch-cpu torchvision-cpu -c pytorch
RUN conda install -y JSAnimation

RUN apt-get update && apt-get install -y graphviz xvfb python-opengl swig
RUN pip install graphviz
RUN pip install gym pyvirtualdisplay box2d box2d-kengz

RUN conda clean --yes --tarballs --packages --source-cache

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

CMD xvfb-run -s "-screen 0 1400x900x24" jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=
