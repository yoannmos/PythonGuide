<!-- This guide wont enumerate fonction, but will try to adress theme of fonctionnality instead. -->
# Dealing with Path, Directory and Files

Majors tools, *"Python included"*, to deal with path are `pathlib` and `os` module.

| Module  | Documentation                                                                                                                     |
| :------ | :-------------------------------------------------------------------------------------------------------------------------------- |
| pathlib | [pathlib documentation](https://docs.python.org/3.7/library/pathlib.html) -  [PEP 428](https://www.python.org/dev/peps/pep-0428/) |
| os      | [os.path documentation](https://docs.python.org/3.7/library/os.path.html)                                                         |  |

=== "pathlib"

    ```python
    >>> from pathlib import Path

    # Relative Path
    >>> Path('my/relative/path')
    WindowsPath('my/relative/path')

    # Absolute Path
    >>> Path.cwd() / Path('my/absolute/path')
    WindowsPath('C:/Users/*Username*/PythonWorkspace/Project/_PythonGuide/my/absolute/path')

    # Use of Path
    >>> p = Path('C:/Users/*Username*/_PythonGuide/LICENCE.txt')

    >>> p.parts
    ('C:\\', 'Users', '*Username*', '_PythonGuide', 'LICENCE.txt')

    >>> p.anchor
    'C:\\'

    >>> p.parent
    WindowsPath('C:/Users/*Username*/_PythonGuide')

    >>> p.name
    'LICENCE.txt'

    >>> p.stem
    'LICENCE'

    >>> p.suffix
    '.txt'

    >>> p.drive
    'C:'

    ```

=== "os"
<!--  -->
    ```python
    >>>import os

    # Relative Path
    >>> os.path.relpath('my/relative/path')
    'my\\relative\\path'

    # Absolute Path
    >>> os.path.abspath('my/absolute/path')
    'C:\\Users\\*Username*\\PythonWorkspace\\Project\\_PythonGuide\\my\\absolute\\path'

    # Use of os.path
    >>> p = 'C:\\Users\\*Username*\\_PythonGuide\\LICENCE.txt'

    >>> os.path.dirname(p)
    'C:\\Users\\*Username*\\_PythonGuide'

    >>> os.path.basename(p)
    'LICENCE.txt'

    >>> os.path.split(p)
    ('C:\\Users\\*Username*\\_PythonGuide', 'LICENCE.txt')
    ```

To get the current working directory

=== "pathlib"

    ```python
    >>> Path.cwd()
    WindowsPath('C:/Users/*Username*/PythonWorkspace/Project/_PythonGuide')
    ```

=== "os"

    ```python
    >>> os.getcwd()
    'C:\\Users\\*Username*\\PythonWorkspace\\Project\\_PythonGuide'
    ```

Or get the parent directory

=== "pathlib"

    ```python
    >>> p = Path.cwd()

    >>> p
    WindowsPath('C:/Users/*Username*/PythonWorkspace/Project/_PythonGuide')

    >>> list(p.parents)
    [WindowsPath('C:/Users/*Username*/_PythonGuide'), WindowsPath('C:/Users/*Username*'), WindowsPath('C:/Users'), WindowsPath('C:/')]

    >>> Path.cwd().parents[0]
    WindowsPath('C:/Users/*Username*/PythonWorkspace/Project')

    >>> Path.cwd().parents[1]
    WindowsPath('C:/Users/*Username*/PythonWorkspace')

    >>> Path.cwd().parents[2]
    WindowsPath('C:/Users/*Username*')

    >>> Path.cwd().parents[3]
    WindowsPath('C:/Users')

    >>> Path.cwd().parents[4]
    WindowsPath('C:/')
    ```

=== "os"

    ```python
    >>> os.path.abspath('.')
    'C:\\Users\\*Username*\\PythonWorkspace\\Project\\_PythonGuide'

    >>> os.path.abspath('..')
    'C:\\Users\\*Username*\\PythonWorkspace\\Project'

    >>> os.path.abspath('..\..')
    'C:\\Users\\*Username*\\PythonWorkspace'

    >>> os.path.abspath('..\..\..')
    'C:\\Users\\*Username*'

    >>> os.path.abspath('..\..\..\..')
    'C:\\Users'

    >>> os.path.abspath('..\..\..\..\..')
    'C:\\'
    ```

To change your working directory

```python
os.chdir('A:/New/Path')
```

To get the full path to the directory where your Python file is contained in:

```python
# __file__ is a constant, representing the .py file executed
file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(os.path.realpath(__file__))
```

To concatenate path

```python
>>> Path.cwd() / Path('my/absolute/path')
WindowsPath('C:/Users/*Username*/AppData/Local/Programs/Python/Python37/my/absolute/path')

# or

os.join(os.getcwd(), 'my/relative/path')
```

(Note that the incantation above won't work if you've already used os.chdir() to change your current working directory, since the value of the __file__ constant is relative to the current working directory and is not changed by an os.chdir() call.)

```python
>>> Path.home()
WindowsPath('C:/Users/*Username*')
```

```python
Path(r'C:\Users\*Username*\spam').mkdir() # Create the spam folder
os.makedirs().
```
