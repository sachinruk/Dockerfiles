FROM sachinruk/miniconda3

RUN conda install -y \
    h5py \
    pandas \
    jupyter \
    matplotlib \
    seaborn \
    scikit-learn \
    pandas

RUN conda config --append channels conda-forge

RUN pip install -y tensorflow keras

RUN conda install -y numpy

RUN conda clean --yes --tarballs --packages --source-cache
