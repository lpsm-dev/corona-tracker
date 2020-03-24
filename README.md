Corona Tracker
============

[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/lpmatos/corona-tracker) [![Contributors](https://img.shields.io/github/contributors/lpmatos/corona-tracker)](https://github.com/lpmatos/corona-tracker/graphs/contributors) [![MIT License](https://img.shields.io/github/license/lpmatos/corona-tracker)](https://github.com/lpmatos/corona-tracker/blob/master/LICENSE) [![Languages](https://img.shields.io/github/languages/count/lpmatos/corona-tracker)](https://github.com/lpmatos/corona-tracker) [![Top Language](https://img.shields.io/github/languages/top/lpmatos/corona-tracker)](https://github.com/lpmatos/corona-tracker) [![GitHub fork](https://img.shields.io/github/forks/lpmatos/corona-tracker?style=social)](https://github.com/lpmatos/corona-tracker/network/members) [![GitHub stars](https://img.shields.io/github/stars/lpmatos/corona-tracker?style=social)](https://github.com/lpmatos/corona-tracker/stargazers) [![GitHub watchers](https://img.shields.io/github/watchers/lpmatos/corona-tracker?style=social)](https://github.com/lpmatos/corona-tracker/watchers)

<p align="center">
  <img src="/docs/images/COVID.jpg" width="500px" float="center"/>
</p>
<h1 align="center">🦠 Python Project COVID-19 Tracker 🦠</h1>
<p align="center">
  <strong>Cases COVID-19 in Brazil and in the World</strong>
</p>

## Copyright (c)

Lucca Pessoa da Silva Matos (c) 2020 - **GitHub Repository**

## Getting Started

To use this repository you need to make a **git clone**:

```bash
git clone --depth 1 https://github.com/lpmatos/corona-api-tracker.git -b master
```

Pull requests are welcome. If you'd like to support the work and buy me a ☕, I greatly appreciate it!

<a href="https://www.buymeacoffee.com/EatdMck" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 100px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## Organization

* **/code** in this folder we have the application.
* **/docs** is the directory where we have all documentation files.
* **CHANGELOG.md** is a versioning file usend to control development versions.
* **docker-compose.yml** is the **Docker** container orchestrator.
* **Dockerfile** is a file used to set up your **Docker** environment.
* **Makefile** is a file containing a set of automation policies.
* **README.md** is an optional file. A human-readable **README** file..
* The files found in the project root are support files to others contexts.

## Description

The idea behind this project is the construction of a simple API that consumes data collected on the current situation of COVID-19 in the world, presenting, in addition to a simple view on the cases, a view with details referring to each region/country of the country according to the population quantity.

## Pre-Requisites

**Tools**
:---:
**Python**
**Docker**
**docker-compose**

## Desenvolvimento sem Docker

### Usage

In the directory, install the dependencies.

```bash
npm install
```

Start React development server.

```bash
npm start
```

Await for browser window open in http://localhost:3000.

### Deployment

In the directory, install the dependencies.

```bash
npm install
```

Execute build command to create minify version to production.

```bash
npm run build
```

Will be create folder /build with the files. Inserts into HTTP server. [More information](https://create-react-app.dev/docs/deployment/)

## Desenvolvimento com Docker

Steps to build the Docker image.

### Build

```bash
docker image build -t <IMAGE_NAME> -f <PATH_DOCKERFILE> <PATH_CONTEXT_DOCKERFILE>
docker image build -t <IMAGE_NAME> . (This context)
```

### Run

Steps to run the container.

* **Linux** running:

```bash
docker container run -d -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME> <COMMAND>
docker container run -it --rm --name <CONTAINER_NAME> -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME> <COMMAND>
```

* **Windows** running:

```
winpty docker.exe container run -it --rm <IMAGE_NAME> <COMMAND>
```

### Exec

Steps to enter inside the container.

```bash
docker exec -it <CONTAINER_NAME> <COMMAND>
```

### Cleaning

Steps to clean your Docker environment. 

```bash
docker system prune -af
```

*  Stop all containers.

```bash
docker stop $(docker ps -aq)
```

*  Remove all containers.

```bash
docker rm $(docker ps -aq)
```

*  Remove all images.

```bash
docker rmi $(docker images -a)
```

*  Remove all volumes.

```bash
docker volume prune -f
```

*  Remove all network.

```bash
docker network prune -f
```

## Environment variables

**Name**  |  **Description**
:---:  |  :---:
**LOG_PATH**  |  Just the Log Path
**LOG_FILE**  |  Just the Log File
**LOG_LEVEL**  |  Just the Log Level
**LOGGER**  |  Just the Logger name

## Built with

- [Python](https://www.python.org/)
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## How to contribute

1. Make a **Fork**.

2. Follow the project organization.

3. Add the file to the appropriate level folder - If the folder does not exist, create according to the standard.

4. Make the **Commit**.

5. Open a **Pull Request**.

6. Wait for your pull request to be accepted.. 🚀

Remember: There is no bad code, there are different views/versions of solving the same problem. 😊

## Add to git and push

You must send the project to your GitHub after the modifications

```bash
git add -f .
git commit -m "Added - Fixing somethings"
git push origin master
```

## Pomodoro Tasks

- [x] Create the first Dockerfile with multistage builds strategy.
- [x] Test Dockerfile with multistage.
- [x] Create log class and config class.
- [x] Adding exceptions handlers in log class and config class.
- [x] Customize log with coloredlogs.
- [x] Create simple ASCII Art with pyfiglet module.
- [x] Adding request class.
- [x] Adding Bing Corona to get information.

## TODO

- Implement country information search using restcountries API.

## Contacts

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

* **Email**: luccapsm@gmail.com
* **Linkedin**: www.linkedin.com/in/lucca-pessoa-4abb71138/

[![Facebook](https://github.frapsoft.com/social/facebook.png)](https://www.facebook.com/lucca.pessoa.9)
[![Github](https://github.frapsoft.com/social/github.png)](https://github.com/lpmatos)

## Versioning

- [CHANGELOG](CHANGELOG.md)

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Links References:

* Projects:
    * https://github.com/pomber/covid19
    * https://github.com/Doc-McCoy/bot-corona-tracker

* Datasets:
    * https://github.com/CSSEGISandData/COVID-19

* APIs:
    * https://restcountries.eu/rest/v2/
    * https://www.bing.com/covid/data
    * https://thevirustracker.com/api

* Strategys:
    * https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3

## Get to Know

| Link  | Description  |
|:------|:-------------|
| [Coronavirus](https://www.who.int/health-topics/coronavirus) | World Health Organization. |
| [Novel coronavirus (COVID-19)](https://www.who.int/emergencies/diseases/novel-coronavirus-2019) | World Health Organization. |

## Current Status

| Link  | Description  |
|:------|:-------------|
| [WHO](https://www.who.int/emergencies/diseases/novel-coronavirus-2019) | World Health Orginization. |
| [CDC](https://www.cdc.gov/coronavirus/2019-ncov/about/index.html) | Center for Disease control. |

## Contributors ✨

<table>
  <tr>
    <td align="center"><a href="https://github.com/lpmatos"><img src="https://avatars2.githubusercontent.com/u/58797390?s=400&v=4" width="100px;" alt=""/><br /><sub><b>Lucca Pessoa</b></sub></a><br /><a href="https://github.com/lpmatos/omnistack/commits?author=lpmatos" title="Code">💻</a></a></td>
  <tr>
</table>

## Autor

<table>
  <tr>
    <td align="center"><a href="https://github.com/lpmatos"><img src="https://avatars2.githubusercontent.com/u/58797390?s=400&v=4" width="100px;" alt=""/><br /><sub><b>Lucca Pessoa</b></sub></a><br /><a href="https://github.com/lpmatos/omnistack/commits?author=lpmatos" title="Code">💻</a> <a href="#lpmatos" title="Design">🎨</a></td>
  <tr>
</table>

## Project Status

* 🔛 In production
