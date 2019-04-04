FROM python:2

RUN mkdir -p /opt/tvb
WORKDIR /opt/tvb
RUN git clone https://github.com/the-virtual-brain/tvb-library
RUN pip install numpy scipy matplotlib numba scikit-learn
RUN pip install Cython
RUN pip install networkx
RUN cd tvb-library && python setup.py install

ADD demo1.py /opt/run.py

CMD python /opt/run.py