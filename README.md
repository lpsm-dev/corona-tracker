Corona API Tracker
============

[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/lpmatos)

The idea behind this project is the construction of a simple API that consumes data collected on the current situation of COVID-19 in the world, presenting, in addition to a simple view on the cases, a view with details referring to each region/country of the country according to the population quantity.

## Copyright (c)

Lucca Pessoa da Silva Matos (c) 2020 - **GitHub Repository**.

## Getting Started

To use this repository you need to make a **git clone**:

```bash
git clone --depth 1 https://github.com/lpmatos/corona-api-tracker.git -b master
```

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

## Contacts

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

---

* **Email**: luccapsm@gmail.com
* **Linkedin**: www.linkedin.com/in/lucca-pessoa-4abb71138/

---

[![Facebook](https://github.frapsoft.com/social/facebook.png)](https://www.facebook.com/lucca.pessoa.9)
[![Github](https://github.frapsoft.com/social/github.png)](https://github.com/lpmatos)

## Versioning

- [CHANGELOG](CHANGELOG.md)

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

- [] Implement country information search using restcountries API.

## Project Status

* In production
