# Developement Process

## Clean your environement

Uninstall all package

```ps
pip freeze > requirements.txt
pip uninstall -r requirements.txt  -y
```

Or if you don't wan't to overide your requirements.txt

```ps
pip uninstall -y -r <(pip freeze)
```


## Clone Directory

Change directory where you want to clone the repository

```cmd
PS C:\Users\*USERNAME*\PythonWorkspace> cd Project
PS C:\Users\*USERNAME*\PythonWorkspace\Project>
```

Git clone the repository under _MeasureLib

```cmd
PS C:\Users\*USERNAME*\PythonWorkspace\Project> git clone https://github.com/yoannmos/MeasureLib.git _MeasureLib
```

Change directory to _MeasureLib

```cmd
PS C:\Users\*USERNAME*\PythonWorkspace\Project> cd _MeasureLib
PS C:\Users\*USERNAME*\PythonWorkspace\Project\_MeasureLib>
```

## Create virtual environment

Create a virtual environment

```cmd
PS C:\Users\*USERNAME*\PythonWorkspace\Project\_MeasureLib> python -m venv .venv
```

Activate the environment

```cmd
PS C:\Users\*USERNAME*\PythonWorkspace\Project\_MeasureLib> .venv\Scripts\activate
(.venv) PS C:\Users\*USERNAME*\PythonWorkspace\Project\_MeasureLib>
```

Install requirements

```cmd
(.venv) PS C:\Users\*USERNAME*\PythonWorkspace\Project\_MeasureLib> pip install -r requirements.txt
```

Setup your vs code settings

```json
{
    "python.pythonPath": ".venv\\Scripts\\python.exe",
    "python.formatting.provider": "black",
    "python.linting.pylintEnabled": true,
    "python.linting.enabled": true,
    "python.testing.pytestArgs": [
        "AlimEa\\tests",
        "Hbm\\tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.pytestEnabled": true
}
```

Create a branch
(Try to use a feature name for YOUR_BRANCH)

```cmd
(.venv) PS C:\Users\*USERNAME*\PythonWorkspace\Project\_MeasureLib> git checkout -b *YOUR_BRANCH*
```

Start developping on your branch and commit your changes.

Test your branch by intalling with pip in a seperate env.

```cmd
(test) PS C:\Users\*USERNAME*\PythonWorkspace\Project\_MeasureLib> pip install -e .
```

When you are ready to Pull Request your feature,
Push the branch on github

```cmd
(.venv) PS C:\Users\*USERNAME*\PythonWorkspace\Project\_MeasureLib> git push origin *YOUR_BRANCH*
```

And create a Pull Request on **master** in GitHub
