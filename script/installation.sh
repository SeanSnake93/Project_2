#!/bin/bash
  
sudo cp ect/systemd/system/flask.service ect/systemd/system/

sudo systemcrl daemon-reload

sudo systemcrl enable flask.service

source venv/bin/activate

pip install -r requirments.txt

source /var/lib/jenkins/workspace/Project_2/venv/bin/activate

python3 /var/lib/jenkins/workspace/Project_2/app.py
