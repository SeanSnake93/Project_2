<!-- [links]: link -->
[site]: 35.246.12.58:5000
[git]: www.github.com
[git-project]: www.github.com/SeanSnake93/Project_2
[git-bash]: https://git-scm.com/downloads
[gcp-vm]: https://console.cloud.google.com/compute/instances
[gcp-firewall-rules]: https://console.cloud.google.com/networking/firewalls/list
[docker]: https://www.docker.com/


# [Project_2][site]
QA Indevisual Project 2

## Contests

* Introduction
    * Project Outlines
    * My Project Plan
* Planning Documentation
    * Trello
    * Enitiy Relationship Diagram
    * Risk Assesment
* Set-Up Process
    * Creating Virtual Machine
        * Opening ports
        * Importing Git Reopository
        * Remote Access
        * Create .gitignore
        * Installations
    * Creating SQL DATABASE
        * Defining Exports
    * Setting Up Jenkins
        * Creating Item
        * Creating Developers Branch
* Creation Process
    * app.py
    * models.py
    * Forms.py
    * Routes.py
* Web Page Creation
    * Layout.html
    * Home.html
    * About.html
* Testing
    * Pytest
    * Debuging
    * Pytest Coverage
    * Futher Testing
    * Integration Testing
* File Index

## Introduction
### Project Outlines

### My Project Plan


## Planning Documentation
### Trello

Using MoSCoW to break up the elements of the site into tasks that I...

- Must Have (100-199)
- Should Have (200-299)
- Could Have (300-399)
- Would Have (400-499)

...during the development of the project.

To indercate what level of MoSCoW I will be focusing on, I will number each tast as a clear indercator.<br />
This can be seen above in brackets, anything bellow 100 (1-99) will be planning documentation.

### Enitiy Relationship Diagram

As the project is to involve the use of....

I have created a total of # Tables, They are as follows...

**Table 1**
- id (*Primary Key*)
- attribute
- attribute (*Foreign Key*)

### Risk Assesment

To be added later

| Risk             | Risk Statment    | Response Stratogy       | Objectives              | Liklyhood  | Impact | Risk Level |
| :--------------- | :--------------: | :---------------------: | :---------------------: | :--------: | :----: |----------: |
| Risk 1           | Accepting        | How should I tackle it? | What I expect to happen | impossible | Low    | 1          |
| Risk 2           | Reducing         | How should I tackle it? | What I expect to happen | Unlikly    | Low    | 1          |
| Risk 3           | Undefined        | How should I tackle it? | What I expect to happen | likly      | High   | 10         |

## Set-Up Process
### Creating Virtual Machine

To create my Virtual Machine I used the [Google Cloud Platform][gcp-vm] and created an instance. <br />
The settings changed from the default where the Region (eroupe-west2) and Boot disk (Ubuntu, Ubuntu 18.04 LTS).

Once done I clicked 'Create' to produce my instance.

#### Opening ports

To enable ports on my VM I needed to edit the ports my machine has access to. This is done by using GCP's [Firewall Rules][gcp-firewall-rules] found in the 'VCP Network' tab. In here I created Ports with the following settings.

* open-flask
    - Targets
        - All instances in the network
    - Source filters
        - IP Ranges : 0.0.0.0/0
    - Protocols and ports
        - tcp : 5000

* open-jenkins
    - Targets
        - All instances in the network
    - Source filters
        - IP Ranges : 0.0.0.0/0
    - Protocols and ports
        - tcp : 8080

Returning to the [Virtual Machine Instance's][gcp-vm] and entering my Virtual Machine to edit its setting. <br />
Scrolling down to Network Tags I enter the Port name's (i.e. open-flask) I wished to open and press space to add the port.<br />
When ports are added click save to enable the changes.

#### Importing Git Reopository

Creating a [Git Repository][git] to import over and hold my projects files. I reated mt repo with "Initialize this repository with a README" ticked (this was to not have an empty repo upon creation).

Once a New repo is made, clicking on "Clone or download" and copying the code inside / or copying the url link. 

Returning to the SHH terminal on my [Vitrual Machine][gcp-vm] I wish to copy my git repo over, so by using the following command...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| *git clone https://github.com/SeanSnake93/Project_2.git*      | {uploaded}                                                 |

We are able to clone/copy our git repo over to the VM, as can be seen by using...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| *ls*                                                          | Project_2                                                  |

we are then able to enter this file by using... 

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| *cd Project_2/*                                               | :~/Project 2$                                              |

And to confirm it is my new repo, i should have a "read me" file inside my folder.

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| *ls*                                                          | README.md                                                  |

#### Remote Access

In order to use my SHH remotly I need to create a keygen. This can be created on the SHH terminal or by using [Git Bash][git-bash] on your local machine. By using the Git Bash terminal the file will land directly on your system in the directory location Git Bash is launched within.

Heading (on Windowns) to the directory "C:/Users/*LocalName*/.ssh" or "~/.shh" and right clicking will give you the option to "Git Bash Here". Within the terminal *I uses*/use the following commands...

| Code Input *- Bash*                                          | Output                                                            |
| :----------------------------------------------------------- | ----------------------------------------------------------------: |
| ssh-keygen -t rsa -b 4096 -C "my@gitemail.com"               | Enter a file in which to save the key (/c/Users/you/.ssh/id_rsa): |
| {Enter Directory} or {*Press Enter to use default location*} | Enter passphrase (empty for no passphrase):                       |
| {Enter passphrase} or {*Press Enter*}                        | Enter same passphrase again:                                      |
| {Re-enter passphrase} or {*Press Enter if left blank*}       | {Print out keys (id_rsa.pub; id_rsa)}                             |

Now we have the 2 files in our ".shh" directory called "id_rsa" and "id_rsa.pub".

We can open the "id_rsa" using notepad to view the code needed or in the Bash or SHH terminal use...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| cat id_rsa.pub                                                | {Code output ~ = my@gitemail.com}                          |

With the code now visable, by returning to out [Virtual Machine][gcp-vm] and entering the "edit" setting of out VM, by scrolling down I can add my Public Key to the "SHH Key". Clicking the link to drop down the menu and paist my code into the SHH Keys and saving it to allow me remote access to the server via my Private Key. It is now where if you wish to change the name of you e key you can. It can be changed later however, you will need to do this next step agin to change the new file location.

Now to allow my Local System access to find my VM I need to create a "config" file. while still in the ".shh" directory and using "Git Bash" enter the following command.

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| touch config                                                  | {Create file "config"}                                     |
| vim config                                                    | {vim/enter file "config"}                                  |

Inside this file we will need to define the Host, HostName, User, IdentityFile and declare what format. inside this file enter the following...

| Code Input *- Vim*                                            | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| i                                                             | {Enter Insert Mode}                                        |
| *Host Project2*<br />->  *HostName {server IP}*<br />->  *User seansnake93*<br/>->  *IdentityFile ~/.ssh/keygen_name*<br /><br />*Host shh*<br />->  *HostName shh*                                              |                                                            |
| esc                                                           | {Enter Command Mode}                                       |
| *:wq*                                                         | {Exit and Save}                                            |

With this file created we can now head to "Visual Studio", (if "known_hosts" exists in the ".shh" directory , delte this first then) click on the green icon situated in the bottom left of the program and select "Remote-SHH: Connect to Host...".

As I have called my Host "Project2" I should see this name in my list and by clicking on it ill be asked what language to use, in thei scase "**Linux**".

Now with a new window open, in the green box located in th ebottom left should say "SHH: Project2". By clicking the Exploror tab and selecting "Open Drectory" i can have "Visual Studio" only show files within my project by clicking Project to in the drop down in my directory path and accepting.

#### Create .gitignore

By using this file I can tell git to not upload clutter files to the repo. This includes cashe files etc; so with remote access enabled and in my home directory, I can click on the "New File" icon and enter the name ".gitignore" and start editing.

| Code Input *- Visual Studio*                                  | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| */pycache/*<br />**.pyc*<br />*/project2-venv/*<br />*/venv/*<br />*/.vscode/*                                                           |                                                            |
| ctrl + s                                                      | {Save Changes}                                             |

The "/project2-venv/" and "/venv/" files will relate to the Python3 install made later in the documentaion.

Now I have access via our external SHH on Visual Studio, I configured my git hib so make uploading easier and help with the Shebang next.

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| *git config --global user.email "my@gitemail.com"*            | {configured Email}                                         |
| *git config --global user.name "SeanSnake93"*                 | {configured User}                                          |

#### Creating a *Shebang* git push

In the SHH terminal on Visual Studio I created a ".sh (shell file)" called "gitpush.sh". The idea is that I can use this file to automate a lot of the Git Push process for me. By clicking the "Add File" icon I can create the file called "gitpush.sh" and begin to edit.

| Code Input *- Visual Studio*                                  | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| *#!/usr/bun/env bash*<br /><br />*git add .*<br /><br />*git commit -m "Shebang Commit"*<br /><br />*git push* |                   |
| ctrl + s                                                      | {Save Changes}                                             |

Now the file has been created with the following commands inside I want to run it. The file as it stands hold has **Read** and **Write** permissions but to use this as a Shebang we need to enable the **Exicute** permissions.

This can be doen a couple of ways.<br />
By using the command...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| *ls -l*                                                      | -rw-rw-r-- 1 seansnake93 seansnake93 14382 May 27 17:14 README.md<br />
-rw-rw-r-- 1 seansnake93 seansnake93  1845 May 27 17:45 gitpush.sh |

I will recive a list of the files in my current directory with its Permissions (Read, Write, Exicute), Group and User.<br />
For referance the tabel bellow should help with the breakdown of Permissions...

| Permissions                                                   | Description                                                |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| d---------                                                    | Decares it is a directory.                                 |
| -rwx------                                                    | Read, Write and Exicute Privlages for Owner.               |
| ----rwx---                                                    | Read, Write and Exicute Privlages for Group.               |
| -------rwx                                                    | Read, Write and Exicute Privlages for all other users.     |

To allow the "gitpush.sh" to have **Execute** Permissions you can use the command...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| *chmod +x ./gitpush*                                          | {Adds Execute Permissions to all Users}                    |

By doing this if we run the command to the file Permissions again...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| *ls -l*                                                      | -rw-rw-r-- 1 seansnake93 seansnake93 14382 May 27 17:14 README.md<br />
-rw**x**rw**x**r-**x** 1 seansnake93 seansnake93  1845 May 27 17:45 gitpush.sh |

I can see the Execute (x) Permissions is now present on the file. If I run this file in the SHH terminal in its directory location...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| *./gitpush.sh*                                                | {All files pushed to git with "Shebang Commit" as comment} |

Now with the file working, I want to make this accessable to me anywhere in the directory. I did this by copying the file to the "bin". this enables the file to be accessed using a smaller command than having to provide the full directory.

As the file is working I created a directory called "script" and in it another directory "shebang" and moved the file into this location. This is to store my commands in the same place as a libary of custom scripts easy to find and edit if need be.

To copy the file into the bin and change the files Permissions to enable the Execute requires the following commands...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| *sudo su*                                                     | {Change to 'root' User}                                    |
| *cp /Project_2/script/shebang/gitpush.sh /bin/gitpush.sh*     | {Copy file into "/bin" location}                           |
| *chmod +x /bin/gitpush*                                       | {Adds Execute Permissions to all Users}                    |
| *sudo su seansnake93*                                         | {Return to SeanSnake93 User}                               |

Now that the file has been moved into "/bin" I am able to run a simple command anywhere in my directory to have the script run...

| Code Input *- Bash*                                           | Output                                                     |
| :------------------------------------------------------------ | ---------------------------------------------------------: |
| *gitpush*                                                     | {All files pushed to git with "Shebang Commit" as comment} |

*This file has since been modified to ask for custom comments for commit's to git with yes/no prompts before "git commit -m" and "git push".* 

#### Installations



### Creating SQL DATABASE
#### Defining Exports
### Setting Up Jenkins
#### Creating Item
#### Creating Developers Branch

## Creation Process

### app.py
### models.py
###### Project2/application/models.py

### Forms.py
###### Project2/application/forms.py

### Routes.py
###### Project2/application/routes.py

### __init __.py
###### Project2/application/__init __.py

## Web Page Creation
### Layout.html
### Home.html
### About.html

## Testing
### Pytest
### Debuging
### Pytest Coverage
### Futher Testing
### Integration Testing

## File Index

# This will change
Project2/application/ <br />
Project2/application/__init __.py <br />
Project2/application/forms.py <br />
Project2/application/models.py <br />
Project2/application/routes.py <br />
Project2/application/static <br />
Project2/application/static/css <br />
Project2/application/static/css/main.css <br />
Project2/application/templates <br />
Project2/application/templates/layout.html <br />
Project2/application/templates/home.html <br />
Project2/application/templates/about.html <br />
Project2/application/templates/register.html <br />
Project2/application/templates/login.html <br />
Project2/application/templates/account.html <br />
Project2/application/templates/catalogue.html <br />
Project2/application/templates/add_movie.html <br />
Project2/application/templates/edit_movie.html <br />
Project2/application/templates/collection.html <br />
Project2/etc/ <br />
Project2/etc/systemd <br />
Project2/etc/systemd/system <br />
Project2/etc/systemd/system/flask.service <br />
Project2/script/ <br />
Project2/script/installation.sh <br />
Project2/tests/ <br />
Project2/tests/__init __.py <br />
Project2/tests/test_int.py <br />
Project2/tests/test_back_end.py <br />
Project2/test_results/ <br />
Project2/test_results/test=at-month-day-on-year-hour:month.html <br />
Project2/Risk_Assesment.xlsx Project2/requirments.txt <br />
Project2/app.py <br />
Project2/create.py <br />
Project2/chromedriver