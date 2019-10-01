FROM sachinruk/miniconda3

RUN conda install -y \
    mkl-service \
    h5py \
    pandas \
    jupyter \
    matplotlib \
    seaborn \
    scikit-learn \
    pandas

RUN conda config --append channels conda-forge
RUN conda install -c conda-forge -y fbprophet

RUN conda clean --yes --tarballs --packages --source-cache

COPY jupyter_notebook_config.py /root/.jupyter/

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

CMD jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=