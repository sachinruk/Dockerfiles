FROM ubuntu

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
  && rm -rf /var/lib/apt/lists/*

RUN curl -qsSLkO \
      https://repo.continuum.io/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh \
    && bash Miniconda3-4.5.4-Linux-x86_64.sh -b \
    && rm Miniconda3-4.5.4-Linux-x86_64.sh

ENV PATH=/root/miniconda3/bin:$PATH

RUN echo $(python --version)
