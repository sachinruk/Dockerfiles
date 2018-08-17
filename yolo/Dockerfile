FROM ubuntu

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
  && rm -rf /var/lib/apt/lists/*

RUN curl -qsSLkO \
      https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-`uname -p`.sh \
    && bash Miniconda3-latest-Linux-`uname -p`.sh -b \
    && rm Miniconda3-latest-Linux-`uname -p`.sh

ENV PATH=/root/miniconda3/bin:$PATH

RUN RUN conda install -y \
    h5py \
    pandas \
    jupyter \
    matplotlib \
    seaborn \
    scikit-learn

RUN pip install opencv-python
RUN pip install opencv-contrib-python

WORKDIR /
RUN git clone https://github.com/pjreddie/darknet.git
WORKDIR /darknet
# Set OpenCV makefile flag (already done)
RUN sed -i 's/OPENCV=1/OPENCV=0/' Makefile
RUN make
ENV DARKNET_HOME /darknet
ENV LD_LIBRARY_PATH /darknet

## Download and compile YOLO3-4-Py ##
WORKDIR /
RUN git clone https://github.com/madhawav/YOLO3-4-Py.git
WORKDIR /YOLO3-4-Py
RUN pip3 install pkgconfig
RUN pip3 install cython
RUN python3 setup.py build_ext --inplace

RUN conda clean --yes --tarballs --packages --source-cache

VOLUME /YOLO3-4-Py
EXPOSE 8888
CMD jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=