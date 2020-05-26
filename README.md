<!-- [links]: link -->
[site]: 35.246.12.58:5000
[git]: www.github.com
[git-project]: www.github.com/SeanSnake93/Project_2
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

Creating a [Git Repository][git]

#### Remote Access

git config --global user.email "git@email.com"
git config --global user.name "User_Name"

#### Create .gitignore
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