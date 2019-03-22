# Instruction for running test 


## Clone repository

Use this command
```commandline
git clone https://github.com/Ksen4ik/Test-run-browser.git
```



## Install Python

Here is the [link](https://www.python.org/downloads/source/) for install Python on Ubuntu

Here is the [link](https://www.python.org/downloads/windows/) for install Python on Windows

Here is the [link](https://www.python.org/downloads/mac-osx/) for install Python on MacOS


## Install pip

Use [pip](https://pip.pypa.io/en/latest/installing/) to run the following commands. Python 3.6 has pip available in the standard library. 


## Install required packages

For __Ubuntu__

- Open saved folder (Test-run-browser)
- Click right mouse button
- Click "Open in Terminal"
- Run the command:

```bash
pip install -r requirements.txt
```

For __Windows__

- Open Command line:   Start *menu* -> Run  and type *cmd*
- Type ```pip install -r``` and PATH to ```requirements.txt```

Mine looks like this:

```commandline
pip install -r D:\Downloads\Test-run-browser\requirements.txt)
```

For __MacOS__

- Open Command line:   *Finder -> Go menu -> Applications -> Terminal*
- Type:
```commandline
pip install -r requirements.txt
```




## Run via IDE

- Open ```try1.py``` file in any [JetBrains IDE](https://www.jetbrains.com/). In my case, I'm using [PyCharm](https://www.jetbrains.com/pycharm/?fromMenu)
- Run this file by clickng ```Shift + F10```


## Run via Terminal

For __Ubuntu__ / __MacOS__

- Run Terminal from directory where you saved your ```try1.py``` file.
- Type ```python3 ./try1.py``` to run test

For __Windows__

- Run Terminal from directory where you saved your ```try1.py``` file.
- Type: 
```commandline
C:\python27\python.exe D:\Downloads\Test-run-Browser\try1.py
```


#### Notes

- Please, make sure your Chrome browser's version is ```Version 73.0.3683.75 (Official Build) (64-bit)```





 