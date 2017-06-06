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

RUN conda install -y theano \
                     tensorflow \
                     keras

RUN conda clean --yes --tarballs --packages --source-cache

RUN apt-get update && apt-get install -y graphviz
RUN pip install graphviz xgboost

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888
CMD jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=
