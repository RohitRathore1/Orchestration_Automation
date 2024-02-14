#!/bin/bash

# Activate the Ray environment
source ~/anaconda3/bin/activate ray-gpu

# Prompt the user to enter the head node IP address
read -p "Enter the head node IP address to join the Ray cluster: " head_node_ip

# Join the Ray cluster using the provided IP address
ray start --address="$head_node_ip:6379" --num-gpus=1 --block
