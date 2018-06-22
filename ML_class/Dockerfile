FROM sachinruk/ds_base

RUN conda config --append channels conda-forge
RUN conda install -y tensorflow keras

RUN apt-get update && apt-get install -y graphviz xvfb python-opengl
RUN pip install graphviz xgboost

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

CMD xvfb-run -s "-screen 0 1400x900x24" jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=
