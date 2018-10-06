FROM sachinruk/ds_base

RUN apt-get update && apt-get install -y graphviz xvfb python-opengl swig
# RUN pip install graphviz
# RUN pip install mlagents
# RUN pip install pyvirtualdisplay
RUN pip install gym 
RUN pip install box2d 
RUN pip install box2d-kengz

RUN conda config --append channels conda-forge
RUN conda install -y pytorch-cpu torchvision-cpu -c pytorch
RUN conda install -y JSAnimation

RUN conda clean --yes --tarballs --packages --source-cache

COPY jupyter_notebook_config.py /root/.jupyter/

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

CMD xvfb-run -s "-screen 0 1400x900x24" jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=
