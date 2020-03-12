FROM ubuntu

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
    h5py \
    pandas \
    jupyter \
    matplotlib \
    scikit-learn

RUN conda config --append channels conda-forge
RUN conda install -y tensorflow keras

RUN apt-get update && apt-get install -y graphviz xvfb python-opengl
RUN pip install graphviz xgboost

RUN conda clean --yes --tarballs --packages --source-cache

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

CMD xvfb-run -s "-screen 0 1400x900x24" jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=
