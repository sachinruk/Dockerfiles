FROM sachinruk/miniconda3

RUN conda install -y \
    mkl-service \
    h5py \
    jupyter \
    matplotlib \
    seaborn \
    scikit-learn \
    pandas \
    xlrd

RUN conda config --append channels conda-forge
RUN conda install -yc plotly plotly
RUN conda install -yc conda-forge fbprophet feather-format
RUN conda install -y pytorch torchvision cpuonly -c pytorch
RUN conda install gpytorch -yc gpytorch

RUN conda clean --yes --tarballs --packages --source-cache

COPY jupyter_notebook_config.py /root/.jupyter/
COPY custom.js /root/.jupyter/

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

CMD jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=