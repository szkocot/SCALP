# base img
FROM continuumio/miniconda3

# use bash instead of sh
SHELL ["/bin/bash", "-c"]

# use python requirements from outside
ADD python_requirements.txt .

# separate env for project
RUN conda create -y -n bbd python=3.6
RUN echo "source activate bbd" > ~/.bashrc
ENV PATH /opt/conda/envs/bbd/bin:$PATH

# python dependencies
RUN source activate bbd && while read requirement; do conda install -c anaconda --yes $requirement || pip install $requirement; done < python_requirements.txt

# TODO: Web deps installation and testing.