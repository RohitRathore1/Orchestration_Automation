To reproduce this `setup.yml` file, you should have amsible in your environment. If you don't
have it, you can install it using the following command:

```bash
$ sudo apt-add-repository ppa:ansible/ansible
$ sudo apt-get update
$ sudo apt install ansible
$ ansible --version
```

Further, you can follow more guide from `README.md`.

Now after verifying ansible installation, `cd` to `src` directory using the following command:

```bash
$ cd src
$ ansible-playbook -i hosts.ini setup.yml
```

This will run the `setup.yml` file and install all the required packages and dependencies.

Enjoy the automation! :smile:
