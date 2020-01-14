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

Git clone the repository under _DemoProject

```cmd
PS C:\Users\*USERNAME*\PythonWorkspace\Project> git clone https://gitlab.com/ymosteiro/demoproject.git _DemoProject
```

Change directory to _DemoProject

```cmd
PS C:\Users\*USERNAME*\PythonWorkspace\Project> cd _DemoProject
PS C:\Users\*USERNAME*\PythonWorkspace\Project\_DemoProject>
```

## Create virtual environment

Create a virtual environment

```cmd
PS C:\Users\*USERNAME*\PythonWorkspace\Project\_DemoProject> python -m venv .venv
```

Activate the environment

```cmd
PS C:\Users\*USERNAME*\PythonWorkspace\Project\_DemoProject> .venv\Scripts\activate
(.venv) PS C:\Users\*USERNAME*\PythonWorkspace\Project\_DemoProject>
```

Install requirements

```cmd
(.venv) PS C:\Users\*USERNAME*\PythonWorkspace\Project\_DemoProject> pip install -r requirements.txt
```

Setup your vs code settings

```json
{
    "python.pythonPath": ".venv\\Scripts\\python.exe",
    "python.formatting.provider": "black",
    "python.linting.pylintEnabled": true,
    "python.linting.enabled": true,
    "python.testing.pytestArgs": ["DemoProject\\tests"],
    "python.testing.unittestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.pytestEnabled": true
}
```

!!! todo
    Modify with Gitlab workflow.

Create a branch
(Try to use a feature name for YOUR_BRANCH)

```cmd
(.venv) PS C:\Users\*USERNAME*\PythonWorkspace\Project\_DemoProject> git checkout -b *YOUR_BRANCH*
```

Start developping on your branch and commit your changes.

Test your branch by intalling with pip in a seperate env.

```cmd
(test) PS C:\Users\*USERNAME*\PythonWorkspace\Project\_DemoProject> pip install -e .
```

When you are ready to Merge Request your feature,
Push the branch on gitlab

```cmd
(.venv) PS C:\Users\*USERNAME*\PythonWorkspace\Project\_DemoProject> git push origin *YOUR_BRANCH*
```

And create a Merge Request on **master** in GitLab
