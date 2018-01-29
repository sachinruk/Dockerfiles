FROM sachinruk/ds_base

RUN apt-get update && apt-get install -y graphviz xvfb python-opengl
RUN pip install graphviz xgboost

RUN apt-get install -y cmake zlib1g-dev libjpeg-dev libav-tools xorg-dev libboost-all-dev libsdl2-dev swig
RUN pip install 'gym[all]'

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

CMD xvfb-run -s "-screen 0 1400x900x24" jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=
