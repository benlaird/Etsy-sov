!/bin/bash

pip install jupyter
cd /root/SBIR_regression
jupyter notebook --NotebookApp.token='' --port=8081 --ip=0.0.0.0 --allow-root --no-browser . &


