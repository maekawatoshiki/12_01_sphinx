FROM python:slim

RUN pip install pylint flake8 autopep8 coverage sphinx sphinx-rtd-theme \
    && apt -y update \
    && apt -y install git make

WORKDIR /mnt
