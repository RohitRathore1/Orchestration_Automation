# Orchestration_Automation

If we want to design a decentralized compute platform like IO.net, which should be capable of harnessing 
GPU resources from a diverse pool of suppliers ranging from layman users to mining data centers, involves 
careful planning and robust architecture. For production purpose it should be scalable, secure, and 
user-friendly, ensuring ease of use for non-technical users while providing the necessary controls and 
scalability for more technical ones. Below, I tried to address the key components and considerations for 
such a platform.

> Questions to be answered

## Integration Strategy

> How would you approach the development of the setup script to ensure seamless integration of devices 
into the IO Net network for Ray cluster orchestration? Which technologies would you think about using 
for this task ?

For the integration of a VM or Computer into the IO.net platform, each device would need:
- **Bootstrap Agent**: A lightweight, easy-to-install software agent for initial setup and communication 
with the IO.net platform. This agent would handle initial configuration, authentication, and connection 
to the central management system.

- **Runtime Environment**: Depending on the jobs being run, a container runtime (e.g., Docker) or a virtual 
environment might be required to isolate and execute tasks securely.

- **Resource Monitoring Tool**: To report the usage of CPU, GPU, memory, and network bandwidth in real time 
to the IO.net platform for optimal task allocation.

- **Secure Communication Layer**: Implementing TLS/SSL for secure data transmission between the compute devices 
and the IO.net platform.

<!-- To ensure seamless integration into io.net network, leveraging Ansible and Docker offers a robust solution.
Ansible automates environment setup across devices, utilizing playbooks to install necessary software, 
configure network settings, and manage dependencies. This ensures consistency and reproducibility in the
deployment process, minimizing manual errors and stremlining the orchestration of Ray clusters. Docker 
complements this approach by containerizing Ray applications, guaranteeing that they run the same way, 
regardless of the underlying computing environment. Containers encapsulate the application, its dependencies, 
and runtime into a single package, fostering portability and consistency across development, testing, and 
production environments. Together, Ansible and Docker facilitate a scalable, efficient, and controlled 
deployment mechanism for complex distributed systems like Ray clusters. -->

<!-- ## Required Components

> What components are required by a bare metal VM created from scratch to run your orchestration?

For a Ray cluster on bare metal VMs, essential components ensure its functionality and performance. Python 
is required as Ray's primary programming environment. Ray itself must be installed to manage distributed 
computing tasks. Docker facilitates application containerization, ensuring consistency across various 
environments. GPU drivers are crucial for computational tasks requiring accelerated hardware. Lastly, 
proper network configurations are necessary to enable efficient communication within the cluster, ensuring 
nodes can interact and synchronize tasks effectively. This comprehensive setup supports scalable and 
efficient distributed computing. -->

## Connectivity Solutions

- **Adaptive Bandwidth Management**: Implement algorithms that can adapt the workload based on the current 
bandwidth and latency, ensuring tasks are allocated to nodes with sufficient connectivity.

- **Peer-to-Peer Architecture**: Reduce reliance on central servers for data transfer, enabling faster, more 
resilient data exchanges, especially for large datasets.

- **Fallback Mechanisms**: In case of connectivity issues, tasks should be able to pause and resume, or fallback 
to local processing if needed.

## Remote Management & Resource Pools

- **Central Management Dashboard**: A web-based UI for suppliers to monitor their devices' status, earnings, and 
health.

- **Containerization Technologies**: Utilize Docker or Kubernetes for isolating tasks, simplifying deployment, 
and managing dependencies without direct SSH access.

- **Dynamic Resource Allocation**: Implement a scheduler (e.g., Kubernetes scheduler) that can dynamically allocate 
resources based on availability, task requirements, and performance metrics.

- **Challenges**:  Balancing resource utilization, ensuring security, and handling dynamic IP addresses and network 
conditions.


## Orchestration Automation

> Describe the steps you would take to automate the orchestration of Ray clusters, particularly focusing on 
the differentiation between headnode and worker node configurations.

<!-- Automating cluster orchestration with Ansible enables scalable and flexible management of Ray clusters. By 
using dynamic inventory, Ansible can differentiate between headnode and workernodes, applying specific 
configurations through conditional tasks. This method allows for tailored setups that adapt to the cluster's 
evolving needs, making the deployment process both scalable and manageable. It streamlines the orchestration 
process, ensuring clusters are configured correctly and efficiently, while also providing the flexibility to 
adjust to different deployment environments and requirements. See [See Integration Strategy section](#integration-strategy)
for more details. -->
- **Orchestration Tools**: Kubernetes combined with custom agents on each node can automate the orchestration process. 
The headnode (master) can distribute jobs to worker nodes based on their available resources and current workload.

- **Custom Agent Communication**: Agents on each node communicate with the central platform using secure APIs, receiving 
instructions, and sending back status updates.

## Connectivity

> In a decentralized environment, having devices all over the world with different connectivity strengths and 
speed - would you do anything about the networks? If your orchestration software communicates on specific 
ports - how would you manage this as users may or may not have that port open?

In a decentralized environment, addressing connectivity challenges involves implementing Virtual Private Networks 
(VPNs) or secure tunnels like SSH tunnels or WireGuard, which encapsulate network traffic over public networks, 
ensuring secure and consistent connections across the cluster. Tools like `iptables` or `ufw` manage port configurations 
and firewall rules to open necessary ports for Ray's communication while blocking unauthorized access. Network 
security groups, especially in cloud environments, further restrict traffic to only allowed IP addresses and ports, 
enhancing security and connectivity management. These measures collectively ensure that the Ray cluster remains 
accessible and secure, even across diverse network conditions and geographies.

## Remote Management

> What technologies or methodologies would you consider for remotely managing the state of machines once they are 
integrated into the cluster? Discuss their advantages and potential challenges. In production having ssh access is 
not possible due to the nature of application and security.

For environments with restricted SSH access, leveraging tools like Ansible Tower provides an effective solution for 
remote management. Ansible Tower offers a web-based UI and APIs for automating tasks, managing configurations, and 
monitoring the state of machines across a distributed infrastructure. It allows for secure, role-based access control, 
enabling teams to execute tasks and monitor systems without direct SSH access. Similarly, Ray's dashboard provides 
real-time monitoring capabilities for the cluster, offering insights into performance metrics and system health, 
facilitating effective remote management and troubleshooting.

## Security Measures

> What security measures would you implement or recommend to ensure the secure remote management of machines within 
the Ray cluster?

For enhancing security within a Ray cluster, implement SSH key-based authentication to replace less secure password 
logins, ensuring only authorized users access nodes. Use Transport Layer Security (TLS) for encrypted communication 
between nodes to protect data in transit. Firewalls, configured via tools like `iptables` or `ufw`, limit access to 
essential ports required for Ray and application-specific traffic, blocking unauthorized access. Regularly scanning 
Docker images for vulnerabilities using tools like Docker Bench or Clair prevents deploying containers with known 
security issues. Additionally, deploying Role-Based Access Control (RBAC) within Kubernetes or similar environments 
managing access permissions ensures users have only the necessary privileges, minimizing the risk of unauthorized actions.

- **End-t-End Encryption**: Encrypt data in transit and at rest to protect sensitive information and computation results.

- **Authentication and Authorization**: Implement OAuth or JWT for secure API access, ensuring that only authenticated 
devices can join the network and receive tasks.

- **Regular Security Audits**: Conduct vulnerability assessments and updates to the bootstrap agent and any platform 
components to mitigate security risks.

> If a node will be busy then how can we assign node to the next user?

To efficiently manage a pool of computing resources where nodes might become busy and we need to assign available 
nodes to the next user, we can implement a dynamic resource allocation and scheduling system. This system can monitor 
the status of each node in real time and make intelligent decisions about where to route new user requests. Here's 
how such a system could be designed:

1) Node Status Monitoring
    -  Implement a monitoring system that tracks the current load and status of each node in real-time. This includes 
    CPU, GPU utilization, memory usage, and network bandwidth.
    - Regular health checks to ensure nodes are operational and to detect any issues proactively.

2) Dynamic Scheduling Algorithm
    - Use a priority queue or a similar data structure to manage incoming user requests. The scheduler can prioritize 
    requests based on predefined criteria (e.g., urgency, compute requirements, user tier).
    - The algorithm matches requests to nodes based on the resource requirements of the task and the current availability 
    of the nodes. This involves checking if a node is busy and, if so, finding an available node that meets the task's 
    requirements.

3) Load Balancing
    - Implement load balancing to evenly distribute workloads across the available nodes, preventing any single node 
    from becoming a bottleneck.
    - Ensure the system is scalable, allowing for the addition of more nodes easily to the pool as demand increases.

4) Queueing System for Tasks
    - When all suitable nodes are busy, incoming tasks are placed in a queue. As soon as a node becomes available, 
    tasks from the queue are assigned based on their priority and the order of arrival.
    - Users can be notified about the status of their tasks, including any delays due to high demand.

5) Failover and Redundancy
    - Implement a failover mechanism to handle cases where a node becomes unavailable or fails during task execution. 
    This ensures that tasks are not lost and can be rerouted to other available nodes.
    - Implement redundancy to ensure that there are always backup nodes available in case of failures.

> **Note:** To use Docker with GPUs, especially for the provided VMs and GPUs, we will have to ensure that NVIDIA drivers and NVIDIA 
            Docker toolkit are installed on our VMs. This setup will allow Docker containers to leverage GPU resources effectively. 
            Docker's `--gpus` flag can be used to specify GPU access for containers running Ray or other GPU-accelerated applications. 
            This approach requires the NVIDIA runtime to be set up as Docker's default or specified explicitly when running containers. 
            This ensures our Ray cluster can utilize GPU resources for compute-intensive tasks efficiently.


# Setup script
This script should be run on every VM that will be part of the Ray cluster, including the head node and 
worker nodes. It ensures that Ray and other necessary dependencies are installed. Here, I have considered
the use of Anaconda for managing python versions and dependencies but in ansible I am following python and 
pip. The script is as follows:

```bash
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
```

# Headnode script
The headnode script initializes the VM designated as the head node. It starts the Ray head process, which will 
manage worker nodes. This script also generates a command that can be used to join worker nodes to the cluster.

```bash
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
```

# Workernode script
The worker node scripts configure VMs as worker nodes. These scripts are run on the VMs designated as worker nodes 
to connect them to the head node.

```bash
#!/bin/bash

# Activate the Ray environment
source ~/anaconda3/bin/activate ray-gpu

# Prompt the user to enter the head node IP address
read -p "Enter the head node IP address to join the Ray cluster: " head_node_ip

# Join the Ray cluster using the provided IP address
ray start --address="$head_node_ip:6379" --num-gpus=1 --block
```

# Integration STrategy

Now, for seamless integration of devices into the io.net network and Ray cluster orchestration, the development of the 
setup script will leverage Ansible. Ansible is an open-source automation tool that enables idempotent deployment, making 
it ideal for consistent setup across head and worker nodes without repetitive manual intervention. This choice facilitates 
the scalability and reproducibility of cluster deployments.

## Technologies to USe:

- **Ansible**: For automating the deployment and configuration of Ray clusters.
- **Docker**: To containerize Ray applications, ensuring consistency across different environments.
- **Ray**: The primary framework for distributed computing.

## Orchestration with Ansible
The automation process will be divided into distinct phases:

- **Initial Setup (Ansible Playbooks)**: Create Ansible playbooks for the setup script, which will install Docker, Python, and 
necessary dependencies on all VMs.
- **Dynamic Configuration**: Utilize Ansible's inventory and templating features to dynamically configure the head node and worker 
nodes, passing the head node's IP address as an argument to the worker nodes.
- **Cluster Startup**: Script the Ray cluster startup using Python, with commands to initialize the head node and join worker nodes 
to the cluster based on the dynamic IP address configuration.

## Ansible Installation
To install Ansible on your local machine, run the following commands:

```bash
$ sudo apt-add-repository ppa:ansible/ansible
$ sudo apt-get update
$ sudo apt install ansible
$ ansible --version
```

Step 1: Verify Ansible Installation
Ensure Ansible is installed on your machine by running:

```bash
$ ansible --version
```

### Create Ansible Inventory

First prepare an `hosts.ini` inventory file, which is containing the IP addresses of the machines
where we want to execute the Ansible tasks. Here is the content of the file:

```ini
[headnode]
headnode1 ansible_host=149.36.0.221 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/ray_gpu

[workernode]
workernode1 ansible_host=94.101.98.216 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/ray_gpu
workernode2 ansible_host=94.101.98.190 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/ray_gpu
```

Step 2: Check Connectivity to Your VMs
Before running the playbooks, it's a good practice to check that Ansible can successfully connect to all your VMs. You can do 
this by pinging all the hosts defined in your inventory file using the Ansible ping module:

```bash
$ ansible -i hosts.ini all -m ping
```

### Create the setup playbook

This playbook will install the necessary dependencies and configurations on all the VMs. The `setup.yml` file is as follows:

```yaml
---
- name: Install dependencies to create a Ray cluster
  hosts: all
  remote_user: ubuntu
  become: true
  vars:
    arch_mapping:
      x86_64: amd64
      aarch64: arm64
    user_name: ubuntu

  tasks:
  - name: Update and upgrade all packages to the latest version
    ansible.builtin.apt:
      update_cache: true
      upgrade: dist
      cache_valid_time: 3600

  - name: Install necessary packages
    apt:
      name: "{{ packages }}"
      state: latest
      update_cache: true
    vars:
      packages:
      - python3-pip
      - python3-venv
...........................................................
...........................................................
...........................................................
```

It's not complete. It's just an example of how the playbook will look like. The playbook will install the necessary packages.
I will update later as I have complete `setup.yml` file. Now to execute the playbook against our inventory to set up all VMs,
run the following command:

```bash
(base) TeAmP0is0N@laas3-host:~/ray$ ansible-playbook -i hosts.ini setup.yml
```

### Configure the Head Node and Worker Nodes

To start our Ray cluster using the `headnode_setup.yml` and `workernode_setup.yml` playbooks, run the following command:

Step 3: Run the Head Node Setup Playbook
Start by configuring the head node. Navigate to the directory where your headnode_setup.yml file is located and run:

```bash
(base) TeAmP0is0N@laas3-host:~/ray$ ansible-playbook -i hosts.ini headnode_setup.yml 
```

Step 4: Run the Worker Nodes Setup Playbook
After the head node has been successfully configured, proceed to configure the worker nodes. Run:

```bash
ansible-playbook -i hosts.ini workernode_setup.yml
```

## Verification

Now I will verify the cluster setup by running a simple Ray program or using the Ray dashboard to ensure the nodes are correctly 
configured and communicating. After both playbooks have been executed successfully, we should verify that our Ray cluster is up 
and running correctly. We can do this by SSH'ing into the head node and using Ray commands to check the cluster status. For example:

```bash
$ ssh ubuntu@<head-node-ip> -i <path-to-your-SSH-private-key>
$ source ~/ray_env/bin/activate
$ ray status
```

## Ray Cluster Status

Use `ray status` from any node in the cluster to see the cluster's health and node details.

```bash
ubuntu@rohit-ray-test-machine-0:~$ ray status
======== Autoscaler status: 2024-02-14 09:17:14.373600 ========
Node status
---------------------------------------------------------------
Active:
 1 node_84e68fc74b546704501596e4bf4e0bb7d1288cbde44b7906b950f482
 1 node_1a0f73a4c8ec06c4c0e09986ebddae9ef88a34412459a9b3d39fc313
 1 node_a486a31c09d6db302f89565cb06c6dbab3bbbc660052e4793f757c3d
Pending:
 (no pending nodes)
Recent failures:
 (no failures)

Resources
---------------------------------------------------------------
Usage:
 0.0/18.0 CPU
 0.0/3.0 GPU
 0B/45.72GiB memory
 0B/20.58GiB object_store_memory

Demands:
 (no resource demands)
```

## Cluster Startup script using python

For the cluster startup, we can use a simple Python script to manage the startup sequence programmatically. However, managing Ray 
cluster startup directly in Python outside of a framework like Ansible for initial setup is unconventional. Typically, we would 
use Python scripts to interact with the Ray API for job submission, not for starting or stopping the cluster itself. The cluster's 
startup and management are usually handled through command-line instructions or Ansible playbooks, as shown above.

If we're looking for a way to use Python to dynamically manage our Ray cluster (e.g., adding nodes, removing nodes), we would typically 
do this through Ray's autoscaler API or by interfacing with our cloud provider's API directly for VM management, which then could be 
combined with Ray commands for cluster management.

ACcording to me, for initializing a cluster and joining nodes, the recommended approach is to use the command line or Ansible scripts as 
provided. Python would be more applicable for developing applications that run on Ray or for using Ray's APIs to manage the workload 
distribution once the cluster is up and running.

# Start Ray with the Ray Cluster Launcher

The provided `default.yaml` cluster config file will create a Ray cluster given a list of nodes.

```yaml
cluster_name: default

docker:
    image: "rayproject/ray-ml:latest-gpu"
    container_name: "ray_container"
    pull_before_run: True
    run_options:
        - --ulimit nofile=65536:65536

provider:
    type: local
    head_ip: 149.36.0.221
    worker_ips: [94.101.98.216, 94.101.98.190]

auth:
    ssh_user: ubuntu
    ssh_private_key: ~/.ssh/ray_gpu

min_workers: 2
max_workers: 2
upscaling_speed: 1.0
idle_timeout_minutes: 5

# Add your setup_commands, file_mounts, and any other configurations as necessary.

head_start_ray_commands:
    - ray stop
    - ulimit -c unlimited && ray start --head --port=6379 --autoscaling-config=~/ray_bootstrap_config.yaml

worker_start_ray_commands:
    - ray stop
    - ray start --address=$RAY_HEAD_IP:6379
```

To ensure everything is dynamic and no hardcoding is necessary, especially for the head node IP and worker nodes' IPs, 
we can utilize Ansible's inventory variables and environment variables within our Ray cluster configuration scripts. 
For SSH details, Ansible can use the inventory's SSH configurations, avoiding hardcoding. This approach requires our 
scripts and Ansible playbooks to dynamically fetch and use these details during execution, ensuring flexibility and s
calability without manual intervention for each deployment.
