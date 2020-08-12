FROM sachinruk/miniconda3

RUN conda install -y \
    h5py \
    pandas \
    jupyter \
    matplotlib \
    scikit-learn

RUN pip install git+https://github.com/huggingface/transformers.git

RUN conda clean --yes --tarballs --packages --source-cache

COPY jupyter_notebook_config.py /root/.jupyter/
COPY custom.js /root/.jupyter/


VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

CMD jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=