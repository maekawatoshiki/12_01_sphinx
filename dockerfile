FROM python:slim

RUN pip install pylint flake8 autopep8 sphinx sphinx-rtd-theme \
    && apt -y update \
    && apt -y install git make diffutils patch

WORKDIR /mnt/12_01_sphinx
