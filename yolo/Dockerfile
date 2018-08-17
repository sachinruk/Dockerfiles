FROM ubuntu

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    curl \
    git \
  && rm -rf /var/lib/apt/lists/*

RUN curl -qsSLkO \
      https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-`uname -p`.sh \
    && bash Miniconda3-latest-Linux-`uname -p`.sh -b \
    && rm Miniconda3-latest-Linux-`uname -p`.sh

ENV PATH=/root/miniconda3/bin:$PATH

## OpenCV 3.4 Installation ##
RUN apt-get install -y build-essential cmake
RUN apt-get install -y qt5-default libvtk6-dev
RUN apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libjasper-dev libopenexr-dev libgdal-dev
RUN apt-get install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev
# RUN apt-get install -y python3-dev python3-tk python3-numpy
RUN apt-get install -y unzip wget
RUN wget https://github.com/opencv/opencv/archive/3.4.0.zip
RUN unzip 3.4.0.zip
RUN rm 3.4.0.zip
WORKDIR /opencv-3.4.0
RUN mkdir build
WORKDIR /opencv-3.4.0/build
RUN cmake -DBUILD_EXAMPLES=OFF ..
RUN make -j4
RUN make install
RUN ldconfig

WORKDIR /
RUN git clone https://github.com/pjreddie/darknet.git
WORKDIR /darknet
# Set GPU flags to none
RUN sed -i 's/OPENCV=1/OPENCV=0/' Makefile
RUN sed -i 's/GPU=1/GPU=0/' Makefile
RUN sed -i 's/CUDNN=1/CUDNN=0/' Makefile
RUN make
ENV DARKNET_HOME /darknet
ENV LD_LIBRARY_PATH /darknet

# ## Download and compile YOLO3-4-Py ##
# WORKDIR /
# RUN git clone https://github.com/madhawav/YOLO3-4-Py.git
# WORKDIR /YOLO3-4-Py
# RUN pip install pkgconfig
# RUN pip install cython
# # RUN python setup.py build_ext --inplace

# # RUN conda install -y \
# #     h5py \
# #     pandas \
# #     jupyter \
# #     matplotlib \
# #     seaborn \
# #     scikit-learn

# # RUN conda clean --yes --tarballs --packages --source-cache

# # VOLUME /YOLO3-4-Py
# # EXPOSE 8888
# # CMD jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=