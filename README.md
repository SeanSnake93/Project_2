<!-- START - links -->
<!-- [links]: link -->

[docker]: https://www.docker.com/
[docker-repo]: https://hub.docker.com/repositories
[gcp-firewall-rules]: https://console.cloud.google.com/networking/firewalls/list
[gcp-vm]: https://console.cloud.google.com/compute/instances
[git]: www.github.com
[git-bash]: https://git-scm.com/downloads
[git-project]: www.github.com/SeanSnake93/Project_2
[site]: 35.246.12.58:5000
[trello]: https://trello.com/b/d1QbbJeG

<!-- END --- links -->

# [Project_2][site]

QA Indevisual Project 2 ~ Version 

I am going to be intergrating a database to hold the content inside tables.
I will be looking to allow a function to add films to the table in this sprint.

The goal is to intergrate a table into the system using a GCP SQL folling on from Version 1,
using it as a base to improve upon.

Submit by Date: 15th june

## Contents

* [Introduction](#project_2)
    * [My Project Plan](#my-project-plan)
* [Planning Documentation](#planning-documentation)
    * [Trello](#trello)
    * [Enitiy Relationship Diagram](#enitiy-relationship-diagram)
    * [Risk Assesment](#risk-assesment)

### My Project Plan

    Using the data already compiled, create a table in SQL and add some data into the tables manually.
    It is for me to intergrate a way for the user to enter data. This will inclusde the use of a Users Table. This may be done using a Service of its own.

## Planning Documentation

### Trello

I will be updating the [Trello board][trello] to allow for me to keep track of the projects development. Steps will be added to the trello board in nessasery to indercate the indervisual sprints nessasery to complete this task.

### Enitiy Relationship Diagram

**Genre**
ID
Genre

**Rating**
id
Rating

**Genre Links**
Genre ID
Film ID

**Films**
ID
Film Title
Genre(s)
Rating ID
Description

**Users**
ID
User Name
Password
First Name
Middle Names
Surname
Sex
age

### Risk Assesment

Liklyhood = Imposible (1), Unlikly (2), Likly (3), Significant (4), Imminent (5)

Impact = Minimal (1), Low (2), Medium (3), High (4), Extreem (5)


| Risk              | Risk Statment | Response Stratogy                                                                   | Objectives                                        | Liklyhood   | Impact      | Risk Level |
| :---------------- | :------------ | :---------------------------------------------------------------------------------- | :------------------------------------------------ | :---------: | :---------: | :--------: |
| Risk 1            | Accepting     | How should I tackle it?                                                             | What I expect to happen?                          | Imminent    | Extreme     | 10         |
| Implementing      | Accepting     | Build the files in stages.                                                          | Data to be visable on site using GCP SQL          | Likly       | Extreme     | 8          |
| Risk 1            | Accepting     | How should I tackle it?                                                             | What I expect to happen?                          | Imminent    | Extreme     | 10         |

Making Changes



Setting Up my SQL