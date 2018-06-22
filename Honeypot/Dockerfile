FROM sachinruk/ds_base

RUN conda config --append channels conda-forge
RUN conda install -y tensorflow keras

RUN conda install -y plotly

RUN conda clean --yes --tarballs --packages --source-cache

RUN pip install geoip2 gensim

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888
CMD jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=
