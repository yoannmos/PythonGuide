# Installation

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
    - `Environment`
    - `Project`
    - `Settings`

```ps
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

C:\Users\*Username*>mkdir PythonWorkspace
C:\Users\*Username*> cd PythonWorkspace
C:\Users\*Username*\PythonWorkspace> mkdir Download
...
C:\Users\*Username*\PythonWorkspace> mkdir Environment
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
d-----       01.01.2020     08:00                Download
d-----       01.01.2020     08:00                Environment
d-----       01.01.2020     08:00                Project
d-----       01.01.2020     08:00                Settings
```

!!! tip
    * `cls` : To clear the screen and keep only the last line on screen

If you need to delete a file or a folder you can use `del *FileName_or_FolderName`

!!! warning
    `del` don't put your file or folder in Recycle Bin and you don't have an alert message. Use it with caution.

## Python

### 1. Install Python

* Go to <https://www.python.org/downloads/>
* Download Python (*Prefer 32x version over 64x for general use*)
* Run the installer
* Click : Add Python 3.X to PATH
* Install

### 2. Test your install

* Open cmd and tap `python`

```ps
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

C:\Users\*Username*>python
Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 14 2019, 23:09:19) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### 3. Setup your virtual environement

Move to your Environment folder with cd command

```ps
C:\Users\*Username*>cd PythonWorkspace\Environment
C:\Users\*Username*\PythonWorkspace\Environment
```

Virtual environement permit to install package seperatly and never polute your Python install

Then create a Base environement

```ps
C:\Users\*Username*\PythonWorkspace\Environment>python -m venv Base
```

Activate it

```ps
C:\Users\*Username*\PythonWorkspace\Environment>Base\Scripts\activate
```

You should see

```ps
(Base) C:\Users\*Username*\PythonWorkspace\Environment>
```

To deactivate your environemnet simply type "deactivate"

```ps
(Base) C:\Users\*Username*\PythonWorkspace\Environment>deactivate
C:\Users\*Username*\PythonWorkspace\Environment>
```

Create a lab env following the same logic and activate it before next step

### 4. Install packages

!!!danger
    Nerver install package on your base python

* Install :

```ps
(lab) PS C:\Users\*Username*\PythonWorkspace> pip install #PACKAGENAME#
```

* Uninstall :

```ps
(lab) PS C:\Users\*Username*\PythonWorkspace> pip uninstall #PACKAGENAME#
```

* Downgrade :

```ps
(lab) PS C:\Users\*Username*\PythonWorkspace> pip install #PACKAGENAME#==2.1 --upgrade
```

* List of installed lib :

```ps
(lab) PS C:\Users\*Username*\PythonWorkspace> pip freeze
```

* File of installed lib :

```ps
(lab) PS C:\Users\*Username*\PythonWorkspace> pip freeze > python_lib_list.txt
```

#### Package Commonly used

This list is just a basic list, you will find much more information Library.

* Science Base : scipy, numpy, matplotlib
* Calcul symbolique : sympy
* Traducteur : Babel
* COM Win32 : pywin32
* Additional GUI App : PyQt5 ou Pyside2
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
* Standard IDE : VSC

## VSCode

### 1. Install VSCode

* Go to <https://code.visualstudio.com/download>
* Download Vscode
* Run the installer
* **ADD INFO HERE**
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
* Python Test Explorer (inc. Test Explorer UI)
* One Dark Pro
* vscode-icons
* Markdown All in One
* markdownlint
* Git Graph

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
