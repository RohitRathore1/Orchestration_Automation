#!/bin/bash

# Activate the Ray environment
source ~/anaconda3/bin/activate ray-gpu

# Start Ray head node. Adjust memory/CPU resources as needed
ray start --head --port=6379 --num-gpus=1 --block

# Prompt the user to enter the head node IP address
read -p "Enter the head node IP address to generate the worker node join command: " head_node_ip

# Output the command to join worker nodes to this head node with the user-provided IP address
echo "Worker nodes can join the Ray cluster by running the following command:"
echo "ray start --address='$head_node_ip:6379' --num-gpus=1 --block"
