# base img and python
FROM ubuntu:18.04
RUN apt-get update && apt-get update -y
RUN apt-get install -y python3.6 python3-pip

# use python requirements from outside
ADD python_requirements.txt .

# python dependencies
RUN pip3 install -r python_requirements.txt

# TODO: Web deps installation and testing.