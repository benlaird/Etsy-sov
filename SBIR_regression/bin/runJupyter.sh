#!/bin/bash -x

user=$USER

if [ "$user" != "root" ]; then
    echo "Must be root in docker to run this command, exiting..."
    exit 1
fi

pip install jupyter >& /dev/null
cd /root/SBIR_regression
jupyter notebook --NotebookApp.token='' --port=8081 --ip=0.0.0.0 --allow-root --no-browser . &


