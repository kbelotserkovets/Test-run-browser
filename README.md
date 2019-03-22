# Preparation

This is instruction for running test


## Installation

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Selenium.

```bash
pip install selenium
```

You may consider using [virtualenv](https://virtualenv.pypa.io/en/latest/) to create isolated Python environments. 
Python 3.6 has **pyvenv** which is almost the same as virtualenv.

- Selenium server is a Java program. Java Runtime Environment (JRE) 1.6 or newer version is recommended to run Selenium server. 

- Selenium requires a driver to interface with the chosen browser. Here we use 
[Crhrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and you should choose
version according what version of Chrome you're using

If Java Runtime Environment (JRE) is not installed in your system, you can download the [JRE from the Oracle website](https://www.oracle.com/technetwork/java/javase/downloads/index.html). If you are using a GNU/Linux system and have root access in your system, you can also use your operating system instructions to install JRE.


## Run via IDE

- Open ```try1.py``` file in any [JetBrains IDE](https://www.jetbrains.com/). In my case, I'm using [PyCharm](https://www.jetbrains.com/pycharm/?fromMenu)
- Run this file by clickng ```Shift + F10```


## Run via Terminal

- Launch Terminal from directory where you saved your ```try1.py``` file.
- Type ```python ./try1.py``` to run test

## Notes

Please, make sure that you set correct PATH to chrome driver in ```try1.py``` file on 4th line