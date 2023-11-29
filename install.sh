#!/bin/sh 

# Install dependencies 
sudo apt-get install -y python3-pip
sudo pip3 install -r requirements.txt

# make the alias
echo "alias manai='~/LLM-Powered_QA_App/script.py'" >> ~/.zshrc
echo "alias manai='./script.py'" >> ~/.bashrc
