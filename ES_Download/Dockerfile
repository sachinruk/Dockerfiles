FROM sachinruk/miniconda3

RUN conda install -y \
    numpy \
    pandas

RUN pip install urllib3 elasticsearch requests_aws_sign
RUN conda clean --yes --tarballs --packages --source-cache

VOLUME /notebook
WORKDIR /notebook

RUN apt-get update && apt-get install -y --no-install-recommends openssh-server
