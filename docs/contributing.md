## Dev Env Setup

### Pyenv

Install pyenv with pip

- Powershell or Git Bash: `pip install pyenv-win --target $HOME\\.pyenv`

- cmd.exe: `pip install pyenv-win --target %USERPROFILE%\.pyenv`

Install python 3.8.10 with pyenv `pyenv install 3.8.10`

Set pyenv local to 3.8.10 `pyenv local 3.8.10`

### Poetry

#### Install

Powershell

```ps
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

osx / linux / bashonwindows

``` bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

#### Set .venv folder

```ps
poetry config virtualenvs.in-project true
```

### Install dependencies

```ps
poetry install
```

### Run test

In poetry you can use `poetry run pytest` it activate your .venv for this command

Or `.\.venv\Scripts\activate` then `pytest`

### Create a new branch for starting developping

For exemple if we are in 0.1.6

Depending of what you want to implement :

## Hotfix

Make a branch and Pull Request on main/master.

*You will make your commit with the hotfix*
*A a new tag 0.1.7 associated with your commit*

|     | Commit                           | Description                                                                                              |
| --- | -------------------------------- | -------------------------------------------------------------------------------------------------------- |
| 1   | :bookmark: Release version 0.1.7 | *Update version number in `ydownloader/__init__.py` and add a new tag 0.1.7 associated with your commit* |
| 2   | :pencil: Update release notes    | *Update `docs\release_notes.md`*                                                                         |
| 3   | :art: Fix that bugy stuff (#15)  |                                                                                                          |

## Feature

- feature make a branch and Pull Request on the next feature release (ie : 0.1.x)

## No-Backcompatibility

- No-Backcompatibility make a branch and Pull Request on the next version release (ie : 0.2.x)



| Commit type                | Emoji                                                     |
| :------------------------- | :-------------------------------------------------------- |
| Initial commit             | :tada: `:tada:`                                           |
| Version tag                | :bookmark: `:bookmark:`                                   |
| New feature                | :sparkles: `:sparkles:`                                   |
| Bugfix                     | :bug: `:bug:`                                             |
| Metadata                   | :card_index: `:card_index:`                               |
| Documentation              | :books: `:books:`                                         |
| Documenting source code    | :bulb: `:bulb:`                                           |
| Performance                | :racehorse: `:racehorse:`                                 |
| Cosmetic                   | :lipstick: `:lipstick:`                                   |
| Tests                      | :rotating_light: `:rotating_light:`                       |
| Adding a test              | :white_check_mark: `:white_check_mark:`                   |
| Make a test pass           | :heavy_check_mark: `:heavy_check_mark:`                   |
| General update             | :zap: `:zap:`                                             |
| Improve format/structure   | :art: `:art:`                                             |
| Refactor code              | :hammer: `:hammer:`                                       |
| Removing code/files        | :fire: `:fire:`                                           |
| Continuous Integration     | :green_heart: `:green_heart:`                             |
| Security                   | :lock: `:lock:`                                           |
| Upgrading dependencies     | :arrow_up: `:arrow_up:`                                   |
| Downgrading dependencies   | :arrow_down: `:arrow_down:`                               |
| Lint                       | :shirt: `:shirt:`                                         |
| Translation                | :alien: `:alien:`                                         |
| Text                       | :pencil: `:pencil:`                                       |
| Critical hotfix            | :ambulance: `:ambulance:`                                 |
| Deploying stuff            | :rocket: `:rocket:`                                       |
| Fixing on MacOS            | :apple: `:apple:`                                         |
| Fixing on Linux            | :penguin: `:penguin:`                                     |
| Fixing on Windows          | :checkered_flag: `:checkered_flag:`                       |
| Work in progress           | :construction:  `:construction:`                          |
| Adding CI build system     | :construction_worker: `:construction_worker:`             |
| Analytics or tracking code | :chart_with_upwards_trend: `:chart_with_upwards_trend:`   |
| Removing a dependency      | :heavy_minus_sign: `:heavy_minus_sign:`                   |
| Adding a dependency        | :heavy_plus_sign: `:heavy_plus_sign:`                     |
| Docker                     | :whale: `:whale:`                                         |
| Configuration files        | :wrench: `:wrench:`                                       |
| Package.json in JS         | :package: `:package:`                                     |
| Merging branches           | :twisted_rightwards_arrows: `:twisted_rightwards_arrows:` |
| Bad code / need improv.    | :hankey: `:hankey:`                                       |
| Reverting changes          | :rewind: `:rewind:`                                       |
| Breaking changes           | :boom: `:boom:`                                           |
| Code review changes        | :ok_hand: `:ok_hand:`                                     |
| Accessibility              | :wheelchair: `:wheelchair:`                               |
| Move/rename repository     | :truck: `:truck:`                                         |