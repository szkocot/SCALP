# Ubuntu
FROM ubuntu:18.04
RUN apt-get update

# Miniconda
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

# intel optimized python
RUN conda update conda && conda config --add channels intel

# separate env for project
RUN conda create  -y -n bbd intelpython3_core python=3
RUN echo "source activate bbd" > ~/.bashrc
ENV PATH /opt/conda/envs/bbd/bin:$PATH

# python dependencies
RUN source activate bbd && while read requirement; do conda install --yes $requirement || pip install $requirement; done < python_requirements.txt

# TODO: Web deps installation and testing.