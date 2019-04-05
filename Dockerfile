FROM python:2

RUN mkdir -p /opt/tvb
WORKDIR /opt/tvb
RUN git clone https://github.com/the-virtual-brain/tvb-library
RUN pip install numpy scipy matplotlib numba scikit-learn
RUN pip install Cython
RUN pip install networkx
RUN pip install nibabel pybids
RUN cd tvb-library && python setup.py install

# binder support
# https://mybinder.readthedocs.io/en/latest/tutorials/dockerfile.html#preparing-your-dockerfile
RUN pip install --no-cache-dir notebook==5.*
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}
RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}


ADD version /opt/version

ADD conn76_weights.tsv /opt/conn76_weights.tsv

# CMD python /opt/run.py conn76_weights.tsv

ADD demo1.py /opt/run.py

CMD python /opt/run.py /bids-dataset /bids-dataset 01


