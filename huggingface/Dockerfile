FROM sachinruk/miniconda3

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    ca-certificates

RUN conda install -y \
    h5py \
    pandas \
    jupyter \
    matplotlib \
    scikit-learn \
    pyarrow

RUN conda install pytorch torchvision cpuonly -y -c pytorch

RUN pip install git+https://github.com/huggingface/transformers.git

RUN conda clean --yes --tarballs --packages --source-cache

COPY jupyter_notebook_config.py /root/.jupyter/
COPY custom.js /root/.jupyter/


VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

CMD jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=