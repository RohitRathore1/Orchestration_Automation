#!/bin/bash

# Update and upgrade the VM
sudo apt-get update && sudo apt-get upgrade -y

# Install anaconda for managing python versions and dependencies
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
bash Anaconda3-2023.09-0-Linux-x86_64.sh -b
source ~/anaconda3/bin/activate
source ~/.bashrc

# Install Ray with support for GPUs
conda create -c conda-forge python=3.9 -n ray-gpu
conda activate ray-gpu
conda install -c conda-forge "ray-default"