FROM ubuntu

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    poppler-utils \
  && rm -rf /var/lib/apt/lists/*

RUN curl -qsSLkO \
      https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-`uname -p`.sh \
    && bash Miniconda3-latest-Linux-`uname -p`.sh -b \
    && rm Miniconda3-latest-Linux-`uname -p`.sh

ENV PATH=/root/miniconda3/bin:$PATH

RUN conda install -y pandas

RUN pip install requests lxml beautifulsoup4

VOLUME /notebook
WORKDIR /notebook
