FROM sachinruk/miniconda3

RUN conda install -y \
    h5py \
    pandas \
    jupyter \
    matplotlib \
    scikit-learn

RUN conda clean --yes --tarballs --packages --source-cache
