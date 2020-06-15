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
[screenshot1]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/trellocomplete-creenshot.png
[screenshot2]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/images/ERD.png
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
* Contents
    * [Planning Documentation](#planning-documentation)
    * Project Workflow
    
* conclustion
    * reflection


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
[screenshot1]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/Images/trello-screenshot.png
[screenshot2]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/Images/ERD.png
[screenshot3]: https://github.com/SeanSnake93/Project_2/blob/master/Documentation/Images/pipeline-flow.png
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
* [Contests](#contests)
* [Planning Documentation](#planning-documentation)
    * [Trello](#trello)
    * [Enitiy Relationship Diagram](#enitiy-relationship-diagram)
    * [Risk Assesment](#risk-assesment)


## Introduction

In this project i have created an application capable of using 4 services that work as their own entity, working together to conclude a function. Using various softwars to produce a steady CI and CD Pipeline. Incorperating an SQL to host my data and feed this back into other services.

## Contents

### Planning Documentation

#### Trello

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

#### Enitiy Relationship Diagram

![ERD][ScreenShot1]

#### Risk Assesment

**likelihood** = Imposible (1), Unlikely (2), likely (3), Significant (4), Imminent (5)

**Impact** = Minimal (1), Low (2), Medium (3), High (4), Extreme (5)

Link to [Version 1.02](https://github.com/SeanSnake93/Project_2/blob/master/Documentation/README(1.02).md#risk-assesment)
Link to [Version 2.01](https://github.com/SeanSnake93/Project_2/blob/master/Documentation/README(2.01).md#risk-assesment)

#### Workflow pipeline

![Pipeline][ScreenShot2]

1) Using GCP's VM and SQL, host a pythin Flask project.
2) using Remote Access to enable the use of Visual Studio.
3) Push to git branch any changes
4) Update Trello of build progress
5) Run pytests
6) merge to Master
7) push to Docker Hub using push from the terminal or git webhook (git is longer to process)
8) Git webhook activates Jenkins build
9) Jenkins using Ansible will distribute all content across network
10) Pulling current images from Docker including NginX for port mapping.
11) Deploy accress Swarm.

#### Docker Hub

Storing the images on Docker hub has allowed me to keep track of the versions created in stages.
Each has been given a code that resembles the stage they where at.

1.01 and 1.02 are the stages holding static data.
2.01 is the stage created to hold SQL data instead of the static.

[Service-1 Repository](https://hub.docker.com/repository/docker/seansnake93/service-1)
[Service-2 Repository](https://hub.docker.com/repository/docker/seansnake93/service-2)
[Service-3 Repository](https://hub.docker.com/repository/docker/seansnake93/service-3)
[Service-4 Repository](https://hub.docker.com/repository/docker/seansnake93/service-4)

## Conclusion

Some in the Risk assesment have remained the same as although the files are up and running, if any future development was to happen the systme could be damaged to the point of breaking the application.


| Risk              | Risk Statment | Response Stratogy                                                                   | Objectives                                        | likelihood   | Impact      | Risk Level |
| :---------------- | :------------ | :---------------------------------------------------------------------------------- | :------------------------------------------------ | :----------: | :---------: | :--------: |
| Risk 1            | Accepting     | How should I tackle it?                                                             | What I expect to happen?                          | Imminent     | Extreme     | 10         |
| IP Change         | Accepting     | Check the IP Address on GCP for any chnages.                                        | All systems run as expected.                      | Imminent     | Extreme     | 10         |
| Launch failure    | Reducing      | Monitor the changes made in trello regarding hosting.                               | The *site* should be accessable.                  | Unlikely     | High        | 6          |
| Service Failure   | Reducing      | Have key variables print their content to track it's progress.                      | Services delivers content as expected.            | Unlikely     | High        | 6          |
| Brake Service     | Reducing      | Use a Development Branch and only upload to master when the version is working.     | Always have a master version that is working.     | Unlikely     | medium      | 5          |
| Santex Error      | Undefined     | Keep the code simple and use good practice during development.                      | Project should run as expected.                   | Unlikely     | High        | 6          |
| Data Failure      | Undefined     | All data should match witn no typos, i.e name == name.                              | Services delivers content as expected.            | Unlikely     | Medium      | 5          |
| Link Failure      | Reducing      | Use the terminla to monitor Service responce.                                       | All links on the site deliver expected outcome.   | Unlikely     | Medium      | 5          |
| Retunrning Empty  | Reducing      | Using terminal prints and static data to fix outcome.                               | Pre-defined data to be visible on site.           | Unlikely     | Low         | 5          |
| Limited Lists     | Undefined     | Values used to randomise content in the list are not limited to its current length. | Intervention not needed when adding new content.  | Unlikely     | Extreme     | 7          |
| File Corruption   | Reducing      | Store backups of the project in a Docker Verson Controle system.                    | Version Controle each working maser upload.       | Unlikely     | Low         | 4          |
| Testing failure   | Reducing      | Define tests before system development.                                             | Tests I define are to pass upon project creation. | likely       | Medium      | 6          |
| Testing Coverage  | Reducing      | Tests should cover 80+% of the site or higher.                                      | All Tests should be a success.                    | likely       | low         | 5          |
| User Error        | Reducing      | Have key variables print their content to track it's progress.                      | Services delivers content as expected.            | Unlikely     | Low         | 3          |
| GCP Cost          | Reducing      | Turn off Virtual Machine when not in use.                                           | Credit to be saved and longate the use of my GCP. | Unlikely     | High        | 6          |
| Underachive       | Reducing      | Use the metrics provided to assure the minimal marks have been aquired.             | Minimal project specification to be achived.      | Unlikely     | Extreme     | 7          |
| Overeaching       | Reducing      | Scale the project to meet to the brief first.                                       | A version of the minimal spec is archived.        | likely       | Medium      | 6          |
| Health and Safety | Reducing      | Take breaks from the screen every couple of hours.                                  | Minimise the chance of headaches as fatigue.      | likely       | High        | 7          |
| Stranded Data     | Reducing      | Data has no use within the project, only adding to its footprint size.              | Minimise the length of data and use of variables. | Unlikely     | Medium      | 5          |
| Project Theft     | Undefined     | All, if any sensative data are to be encripted and Virtual Machine is secure.       | The Project is secure.                            | Unlikely     | Extreme     | 7          |
| Knowlege          | Reducing      | Build the areas i know and reaserch areas I don't, ask questions about the project. | Have a clear understanding of thechnologies used. | likely       | High        | 7          |
| Site Runs Slow    | Accepting     | Try to keep code efficent and consise in each Services.                             | For my project to load in a reasonable time.      | likely       | Low         | 5          |
| Unfinished Document | Reducing    | Provide extensive documentation on the development of my project.                   | Documentation is clear and is followed easily.    | Unlikely     | High        | 6          |