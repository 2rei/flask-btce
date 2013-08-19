#!/bin/bash
echo $0: Creating virtual environment
virtualenv --prompt="<myenv>" ./env

mkdir ./logs
mkdir ./archiv
mkdir ./pids
mkdir ./db
mkdir ./tmp
cp gunicorn.conf.py_distr gunicorn.conf.py
cp api/configs/general.py_distr api/configs/general.py


echo $0: Installing dependencies
source ./env/bin/activate
export PIP_REQUIRE_VIRTUALENV=true
./env/bin/pip install --requirement=./requirements.conf --log=./logs/build_pip_packages.log

echo $0: Making virtual environment relocatable
virtualenv --relocatable ./env

echo $0: Creating virtual environment finished.