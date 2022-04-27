# Installation 

!!! Reminder
    :fire: NEW VERSION ! :champagne:
    
    Old version is still [HERE](installation_old.md)


A walkthrough installation and setup of Python 3.X.X environment on Windows 10.
Those step use Windows PowerShell, This will help familiarize you with the command prompt.
First of all, open a PowerShell instance.
It will be assume your configuration follow this tutorial.

<!-- TODO : Customize PowerShell
            - Modify color
            - Modify transparancy -->

-----

## Workspace

### 1. Start PowerShell

Click Windows search button and type `Windows PowerShell` and click on `Windows PowerShell [x86]`
You should have a command prompt open now.

### 2. Change directory

First of all, move to your user directory with `cd` command.

```ps
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

C:\> cd C:\Users\*Username*
C:\Users\*Username*>
```

!!! tip
    * Type few letter and press `<TAB>` to auto-complete.
    For exemple, if you type `cd C:\Use<TAB>`, and it will auto-complete `cd C:\Users\` automaticaly.
    * If you want to list files in a directory you can use `ls`

### 3. Create a directory

Create a `PythonWorkspace` folder with `mkdir` command.
and add inside few folders :
    - `Download`
    - `Project`
    - `Settings`

```ps
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

C:\Users\*Username*>mkdir PythonWorkspace
C:\Users\*Username*> cd PythonWorkspace
C:\Users\*Username*\PythonWorkspace> mkdir Download
...
C:\Users\*Username*\PythonWorkspace> mkdir Project
...
C:\Users\*Username*\PythonWorkspace> mkdir Settings
...
```

!!! tip
    - `cd ..` : to go up one directory
    - `cd ..\..` : to go up two directory

You can verify you have all folders with `ls` when you are in your PythonWorkspace.

```ps
C:\Users\*Username*\PythonWorkspace> ls


    Directory: C:\Users\*Username*\PythonWorkspace


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       01.01.2021     08:00                Download
d-----       01.01.2021     08:00                Project
d-----       01.01.2021     08:00                Settings
```

!!! tip
    * `cls` : To clear the screen and keep only the last line on screen

If you need to delete a file or a folder you can use `del *FileName_or_FolderName`

!!! warning
    `del` don't put your file or folder in Recycle Bin and you don't have an alert message. Use it with caution.

## Python

### 1. Pyenv

Install pyenv

For windows follow the updated documentation directly on [pyenv-win](https://github.com/pyenv-win/pyenv-win)

If you get a Policy Error, try in administrator or set your policy in Powershell as administrator with `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Once you have pyenv install you can install python 3.9.6 with pyenv `pyenv install 3.9.6`

You can find another version with `pyenv install --list`

Do not use a `a` or `b` version until you know what you do.

Take the latest stable version, in the following list it will be `3.9.6`

```
...
3.9.0a3
3.9.0a4-win32
3.9.0a4
3.9.0a5-win32
3.9.0a5
3.9.0a6-win32
3.9.0a6
...
3.9.2
3.9.3-win32
3.9.3
3.9.4-win32
3.9.4
3.9.5-win32
3.9.5
3.9.6-win32
3.9.6
...
3.10.0b2-win32
3.10.0b2
3.10.0b3-win32
3.10.0b3
3.10.0b4-win32
3.10.0b4
```
Finaly set your global version of python with `pyenv global 3.9.6`

### 2. Poetry

#### Install

Powershell

```ps
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

If you get an error `Invoke-WebRequest : La demande a été interrompue : Impossible de créer un canal sécurisé ssl/TLS.`

Just change your protocol with `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12`

Normally poetry is added to path, restart your terminal and type `poetry`.

If it's not working, simply add poetry to PATH :

 `[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.poetry\bin")`


#### Set .venv folder

```ps
poetry config virtualenvs.in-project true
```


### 3. Test your install

* Open cmd and tap `python`

```ps
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\*Username*>PythonWorkspace python
Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
PS C:\Users\*Username*>PythonWorkspace
```

### 4. Setup a multi purpose project

Move to your Project folder with cd command

```ps
C:\Users\*Username*>cd PythonWorkspace\Project
C:\Users\*Username*\PythonWorkspace\Project
```
Make a new folder

```
mkdir Testing
cd Testing
```

Virtual environement permit to install package seperatly and never polute your Python install

Then init Poetry 

```ps
C:\Users\*Username*\PythonWorkspace\Project\Testing> poetry init
```
Respond to question accordingly don't feel obligated to add dependency now you will have possibility to add them later.

Activate it

```ps
C:\Users\*Username*\PythonWorkspace\Project\Testing\.venv\Scripts\activate
```

To deactivate your environemnet simply type "deactivate"

```ps
(.venv) C:\Users\*Username*\PythonWorkspace\Project\Testing\> deactivate
C:\Users\*Username*\PythonWorkspace\Project\Testing\
```

You can also use `poetry run *whatever*` it's equivalent to have a .venv activated


### 4. Install packages

!!! danger
    Nerver install package on your base python always use a virtual environement

* Install :

 with `poetry add *packagename*` or `poetry add -D *pacakagename*` for dev dependencies.poetry 
```ps
(.venv) C:\Users\*Username*\PythonWorkspace\Project\Testing\> poetry add *packagename*
```
or for developement dependencies only

```ps
(.venv) C:\Users\*Username*\PythonWorkspace\Project\Testing\> poetry add -D *packagename*
```

* Uninstall :

```ps
(lab) PS C:\Users\*Username*\PythonWorkspace> poetry remove *packagename* # with -D for dev
```

#### Package Commonly used

This list is just a basic list, you will find much more information Library.

* Science Base : scipy, numpy, matplotlib
* Calcul symbolique : sympy
* Traducteur : Babel
* COM Win32 : pywin32
* Additional GUI App : Pyside6
* AutoGUI : pyautogui
* Image : pillow
* Xlsx : openpyxl (xlrd deprecated)
* Docx : python-docx (Warning: import docx)
* Pdf : PyPDF2
* Web : requests, bs4, selenium
* Mail : ezgmail
* Linter : Pylint
* Formatter : black
* Notebook IDE : ipython jupyter jupyterlab
* And a lot more !!!

## VSCode

### 1. Install VSCode

* Go to <https://code.visualstudio.com/download>
* Download Vscode
* Run the installer
* In Extension, install Python Extension.

### 2. Setup your Environement

#### Change to JSON settings

* Click on bottom gear icon button and click settings.
* On the top right corner click on the button to "Open Settings (JSON)"
* Copy the following line in your settings.json

```json
{
    // Workbench
    "workbench.settings.editor": "json",
    "workbench.settings.openDefaultSettings": true
}
```

TODO : Update following JSON

```json
{
    // Workbench
    "workbench.colorTheme": "One Dark Pro",
    "workbench.iconTheme": "vscode-icons",
    "workbench.settings.editor": "json",
    "workbench.settings.openDefaultSettings": true,
    //Terminal
    "terminal.integrated.shell.windows": "C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
    // Editor
    "editor.formatOnSave": true,
    // Python
    "python.pythonPath": "C:\\Users\\*Username*\\PythonWorkspace\\Environment\\Base\\Scripts\\python.exe",
    "python.venvPath": "C:\\Users\\*Username*\\PythonWorkspace\\Environment",
    "python.formatting.provider": "black",
}
```

### Recomended packages

* Python
* One Dark Pro
* vscode-icons
* Markdown All in One
* Git Graph
* PlantUML

!!!info
    Corey Shaffer as made a really [good tutorial](https://youtu.be/-nh9rCzPJ20) on youtube. Watch it if you need more info.

## Git

### 1. Install Git

* Go to <https://git-scm.com/downloads>
* Download Git
* Run the installer

* Select Components window

    *Leave all default options checked and check any other additional components you want installed.*

* Choosing the default editor

    *Choose VSCode (if installed) or Notepad++*

* Adjusting your PATH environment

    *Keep the default Use Git from the command line and also from 3rd-party software.*

* Leave the default selected as Use OpenSSH

* Leave the default Use the OpenSSL library selected

* Configuring the line ending conversions

    *Select Checkout Windows-style, commit Unix-style line endings unless you need other line endings for your work.*

* Configuring the terminal emulator : Use with Git Bash window

    *Select Use Windows' default console window (or MinTTY, the default terminal of MSYS2)*

* Configuring extra options window

    *Leave the default options checked unless you need symbolic links.*

* Click the Install button

### 2. Configure Git

#### Enter your name and user name

In a PowerShell enter your global name and global email.

```ps
PS C:\> git config --global user.name "John Doe"
PS C:\> git config --global user.email johndoe@example.com
```

Verify with

```ps
PS C:\> git config --list
user.name=John Doe
user.email=johndoe@example.com
color.status=auto
color.branch=auto
color.interactive=auto
color.diff=auto
...
```
