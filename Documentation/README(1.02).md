<!-- START - links -->
<!-- [links]: link -->

[docker]: https://www.docker.com/
[docker-repo]: https://hub.docker.com/repositories
[gcp-firewall-rules]: https://console.cloud.google.com/networking/firewalls/list
[gcp-vm]: https://console.cloud.google.com/compute/instances
[git]: www.github.com
[git-bash]: https://git-scm.com/downloads
[git-project]: www.github.com/SeanSnake93/Project_2
[git-webhook]: https://github.com/SeanSnake93/Project_2/settings/hooks
[screenshot1]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/trello-screenshot.png
[screenshot2]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/creategcp-screenshot1.png
[screenshot3]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/creategcp-screenshot2.png
[screenshot4]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/CreateRule-screenshot2.png
[screenshot5]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/openports-screenshot.png
[screenshot6]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/vasialsudiologo.png
[screenshot7]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/visualstudio-remote.png
[screenshot8]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/shebang-screenshot1.png
[screenshot9]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/shebang-screenshot2.png
[screenshot10]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/Dockerlogo.png
[screenshot11]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/routes-screenshot1.png
[screenshot12]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/routes-screenshot2.png
[screenshot13]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/routes-screenshot3.png
[screenshot14]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/routes-screenshot4.png
[screenshot15]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/homepage-screenshot.png
[screenshot16]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/aboutpage-screenshot.png
[screenshot17]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/homepage5000-screenshot.png
[screenshot18]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/jenkins-logo.png
[screenshot19]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/initialjenkinsPassword-screenshot.png
[screenshot20]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/jenkinsSetUp-screenshot.png
[screenshot21]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/pipeline-screenshot.png
[screenshot22]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/pipelineSettings-screenshot.png
[screenshot23]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/webhook-screenshot.png
[screenshot24]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/jenkins-build.png
[site]: 35.246.12.58
[trello]: https://trello.com/b/d1QbbJeG

<!-- END --- links -->

# [Project_2][site]

QA Indevisual Project 2 ~ Version 1

Using Flask to create a project that will takes advantage of 4 or more Services to run a function.
The Services are to be built with the help of Docker and I am to demonstrate good practice through out the build process.

Submit by Date: 15th june

## Contents

* [Introduction](#Introduction)
    * [My Project Plan](#my-project-plan)
* [Planning Documentation](#planning-documentation)
    * [Trello](#trello)
    * [Enitiy Relationship Diagram](#enitiy-relationship-diagram)
    * [Risk Assesment](#risk-assesment)
* [Set-Up Process](#set-up-process)
    * [Creating Virtual Machine](#creating-virtual-machine)
        * [Opening ports](#Opening-ports)
        * [Importing Git Repository](#importing-git-repository)
        * [Remote Access](#remote-access)
        * [Create .gitignore](#create-gitignore)
        * [Creating a *Shebang* git push](#creating-a-Shebang-git-push)
    * [Set Up Docker](#set-up-docker)
* [Development](#development)
    * [Creating Developers Branch](#creating-developers-branch)
    * [Creating my app files](#creating-my-app-files)
        * [Test Driven Development](#test-driven-development)
            * [test_back_end.py](#project2/service_#/application/tests/test_back_end.py)
        * [Python Files](#python-files)
            * [app.py](#project2/service_#/app.py)
            * [__init __.py](#project2/service_#/application/__init-__.py)
            * [routes.py](#project2/service_#/application/routes.py)
        * [Web Page Creation](#web-page-creation)
            * [layout.html](#project2/service_1/application/templates/layout.html)
            * [home.html](#project2/service_1/application/templates/home.html)
            * [about.html](#project2/service_1/application/templates/about.html)
    * [Creating Docker Images](#creating-docker-images)
        * [Creating Version Control System](#creating-version-control-system)
        * [Uploading Images to Docker Hub](#uploading-images-to-docker-hub)
    * [Creating and Removing Containers](#creating-and-removing-containers)
    * [Setup Docker Compose](#setup-docker-compose)
        * [Creating a .yaml file](#creating-a-yaml-file)
            * [docker-compose.yaml](#project2/docker-compose.yaml)
        * [Running Docker Compose](#running-docker-compose)
            * [Testing Docker Compose Containers](#testing-docker-compose-containers)
        * [Dropping Docker Compose](#dropping-docker-compose)
    * [Jenkins](#jenkins)
        * [Set Up Jenkins](#set-up-jenkins)
        * [Systemctl Jenkins](#systemctl-jenkins)
        * [Jenkinsfile](#jenkinsfile)
    * [Ansible](#ansible)
        * [Install Ansible](#install-ansible)
        * [Playbook](#playbook)
        * [Roles](#roles)
    * [Docker-Swarm](#docker-swarm)
        * [Install Docker-Swarm](#install-docker-swarm)
        * [Assigning Nodes](#assigning-nodes)
* [Index](#index)
    * [File Index](#file-index-(dev-level-1))
    * [Installations](#installations)
    * [Merge](#merge)


## Introduction

In this Project uploaded to Git I have used Python, Flask and Docker techniques to produce a Service based site. The site will generate a random selection from a Genre list and use it to filter out a Movie from my Collection and present it to the user. 

### My Project Plan

* To use each Service as a layer to the overall build process.
* A Services to select a Genre from a dynamic list.
* A Service using peramiters recived to filter a Movie from a dynamic list that matches.
* A dedicated Service used for compiling the Data recived into a presentable format.
* The final Serviced used for the front end interface to display the site and demonstrate my Project.

## Planning Documentation

### Trello

Link to visit my [Project_2 Trello Board][trello].

![trello-screenshot][ScreenShot1]

Using **MoSCoW** to break up the elements of the site into tasks that I...

- Must Have (`100`-`199`)
- Should Have (`200`-`299`)
- Could Have (`300`-`399`)
- Would Have (`400`-`499`)

...during the development of the project.

To indercate what MoSCoW level I will be focusing on, I will number each task with a clear indercator.<br />
This can be seen above in brackets, anything bellow 100 (`1`-`99`) will be planning documentation.

### Enitiy Relationship Diagram

As the project requires us to me to Services and not a database I will be using static data.<br />
Entities Generated by both Services will be displayed to the user.  

The total number of Lists created is "2", They are as follows...

**Genre**
> tag(s) (i.e. Action, Drama, Horror etc);

**Films**
> Film Name;
> Genre Tag(s);

### Risk Assesment

My risk Assesment will be taking into consideration any possibly damaging risks that could happen to my project.<br />
Looking at the indervisual step needed and the areas that they could go wrong in each.<br />
Using the likelihood and Impact of each risk to messure each risk, providing a Risk Level to each ranging from 1 to 10.<br />

likelihood = Imposible (1), Unlikely (2), likely (3), Significant (4), Imminent (5)

Impact = Minimal (1), Low (2), Medium (3), High (4), Extreme (5)


| Risk              | Risk Statment | Response Stratogy                                                                   | Objectives                                        | likelihood   | Impact      | Risk Level |
| :---------------- | :------------ | :---------------------------------------------------------------------------------- | :------------------------------------------------ | :---------: | :---------: | :--------: |
| Risk 1            | Accepting     | How should I tackle it?                                                             | What I expect to happen?                          | Imminent    | Extreme     | 10         |
| Launch failure    | Reducing      | Monitor the changes made in trello regarding hosting.                               | The *site* should be accessable.                  | likely       | High        | 7          |
| Service Failure   | Reducing      | Have key variables print their content to track it's progress.                      | Services delivers content as expected.            | likely       | High        | 7          |
| Brake Service     | Reducing      | Use a Development Branch and only upload to master when the version is working.     | Always have a master version that is working.     | Significant | High        | 8          |
| Santex Error      | Undefined     | Keep the code simple and use good practice during development.                      | Project should run as expected.                   | likely       | Medium      | 6          |
| Data Failure      | Undefined     | All data should match witn no typos, i.e name == name.                              | Services delivers content as expected.            | Unlikely     | Medium      | 5          |
| Link Failure      | Reducing      | Use the terminla to monitor Service responce.                                       | All links on the site deliver expected outcome.   | Unlikely     | Medium      | 5          |
| Retunrning Empty  | Reducing      | Using terminal prints and static data to fix outcome.                               | Pre-defined data to be visible on site.           | likely       | Low         | 5          |
| Limited Lists     | Undefined     | Values used to randomise content in the list are not limited to its current length. | Intervention not needed when adding new content.  | Unlikely     | Extreme     | 7          |
| File Corruption   | Reducing      | Store backups of the project in a Docker Verson Controle system.                    | Version Controle each working maser upload.       | Unlikely     | High        | 6          |
| Testing failure   | Reducing      | Define tests before system development.                                             | Tests I define are to pass upon project creation. | likely       | Medium      | 6          |
| Testing Coverage  | Reducing      | Tests should cover 80+% of the site or higher.                                      | All Tests should be a success.                    | likely       | High        | 7          |
| User Error        | Reducing      | Have key variables print their content to track it's progress.                      | Services delivers content as expected.            | likely       | Low         | 4          |
| GCP Cost          | Reducing      | Turn off Virtual Machine when not in use.                                           | Credit to be saved and longate the use of my GCP. | Unlikely     | High        | 6          |
| Underachive       | Reducing      | Use the metrics provided to assure the minimal marks have been aquired.             | Minimal project specification to be achived.      | Unlikely     | Extreme     | 7          |
| Overeaching       | Reducing      | Scale the project to meet to the brief first.                                       | A version of the minimal spec is archived.        | likely       | Medium      | 6          |
| Health and Safety | Reducing      | Take breaks from the screen every couple of hours.                                  | Minimise the chance of headaches as fatigue.      | likely       | High        | 7          |
| Stranded Data     | Reducing      | Data has no use within the project, only adding to its footprint size.              | Minimise the length of data and use of variables. | Unlikely     | Medium      | 5          |
| Project Theft     | Undefined     | All, if any sensative data are to be encripted and Virtual Machine is secure.       | The Project is secure.                            | Unlikely     | Extreme     | 7          |
| Knowlege          | Reducing      | Build the areas i know and reaserch areas I don't, ask questions about the project. | Have a clear understanding of thechnologies used. | likely       | High        | 7          |
| Site Runs Slow    | Accepting     | Try to keep code efficent and consise in each Services.                             | For my project to load in a reasonable time.      | likely       | Low         | 5          |
| Unfinished Document | Reducing    | Provide extensive documentation on the development of my project.                   | Documentation is clear and is followed easily.    | Unlikely     | High        | 6          |

## Set-Up Process
### Creating Virtual Machine

To create my Virtual Machine I used the [Google Cloud Platform][gcp-vm] and created an instance. <br />
The settings changed from the default where the Region (`eroupe-west2`) and Boot disk (`Ubuntu`, `Ubuntu 18.04 LTS`).

![Create GCP VM - 1][screenshot2]
![Create GCP VM - 2][screenshot3]

Once done I clicked `Create` to build my instance.

#### Opening ports

![Create Firewall Rule][screenshot4]

To enable ports on my VM I needed to edit the ports my machine has access to. This is done by using GCP's [Firewall Rules][gcp-firewall-rules] found in the `VCP Network` tab. In here I created Ports with the following settings.

![Open Firewall Rule][screenshot5]

| open-flask                                                     |
| :------------------------------------------------------------- |
| Targets<br />->  All instances in the network                  |
| Source filters<br />-> IP Ranges : 0.0.0.0/0                   |
| Protocols and ports<br />->  tcp : 5000                        |

| open-jenkins                                                   |
| :------------------------------------------------------------- |
| Targets<br />->  All instances in the network                  |
| Source filters<br />-> IP Ranges : 0.0.0.0/0                   |
| Protocols and ports<br />->  tcp : 8080                        |

Returning to the [Virtual Machine Instance's][gcp-vm] and entering my Virtual Machine to edit its setting. <br />
Scrolling down to Network Tags I enter the Port name's (i.e. open-flask) I wished to open and press space to add the port.<br />
When ports are added click save to enable the changes.

#### Importing Git Repository

Creating a [**Git repository**][git] to import over and hold my projects files. I created my repo with `Initialize this repository with a README` ticked (this was to not have an empty repo upon creation).

Once a New repo is made, clicking on `Clone or download` and copying the code inside / or copying the url link. 

Returning to the SSH terminal on my [Vitrual Machine][gcp-vm] I wish to copy my git repo over, so by using the following command...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `git clone https://github.com/SeanSnake93/Project_2.git`      | {Uploaded}                                                 |

I am able to clone/copy my git repo over to the VM, as can be seen by using...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `ls`                                                          | "Project_2"                                                |

I can then enter this file by using... 

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `cd Project_2/`                                               | :~/Project 2$                                              |

And to confirm it is my new repo, I should have a "read me" file inside my folder.

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `ls`                                                          | "README.md"                                                |

#### Remote Access

![Visual Studio Code][screenshot6]

In order to use my SSH remotly on **Visual Studio** I need to create a keygen. This can be created on the SSH terminal or by using [**Git Bash**][git-bash] on your local machine. By using the Git Bash terminal, the file will land directly on your system in the directory location Git Bash was launched.

Heading (on Windowns) to the `C:/Users/*LocalName*/.ssh` or `~/.ssh` directory and right clicking inside and selecting the option to `Git Bash Here`. Within the terminal **I uses**/use the following commands...

| Code Input *- Bash*                                               | Output                                                              |
| :---------------------------------------------------------------- | :------------------------------------------------------------------ |
| `ssh-keygen -t rsa -b 4096 -C "my@gitemail.com"`                  | "Enter a file in which to save the key (/c/Users/you/.ssh/id_rsa):" |
| {Enter Directory} *or* {**Press Enter to use default directory**} | "Enter passphrase (empty for no passphrase):"                       |
| {Enter passphrase} *or* {**Press Enter**}                         | "Enter same passphrase again:"                                      |
| {Re-enter passphrase} *or* {**Press Enter if left blank**}        | {Print out keys (id_rsa.pub; id_rsa)}                               |

Now I have 2 files in my `.ssh` directory called `id_rsa` and `id_rsa.pub`.

I can open the `id_rsa` using notepad to view the code needed or in the SSH Bash terminal use...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `cat id_rsa.pub`                                              | "Code output + = my@gitemail.com"                          |

> Note that this may fail to connect, removing the @ and all content that follows may enable fix the issue.

With the code now visable, by returning to my [Virtual Machine][gcp-vm] and entering the `edit` setting of my VM, by scrolling down I can add my Public Key to the `SSH Key`. Clicking the link to drop down the menu and paist my code into the `SSH Keys` and saving it to allow me remote access to the server via my Private Key. It is now where if you wish to change the name of you e key you can. It can be changed later however, you will need to do this next step agin to change the new file location.

Now to allow my Local System access to find my VM I need to create a `config` file. while still in the `.ssh` directory and using **Git Bash** enter the following command.

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `touch config`                                                | {Create file "config"}                                     |
| `vim config`                                                  | {Vim/enter file "config"}                                  |

Inside this file I will need to define the Host, HostName, User, IdentityFile and declare what format. inside this file enter the following...

| Code Input *- Vim*                                            | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `i`                                                           | {Enter Insert Mode}                                        |
| `Host Project2`<br />->  `HostName {server IP}`<br />->  `User SeanSnake93`<br/>->  `IdentityFile ~/.ssh/keygen_name`<br /><br />`Host ssh`<br />->  `HostName ssh` |                                                            |
| `esc`                                                         | {Enter Command Mode}                                       |
| `:wq`                                                         | {Exit and Save}                                            |

With this file created I can now head to Visual Studio, (if `known_hosts` exists in the `.ssh` directory, delte this first then) click on the green icon situated in the bottom left of the program and select `Remote-SSH: Connect to Host...`.

As I have called my Host `Project2` I should see this name in my list and by clicking on it ill be asked what language to use, in this case `Linux`.

Now with a new window open, in the green box located in th ebottom left should say `SSH: Project2`. By clicking the Exploror tab and selecting `Open Drectory` I can have Visual Studio only show files within my project by clicking my project directory in the drop down path list and accepting.

![Connected Visual Code][screenshot7]

#### Create .gitignore

By using this file I can tell git to not upload clutter files to the repo. This includes cashe files etc; so with remote access enabled and in my home directory, I can click on the "New File" icon and enter the name `.gitignore` and start editing.

| Code Input *- Visual Studio*                                  | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `/pycache/`<br />`*.pyc`<br />`/project2-venv/`<br />`/venv/`<br />`/.vscode/` |                                           |
| `ctrl` + `s`                                                  | {Save Changes}                                             |

The `/project2-venv/` and `/venv/` files will relate to the Python3 install made later in the documentaion.

> Addition Entries made to file.
> | Code Input *- Visual Studio*                                  | Output                                                     |
> | :------------------------------------------------------------ | :--------------------------------------------------------- |
> | `*.env`<br />`chromedriver                                  ` |                                                            |
> | `ctrl` + `s`                                                  | {Save Changes}                                             |

Now I have access via my external SSH on Visual Studio, I configured my git hib so make uploading easier and help with the Shebang next.

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `git config --global credential.helper cache`                 | {Cache my credentials ~ removes the need of a password}    |
| `git config --global user.email "my@gitemail.com"`            | {Configured Email}                                         |
| `git config --global user.name "SeanSnake93"`                 | {Configured User}                                          |

#### Creating a *Shebang* git push

In the SSH terminal on Visual Studio I created a `.sh` (shell file) called `gitpush.sh`. The idea is that I can use this file to automate my `git push` process for me. By clicking the `Add File` icon I can create a file called `gitpush.sh` and begin to edit.

| Code Input *- Visual Studio*                                  | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `#!/usr/bun/env bash`<br /><br />`git add .`<br /><br />`git commit -m "Shebang Commit"`<br /><br />`git push` |                   |
| `ctrl` + `s`                                                      | {Save Changes}                                             |

Now the file has been created with the following commands inside I want to run it. The file as it stands hold has **Read** and **Write** permissions but to use this as a Shebang I need to enable the **Exicute** permissions.

This can be doen a couple of ways.<br />
By using the command...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `ls -l`                                                      | "-rw-rw-r-- 1 seansnake93 seansnake93 14382 May 27 17:14 README.md"<br />"-rw-rw-r-- 1 seansnake93 seansnake93  1845 May 27 17:45 gitpush.sh" |

I will recive a list of the files in my current directory with its Permissions (Read, Write, Exicute), Group and User.<br />
For referance the tabel bellow should help with the breakdown of Permissions...

| Permissions                                                   | Description                                                |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| d---------                                                    | Decares it is a directory.                                 |
| -rwx------                                                    | Read, Write and Exicute Privlages for Owner.               |
| ----rwx---                                                    | Read, Write and Exicute Privlages for Group.               |
| -------rwx                                                    | Read, Write and Exicute Privlages for all other users.     |

To allow the `gitpush.sh` to have **Execute** Permissions you can use the command...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `chmod +x ./gitpush`                                          | {Adds Execute Permissions to all Users}                    |

Now I can check to see if the file Permissions have changed...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `ls -l`                                                      | "-rw-rw-r-- 1 seansnake93 seansnake93 14382 May 27 17:14 README.md"<br />"-rw**x**rw**x**r-**x** 1 seansnake93 seansnake93  1845 May 27 17:45 gitpush.sh" |

I can see the Execute (`x`) Permissions is now present on the file. If I run this file in the SSH terminal in its directory location...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `./gitpush.sh`                                                | {All files pushed to git with "Shebang Commit" as comment} |

Now with the file working, I want to make this accessable to me anywhere in the directory. I did this by copying the file to the `bin`. this enables the file to be accessed using a smaller command than having to provide the full directory.

As the file is working I clicked on `New Folder` and called it `script` and in it another called `shebang` and moved the file into this location. This is to store my commands in the same place as a libary of custom scripts easy to find and edit if need be.

To copy the file into the bin and change the files Permissions to enable the Execute requires the following commands...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `sudo su`                                                     | {Change to "root" User}                                    |
| `cp /gitpush.sh /bin/gitpush.sh`                              | {Copy file into "/bin" location}                           |
| `chmod +x /bin/gitpush`                                       | {Adds Execute Permissions to all Users}                    |
| `sudo su seansnake93`                                         | {Return to seansnake93 User}                               |

Now that the file has been moved into `/bin` I am able to run a simple command anywhere in my directory to have the script run...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `gitpush`                                                     | {All files pushed to git with "Shebang Commit" as comment} |

> *This file has since been modified to ask for custom comments for commit's to git with yes/no prompts before* `git commit -m` *and* `git push`*.* 

![gitpush - 1][ScreenShot8]
![gitpush - 2][screenshot9]

### Set Up Docker

![Docker][screenshot10]

I have chose to use [Docker][docker] to enable me to create images, store within containers to then be held within a volume. 

To install Docker I used the following command...

`curl https://get.docker.com | sudo bash`

In order to use any docker comands we will need to put `sudo docker ...` but, we can change this to remove the need of typing `sudo`. This can be achived by using the following command...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `sudo usermod -aG docker $(whoami)`                           | {Remove the need to put sudo befor docker}                 |

Having now run this I can run Docker's welcome screen without the need to include `sudo`...
> This may require a system restart or by creating a new group will enable Docker to run.

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `newgrp docker`                                               | {Creates a new group}                                      |
| `docker run --rm hello-world`                                 | Hello from Docker!<br />This message shows that your installation appears to be working correctly.<br /><br />To generate this message, Docker took the following steps:<br />1. The Docker client contacted the Docker daemon.<br />2. The Docker daemon pulled the "hello-world" image from the Docker Hub.<br />(amd64)<br />3. The Docker daemon created a new container from that image which runs the<br />executable that produces the output you are currently reading.<br />4. The Docker daemon streamed that output to the Docker client, which it to your terminal.<br /><br />To try something more ambitious, you can run an Ubuntu container with:<br />$ docker run -it ubuntu bash<br />Share images, automate workflows, and more with a free Docker ID:<br />https://hub.docker.com/<br /><br />For more examples and ideas, visit:<br />https://docs.docker.com/get-started/ |

Now I know Docker is installed and working I no longer need the *Image* it created. To remove the file I need its IMAGE ID, to do this I generated a list of my current Images using...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `docker images`                                               | {Print out Images Table (seen Bellow)} |

> | REPOSITORY  | TAG    | IMAGE ID     | CREATED      | SIZE   |
> | :---------- | :----- | :----------- | :----------- | :----- |
> | hello-world | latest | bf756fb1ae65 | 4 months ago | 13.3kB |

Now this is done I can copy the IMAGE ID and add it to the Remove Image command, removing the *hello-world* file...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `docker rmi bf756fb1ae65`                                      | Untagged: hello-world:latest<br />Untagged: hello-world@sha256:6a65f928fb91fcfbc963f7aa6d57c8eeb426ad9a20c7ee045538ef34847f44f1<br />Deleted: sha256:bf756fb1ae65adf866bd8c456593cd24beb6a0a061dedf42b26a993176745f6b<br />Deleted: sha256:9c27e219663c25e0f28493790cc0b88bc973ba3b1686355f221c38a36978ac63 |

### Development

#### Creating Developers Branch

With the use of Visual Studio, by clicking on the option labled "Master" in the bottom left corner.
This then will show an option in the Visual Studio menu to "Create new branch...".

I called my other branch `Dev`, It is in here i will work before uploading content to the master. Only complete (Working) versions are allowed to be merged with the Master.

If a branch was not mady using this I could visit [my Git Hub repository][git-project] and create one or use the following command in the SSH terminal.

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `git checkout -b Dev`                                         | {Created and moved to new branch called "Dev"}+            |

To confirm that I have entered the "Dev" branch I can use the following command to highlight (*) what my currently branch is...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `git branch`                                                  | * Dev<br />  master                                        |

#### Creating my app files

Using the Dev branch I can now develop my files. In order to make sure I recive the result I want I'll will be creating it set of constraints that my project must complete, this will be the first stage of Development.

##### Test Driven Development

In order to enable the use of all 3 services ill be using HTTP request to send and recive data from different entities. As the data is to display a random selection of movie. it must be able to do the following...
* Site must be reachable
    - The site must be available on the standard (HTTP://) Port 80
* All links must reach location
    - All hyperlinks must work to produce the desired output
* Recive a valid value
    - Any process based buttons must function as expected
* Successful data transfure
    - Data when sent is recived by the oncomming service

###### Project2/Service_#/application/tests/test_back_end.py

> **Service_1**
>> * Test to see if pages loads successfully
>> * Test to see if buttons direct you to the right location
>> * Test to see if the content generated is acceptable

> **Service_2**
>> * Test request status
>> * Test requested data from Service 3
>> * Test requested data from Service 4

> **Service_3**
>> * Test request status
>> * Test random output values

> **Service_4**
>> * Test request status
>> * Test recived data value
>> * Test filtering
>> * Test output value

##### Python Files

Developing a project with 4 Services can become cluttered and using additional files like I will can enable me to expand much faster as the skeletal structure is in place, the project should not only tell me what line is an issue exitst but also what file. This method is also best practice.

###### Project2/Service_#/app.py

This file is used to contain the port infomation needed in order to be accessed by the open internet and is also importing the app from my `__init__` file. The port selected in this file and service must also match the other times is called upon throughout the project.

> **Service_1**
>> App port: `5000`

> **Service_2**
>> App port: `5001`

> **Service_3**
>> App port: `5002`

> **Service_4**
>> App port: `5003`

> Note: the port selected can be any avaibale port(, Idealy not a default port used by another service). 

###### Project2/Service_#/application/__init __.py

This file is used to host some of my key vairables on the site. As the data being used is static, I will not be including Table data in this version. Imported features like Flask and request from the flask moduel, this will enale the site to use the app.py file to configure the name for the current visable element. The last import is the routes. This will enabel this file to interact with the routes.py file once the app has been generated.

> Routes must be situated at the base of this file to prevent errors. This is because the app must be built before it can recive any route data.

###### Project2/Service_#/application/routes.py

This file I have imported my app as to enable its functionality on the site, some features from flask (render_template and request,) are used to display my site and allow data to travel toO and from each indervisual service. 

![Service1 routes][screenshot11]

> **Service_1**
>> Url extention(s): `:5000/` or `:5000/home`
>> Available method(s): `GET` only
>> Requests Service 2 to return an answer in a text formate.
>> Return data to the user on the front end page with a template called "Project 2 Generator" in a variable called movie.
>
>> Url extention(s): `:5000/about`
>> Available method(s): `GET` only
>> Return to the user a front end page with the template called "About Project 2".

![Service2 routes][screenshot12]

> **Service_2**
>> Url extention(s): `:5001/generate`
>> Available method(s): `GET` and `POST`
>> Requests Service 3 to return a response in a text formate.
>> Requests Service 4 to return a response using a filterer provided be Service 3 in a text formate.
>> Return a sting to Service 1 containing the date formated from responses recived from Service 3 and Service 4.

![Service3 routes][screenshot13]

> **Service_3**
>> Url extention(s): `:5002/randomgenre`
>> Available method(s): `GET` and `POST`
>> Defined a list holding static [genre] data.
>> Aquire a value from the [genre] list using a random select and return it back to Service 2.

![Servvice4 routes][screenshot14]

> **Service_4**
>> Url extention(s): `:5003/<genre>`
>> Available method(s): `GET` and `POST`
>> Define an empty list to later hold filtered "Options".
>> Define a list holding static [movie] data.
>> From the list take each entry and its attributes [title, genre(s)] 1 by 1.
>> If any of the [movie]'s genre(s) match the value recived from Service 2, add to the "Options" list.
>> Return back to Service_2 a value from the "Options" list using the random select.

#### Web Page Creation

###### Project2/Service_1/application/templates/layout.html

This file was created to hold the header and footer menus and any imports required, in the center of the body content I have utilised the capability of Flasks `render_template` to created a "block" area called `body_content` in order to simplify the other html files content. When any other page is requested, this file will also be called to complete the missing content.

| Code Input *- HTML* |
| :------------------ |
| `<html>`<br />    `<head>`<br />        `<title>Movie Generator - {{ title }}</title>`<br />    `</head>`<br />    `<body>`<br />        `{% block body_content  %}`<br />        `{% endblock  %}`<br />    `</body>`<br/>`</html>` |

###### Project2/Service_1/application/templates/home.html

Extending from the "layout.html", This block displays the results given by the `movie` filtering function and a button that is used to refresh the page and repeate the function.

![homepage html][screenshot15]

| Code Input *- HTML* |
| :------------------ |
| `{% extends "layout.html" %}`<br /><br />`{% block body_content %}`<br />    Enter Content<br />`{% endblock %}` |

###### Project2/Service_1/application/templates/about.html

![aboutpage html][screenshot16]

All content within this page is used to dispaly the projects functionality. This page is being used to explain the expected outcomes of my applications features and functions.

### Creating Docker Images

Now I have installed Docker on my Machine I will need to create an image of my indevisual services to begin version control.

First I Login to my docker account from within the SSh terminal...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `docker login`                                                | Username: <br />Password:                                  |

In order to create an Image I will first need to create a Dockerfile holding Instructions as to how I wish to create the file.

###### Project2/Service_#/Dockerfile

Entering the SSH terminal and creating the file using...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | :--------------------------------------------------------- |
| `touch Dockerfile`                                            | {Dockerfile created in current directory}                  |

> Note: The file must have a capital "D" in `Dockerfile`.

Entering the file I have included the following commands within my "Service_1" directory...

| Code Input *- Dockerfile*                                                                                                  |
| :------------------------------------------------------------------------------------------------------------------------- |
| `ARG PYTHON_VERSION=3.7`<br /><br />`FROM python:latest`<br /><br />`RUN mkdir /opt/services/`<br /><br />`COPY . /opt/services/`<br /><br />**`WORKDIR /opt/services/application/templates/`**<br /><br />**`RUN sed -i "s/{{PYTHON_VERSION}}/${PYTHON_VERSION}/g" home.html`**<br /><br />`WORKDIR /opt/services/`<br /><br />`RUN pip3 install -r requirements.txt`<br /><br />`EXPOSE 5000`<br /><br />`ENTRYPOINT ["/usr/local/bin/python3", "app.py"]` |

Above I have highlighted 3 lines in **bold**. With the use of a `--build-arg` in the `docker build` command I am able to change the version of Python I wish to use. Lines (9-11) however will not be included in my other services 2-4 `Dockerfile`, this is because they do not have web pages to host. For line 17, the `EXPOSE` port will chnage for each service. I have increased the port by 1 for each (5001, 5002, 5003) as to simplify the process.

#### Creating Version Control System

With my Dockerfile(s) created in each of my services I can now create my images to capture the current version.
To structure my Versions I will be creating a 3 tear code. The format is as follows... `service-{service Number}:{Development Version}.{Version Sprint}`

| Code Input *- Bash*                                                          | Output                                          |
| :--------------------------------------------------------------------------- | :---------------------------------------------- |
| `docker build -t service-1 --build-arg PYTHON_VERSION=3.7 ./Service_1/`      | {Creates an Image of Service 1}                 |
| `docker build -t service-2 ./Service_2/`                                     | {Creates an Image of Service 2}                 |
| `docker build -t service-3 ./Service_3/`                                     | {Creates an Image of Service 3}                 |
| `docker build -t service-4 ./Service_4/`                                     | {Creates an Image of Service 4}                 |

> The commands above will create the image with the tag latest. If a unique tag is to be included then use the following...
> "docker build -t service-2`:1.01` ./Service_#/" for example.

With my images now created I used the following to see their details...

| Code Input *- Bash*                                      | Output                                                          |
| :------------------------------------------------------- | :-------------------------------------------------------------- |
| `docker images`                                          | {Print out Container Table (seen Bellow)}                       |

#### Uploading Images to Docker Hub

To upload files to the Docker hun the file requires the addition of a username.
the file format is as follows... `{Docker Username}/{Image Name}:{Tag}`

To create this file we can run the following command(s) to copy an Image and change its name...

| Code Input *- Bash*                                      | Output                                                          |
| :------------------------------------------------------- | :-------------------------------------------------------------- |
| `docker tag service-1:latest seansnake93/service-1:1.01` | {Copy and Rename Image with new Tag}                            |
| `docker tag service-1:latest seansnake93/service-2:1.01` | {Copy and Rename Image with new Tag}                            |
| `docker tag service-1:latest seansnake93/service-3:1.01` | {Copy and Rename Image with new Tag}                            |
| `docker tag service-1:latest seansnake93/service-4:1.01` | {Copy and Rename Image with new Tag}                            |

With the new images created I can look at my images to see if all have been created. The new Images with the edited name and tag is ready to be push to my [Docker Hub Repositories][docker-repo] using the following commands...

| Code Input *- Bash*                                      | Output                                                          |
| :------------------------------------------------------- | :-------------------------------------------------------------- |
| `docker push seansnake93/service-1:1.01`                 | {Push new Image to Docker Repository}                           |
| `docker push seansnake93/service-2:1.01`                 | {Push new Image to Docker Repository}                           |
| `docker push seansnake93/service-3:1.01`                 | {Push new Image to Docker Repository}                           |
| `docker push seansnake93/service-4:1.01`                 | {Push new Image to Docker Repository}                           |

> My Images took a minute to upload and a couple more = to be visible in my Repositories. 

### Creating and Removing Containers

With each image built I wanted to test to see if they show details I expected to see by putting each within a "Container", done by using...

| Code Input *- Bash*                                     | Output                                                          |
| :------------------------------------------------------ | :-------------------------------------------------------------- |
| `docker run -d -p 5000:5000 --name service_1 service-1` | {Creates service_1 container}                                   |
| `docker run -d -p 5001:5001 --name service_2 service-2` | {Creates service_2 container}                                   |
| `docker run -d -p 5002:5002 --name service_3 service-3` | {Creates service_3 container}                                   |
| `docker run -d -p 5003:5003 --name service_4 service-4` | {Creates service_4 container}                                   |

> the `-d` detaches the command from the terminal, allowing foe me to use the terminla after activating the "Container".

With my Containers created, by using the following command I get to see a table containing the details of each "Active Container"...

| Code Input *- Bash*                                      | Output                                                          |
| :------------------------------------------------------- | :-------------------------------------------------------------- |
| `docker ps`                                              | {Print out Active  Container Table (seen Bellow)}                |

> | CONTAINER ID | IMAGE      | COMMAND                | CREATED        | STATUS       | PORTS                  | NAMES     |
> | :----------- | :--------- | :--------------------- | :------------- | :----------- | :--------------------- | :-------- |
> | aaaa         | ver-1.1.01 | "/usr/local/bin/pyth…" | 23 minutes ago | Up 5 minutes | 0.0.0.0:5000->5000/tcp | service_1 |
> | bbbb         | ver-2.1.01 | "/usr/local/bin/pyth…" | 21 minutes ago | Up 5 minutes | 0.0.0.0:5001->5001/tcp | service_2 |
> | cccc         | ver-3.1.01 | "/usr/local/bin/pyth…" | 20 minutes ago | Up 5 minutes | 0.0.0.0:5002->5002/tcp | service_3 |
> | dddd         | ver-4.1.01 | "/usr/local/bin/pyth…" | 18 minutes ago | Up 5 minutes | 0.0.0.0:5003->5003/tcp | service_4 |

>> The "Containter ID" will be made up of a random asort of letters and numbers. But to keep my documentation clear I will use the simple ID's.

if a "Container" fails to provide a port it may not show in this list. By using the following command, I am able to so all "Containers" within my project...

| Code Input *- Bash*                                      | Output                                                          |
| :------------------------------------------------------- | :-------------------------------------------------------------- |
| `docker ps -a`                                           | {Show all containers}                                           |

If the "Container" exists but, is not active some of the code my be wrong with the Dockerfile or Service files.

For more details abou the debug I can use the following to print it out on the display...

| Code Input *- Bash*                                      | Output                                                          |
| :------------------------------------------------------- | :-------------------------------------------------------------- |
| `docker logs aaaa`                                       | {Debug container(s) service_1}                                  |

When happy with my containers, I removed them to begin setting up "Docker Compose", This requires me to stop them before removing each "Container", this is done by using...

| Code Input *- Bash*                                      | Output                                                                     |
| :------------------------------------------------------- | :------------------------------------------------------------------------- |
| `docker stop service_1`                                  | {Stop container called service_1}                                          |
| `docker stop service_2 service_3 service_4`              | {Stop container(s) called service_2 + service_3 + service_4}               |
| `docker rm service_1`                                    | {Remove container called service_1}                                        |
| `docker rm service_2 service_3 service_4`                | {Remove container(s) called service_2 + service_3 + service_4}             |

### Setup Docker Compose

Install commands

| Code Input *- Bash*                                      | Output                                                          |
| :------------------------------------------------------- | :-------------------------------------------------------------- |
| `sudo apt update`                                        | {This will make sure jq and curl are available to installed}    |
| `sudo apt install -y curl jq`                            | {Install curl and jq}                                           |

To download the latrst version use the command bellow...

`version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')`

| Code Input *- Bash*                                      | Output                                                          |
| :------------------------------------------------------- | :-------------------------------------------------------------- |
| `sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose` | {Send the file to the bin (so we can call it as a function)} |
| `sudo chmod +x /usr/local/bin/docker-compose`            | {Make the file moved into the bin a executable file}            |
| `docker-compose --version`                               | {Confirm installation be seeing the version installed}          |

#### Creating a .yaml file

This file is created so that my applications may then run the build process of each image located in each service.

###### Project2/docker-compose.yaml

This file when started will construn the images located online(, dowloading them if not local) to the spesifications detailed. Using the port numbers consistant with the port provided in the app.py files. Declaring the version of python and using Nginx as a port forwarding service to host my site. this is done with the help of a "nginx.cong" file.

###### Project2/nginx/nginx.conf

This file is used to ensure that the application then asked to run from the standard port `80` it directs the user to the the port `5000` location instead.

![homepage on port 80][screenshot17]

#### Running Docker Compose

With the pages created, in order to allow the services to work together I need to run them in a group of containers. With the creation of my "docker-compose.yaml" I'll be able to do this. By using the command bellow I can have the system create and run my image containers to test the sites functionality.

| Code Input *- Bash*                                    | Output                                                             |
| :----------------------------------------------------- | :----------------------------------------------------------------- |
| `docker-compose up`                                    | {Lauch current or build no existing images with terminal debug}    |
| `docker-compose up -d`                                 | {Lauch current or build images detached from terminal debug}       |
| `docker-compose up -d --build`                         | {Build and replace any changes to images detached from terminal debug} |

> When using the `--build` extention creates new images, overwiting the name of the old image. This means that the old image will become a void image called `<none>`.
> To remove all of these images created you can use the following command:
>> `docker images --no-trunc | grep '<none>' | awk '{ print $3 }' | xargs -r docker rmi` Remove all `<none>` images (some may require force `-f` extention).

##### Testing Docker Compose Containers

If for any reason i have an error in my code. the container may not be set as an active container (has no active port). To see what container may be the issue you can use this to...

| Code Input *- Bash*                                    | Output                                                             |
| :----------------------------------------------------- | :----------------------------------------------------------------- |
| `docker ps`                                            | {List all active containers}                                       |

If all are running, the functions intergrated may still have output issues and they can be seen using `logs`. This can only be seen when attached to the build terminal however, if the detach `-d` function is used when starting the build you can print them out using the following command...

| Code Input *- Bash*                                    | Output                                                             |
| :----------------------------------------------------- | :----------------------------------------------------------------- |
| `docker-compose logs`                                  | {Produce a readout of the status in all services}                  |

This is ok but, some outputs can be so long that your unable to review the full report presented. To focus on a single service you can do a couple of things. You can return to the [Firwall Rules][gcp-firewall-rules] on GCP and allow the port to your service, this will enable you to open the page and activly see its output. This can prove the output is what is expected, just not being recived correctly. Another option is to use `docker ps` and with the "CONTAINER ID" (abcd1234) use the following...

| Code Input *- Bash*                                    | Output                                                             |
| :----------------------------------------------------- | :----------------------------------------------------------------- |
| `docker logs abcd1234`                                 | {Provide the logs towards a single service.}                       |

> When using the detached `-d` function and testing logs. Actions must be taken on the site to produce a reading. If pages are not opened or links are not tested, the readout will not display it. When attached the readout is live, meaning buttons pressed produce logs instantly on screen.

#### Dropping Docker Compose

If detached from the terminal, to turn off the active containers you can use the following commands. Some will also remove images (to solve rebuild bugs,) from your current build or all images within your project.

| Code Input *- Bash*                                    | Output                                                             |
| :----------------------------------------------------- | :----------------------------------------------------------------- |
| `docker-compose down`                                  | {Turn off active containers and keep images}                       |
| `docker-compose down --rmi local`                      | {Turn off active containers and remove images related to it}       |
| `docker-compose down --rmi all`                        | {Turn off active containers and remove all images stored on machine} |

Now with containers that run as expected I want to allow for my service to build automaticly within a CI and CD pipeline.

### Jenkins

![Jenkinslogo][screenshot18]

With the use of Jenkins I am able to produce a Continues Intergration Pipeline by making use of webhooks on Git, I will be able to send any new pushs to the `master` branch direct to Jenkins, this will then comence the build process for me.

#### Set Up Jenkins

To access Jenkins I need to open port `8080` in [Firwall Rules][gcp-firewall-rules] and apply it to my machine. As Jenkins uses Java, this needs to be installed first...

| Code Input *- Bash*                                    | Output                                                             |
| :----------------------------------------------------- | :----------------------------------------------------------------- |
| `sudo apt update`                                      | {Process any outstanding updates required}                         |
| `sudo apt install default-jre`                         | {Install Java to enable Jenkins to install}                        |
| `java -version`                                        | {Confirm Java is installed on the machine}                         |

Now with Java available on the system running the following commands should install Jenkins on the machine.

`wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -` {add the Jenkins repository key to the current system}

| Code Input *- Bash*                                    | Output                                                             |
| :----------------------------------------------------- | :----------------------------------------------------------------- |
| `sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'` | {Add the new Debian package to the system to allow install} |
| `sudo apt update`                                      | {Process any outstanding updates}                                  |
| `sudo apt install jenkins`                             | {Install Jenkins on the machine}                                   |

#### Systemctl Jenkins

With Jenkins installed on the system, the next thing is to activate the service. This is done through `systemctl` commands...

| Code Input *- Bash*                                    | Output                                                             |
| :----------------------------------------------------- | :----------------------------------------------------------------- |
| `sudo systemctl start jenkins`                         | {Turn on the Jenkins service}                                      |
| `sudo systemctl status jenkins`                        | {Check the status of the Jenkins service}                          |

To reach the service my status must be **active**. When happy, heading to the site on port `8080` will allow for me to begin the intergration process.

> To turn off or reboot the jenkins service, the following commands can be used...
> 
> | Code Input *- Bash*                                    | Output                                                             |
> | :----------------------------------------------------- | :----------------------------------------------------------------- |
> | `sudo systemctl restart jenkins`                       | {restart the Jenkins service}                                      |
> | `sudo systemctl stop jenkins`                          | {Turn off the Jenkins service}                                     |

#### Accessing port 8080

If not already done so, the current machine must have access to port `8080`, the Jenkins default port. This is done on GCP's [Firwall Rules][gcp-firewall-rules] and then included in the machine tags.

When the port is open. Entering the [site][Jenkins] on this port will display a page asking for an Admin password.

![Entering Jenkins Password][screenshot19]

Returning to the terminal and entering the following command will provide a password requred to enter Jenkins.

| Code Input *- Bash*                                      | Output                                                             |
| :------------------------------------------------------- | :----------------------------------------------------------------- |
| `sudo cat /var/lib/Jenkins/secrets/initialAdminPassword` | {Print out initial password}                                       |

Paisting this into Jenkins will take you to the register page, here I can create a username and password (That must be remembered).

Once done you will be presented with a couple of options to install plugins on the service.

![Setup Jenkins Pipeline][screenshot20]

Sticking with the suggested plugins I wated for the installation to finish so i can create a New Item.

#### Create Pipeline

Now having access to Jenkins I can create a "New Item" to begin my CI pipeline.

![Create Jenkins Pipeline][screenshot21]

By clicking on "New Item" I can Name and and select the type of project I want to make. Calling my project "Project_2-pipeline" and selecting Pipeline as the type of project i wish to create.

![settings of Jenkins Pipeline][screenshot22]

Attaching my Git Repository to the Pipeline and assiging it to pull from the master will mean that only if I develop and push to the master branch, I will recive any chnages in regards to the Jenkins machine.

![Webhook Setting][screenshot23]

Returning to my [Git Repository][git-project] and heading to the [webhooks][git-webhook] page in settings. I created a webhook to the Jenkins server. Setting the hook to push the data as a Json.

>It it important that the server location be to the Jenkins port and have the `/github-webhook/` extention.

#### Jenkinsfile

![Jenkins Build][screenshot24]

### Ansible

This is a program used to setup external systems with the requirments they need to achive loading an application successfully. It will be used in my case to assist in the scail out of my project. By installing this and adapting it into my Jenkinsfile and later with "Docker Swarm" I can have my project build any chnages I make to the application and have it role out without the notice of those using it.

#### Install Ansibles

As Ansible is being used to install the requirments of a machine, it is infact unable to be installed within the enviroment. What this means is that if currently in the enviroment I need to `deactivate` it before i continue.

> This may require the installation an additional python installation as it was originaly installed within the enviroment. The command to enter is, `sudo apt install python3 python3-pip`

| Code Input *- Bash*                                      | Output                                                             |
| :------------------------------------------------------- | :----------------------------------------------------------------- |
| `mkdir -p ~/.local/bin`                                  | {Make the following directory}                                     |
| `echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc`            | {Print the directory and store it in .bashrc}                      |
| `source ~/.bashrc`                                       | {Make this the sourse}                                             |
| `pip install --user ansible`                             | {Install Ansible}                                                  |
| `ansible --version`                                      | {Confirm installation by displaying currently installed version}   |

With Ansible successfully installed I can now begin to create a playbook and roles for my build process.

#### Playbook

Within my playbook I will be creating 2 processes. They will have within them roles that corespond to the stages each must procedss in order to become a functioning node within my Swarm. By using an inventory file I am able to cluster groups of servers together. This requires the IP address of the master and external nodes. To add the IP addresses to the system I need to enter the "hosts" file. To get to this I can use the command...

| Code Input *- Bash*                                      | Output                                                             |
| :------------------------------------------------------- | :----------------------------------------------------------------- |
| `vim /etc/hosts`                                         | {open known IP addresses}                                          |

> To boost the security of my system I have renamed the IP addresses for each node. This is achived my including a name directly after the IP address. This will enable me to refure the the other nodes not by their IP address but by the name i have given it.
>> This may later require attention if any node IP changes.

#### Roles

###### Project2/ansible/roles/docker/tasks/main.yml
I here I have set it to aquire the key to the repository, download trhe files and then install docker onto the systme.

###### Project2/ansible/roles/docker-swarm/tasks/main.yml
Create a list of nodes in the swarm, check if all node are active within the cluster. If not aquire the manager and worker tokens.

###### Project2/ansible/roles/docker-swarm-worker/tasks/main.yml
Enter the worker node and print the token inside, enabling the swarm.

#### SSH Access

Just like making the system accessable on my local machine, the Manager of my custer needs to be able to access the others to install any dependancies, this is done though SSH.

By making a Keygen on this node i can paist the public key inside each Worker node. this weill allow the machin to remotly access each and run the Playbook and Roles required for the specified machine. A keygen is created using the following command...#

| Code Input *- Bash*                                      | Output                                                             |
| :------------------------------------------------------- | :----------------------------------------------------------------- |
| `ssh-keygen`                                             | {create privrate and public key} |

> In the direcrory `~/.ssh` will be where the key is saved.

It is in this directory where a `config` file is need to allow this node to access the other worker nodes.

### Docker-Swarm

By including this in my project I have the oppertunity to make my site more responsive to changes with a Continues Deployment. Docker Swarm will enable me to scale my project out. By making this node a manager/master node. i can expand the network by creating one or more worker nodes to cope with higher traffic.

#### Assigning Nodes

Docker Swarm is an included feature of docker so should not require any additional installations to run. In order to make a node a Manager/Master node you are able to use the following command...

| Code Input *- Bash*                                      | Output                                                             |
| :------------------------------------------------------- | :----------------------------------------------------------------- |
| `docker swarm init`                                      | {Swarm initialized: current node (j1dd5kmzioayai2ed34kpu8y2) is now a manager.<br /><br />To add a worker to this swarm, run the following command:<br /><br />docker swarm join --token [token] [ip]:[port]<br /><br />To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.} |

With this now created I can add other nodes to my cluster by simply dropping this `docker swarm join --token [token] [ip]:[port]` inside it. If i ever need to aquire this tocken again i can use the following command...

| Code Input *- Bash*                                      | Output                                                             |
| :------------------------------------------------------- | :----------------------------------------------------------------- |
| `docker swarm join-token worker`                         | {display the token required to add a new node to cluster}          |

## Index

### Development 1 File Index

Project2/<br />
Project2/**docker-compose.yaml**<br />
Project2/**Jenkinsfile**<br />
Project2/**README.md**<br />
Project2/ansible<br />
Project2/ansible/**Inventory**<br />
Project2/ansible/**playbook.yml**<br />
Project2/ansible/roles<br />
Project2/ansible/roles/docker<br />
Project2/ansible/roles/docker/tasks<br />
Project2/ansible/roles/docker/tasks/**main.yml**<br />
Project2/ansible/roles/docker-swarm<br />
Project2/ansible/roles/docker-swarm/tasks<br />
Project2/ansible/roles/docker-swarm/tasks/**main.yml**<br />
Project2/ansible/roles/docker-swarm-worker<br />
Project2/ansible/roles/docker-swarm-worker/tasks<br />
Project2/ansible/roles/docker-swarm-worker/tasks/**main.yml**<br />
Project2/Documentation<br />
Project2/Documentation/**README(1.02).md**<br />
Project2/Documentation/Images<br />
Project2/Documentation/Images/**Screenshot Files**<br />
Project2/etc<br />
Project2/etc/systemd<br />
Project2/etc/systemd/system/**flask.service**<br />
Project2/nginx/<br />
Project2/nginx/**nginx.conf**<br />
Project2/script<br />
Project2/script/**before_installation.sh**<br />
Project2/script/**docker.sh**<br />
Project2/script/**installation.sh**<br />
Project2/script/**source.sh**<br />
Project2/script/shebang<br />
Project2/script/shebang/**gitpush.sh**<br />
Project2/Service_1/<br />
Project2/Service_1/**app.py**<br />
Project2/Service_1/**Dockerfile**<br />
Project2/Service_1/**requirements.txt**<br />
Project2/Service_1/application/<br />
Project2/Service_1/application/**__init__.py**<br />
Project2/Service_1/application/**routes.py**<br />
Project2/Service_1/application/static/<br />
Project2/Service_1/application/templates/<br />
Project2/Service_1/application/templates/**about.html**<br />
Project2/Service_1/application/templates/**home.html**<br />
Project2/Service_1/application/templates/**layout.html**<br />
Project2/Service_1/application/tests/<br />
Project2/Service_1/application/tests/**__init__.py**<br />
Project2/Service_1/application/tests/**test_back_end.py**<br />
Project2/Service_2/<br />
Project2/Service_2/**app.py**<br />
Project2/Service_2/**Dockerfile**<br />
Project2/Service_2/**requirements.txt**<br />
Project2/Service_2/application/<br />
Project2/Service_2/application/**__init__.py**<br />
Project2/Service_2/application/**routes.py**<br />
Project2/Service_2/application/tests/<br />
Project2/Service_2/application/tests/**__init__.py**<br />
Project2/Service_2/application/tests/**test_back_end.py**<br />
Project2/Service_3/<br />
Project2/Service_3/**app.py**<br />
Project2/Service_3/**Dockerfile**<br />
Project2/Service_3/**requirements.txt**<br />
Project2/Service_3/application/<br />
Project2/Service_3/application/**__init__.py**<br />
Project2/Service_3/application/**routes.py**<br />
Project2/Service_3/application/tests/<br />
Project2/Service_3/application/tests/**__init__.py**<br />
Project2/Service_3/application/tests/**test_back_end.py**<br />
Project2/Service_4/<br />
Project2/Service_4/**app.py**<br />
Project2/Service_4/**Dockerfile**<br />
Project2/Service_4/**requirements.txt**<br />
Project2/Service_4/application/<br />
Project2/Service_4/application/**__init__.py**<br />
Project2/Service_4/application/**routes.py**<br />
Project2/Service_4/application/tests/<br />
Project2/Service_4/application/tests/**__init__.py**<br />
Project2/Service_4/application/tests/**test_back_end.py**

### Installations

- `sudo apt update`
- `sudo apt install tree`
- `sudo apt install python3`
- `sudo apt install python3-pip`
- `sudo apt install python3-venv`
- `python3 -m venv project2-venv`
- `. project2-venv/bin/activate`
- **venv** `pip install flask` 
    - Flask==1.1.2
    - Jinja2==2.11.2
- **venv** `pip3 install pytest` 
    - pytest==5.4.2
- **venv** `pip3 install pytest-cov` 
    - pytest-cov==2.8.1
- **venv** `pip3 install flask-testing` 
    - Flask-Testing==0.8.0
    - Werkzeug==1.0.1
- **venv** `pip3 install requests`
    - requests==2.23.0
- `curl https://get.docker.com | sudo bash`
    - `sudo usermod -aG docker $(whoami)`
- `sudo apt update`
- `sudo apt install -y curl jq`
- `version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')`
- `sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
- `sudo chmod +x /usr/local/bin/docker-compose`
- `mkdir -p ~/.local/bin`
- `echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc`
- `source ~/.bashrc`
- `pip install --user ansible`

### Merge

- `git fetch origin`
- `git checkout -b Dev origin/Dev`
- `git merge master`
- `git statis`
- `git commit`