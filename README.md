# POS System for Sharetea

## Introduction

This is a repository that contains both the frontend and backend required to run a POS system for the sale of drinks in a store such as Sharetea. 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Setup

1. **Clone the repository**

HTTPS:
```bash
git clone https://github.com/CSCE331-Fall2025-900-911/project-2-gang-90.git
cd project-2-gang-90
```

SSH:
```bash
git clone git@github.com:CSCE331-Fall2025-900-911/project-2-gang-90.git
cd project-2-gang-90
```

---

### Database setup (Python scripts)

This project works on Python 3.13.7 for database setup scripts. However, other versions of python should work.

It is reccomended to use [pyenv](https://github.com/pyenv/pyenv) to manage Python versions:

```bash
# Install pyenv if you don't have it
curl https://pyenv.run | bash

# MacOS
brew install pyenv

# Install the required Python version
pyenv install 3.13.7

# Set local Python version for the project
pyenv local 3.13.7
```

Alternatively, ensure your system Python version is 3.13.7:

```bash
python3 --version  # Should output Python 3.13.7
```

Set up a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install --upgrade pip
pip install -r requirements.txt
```

> **Note:** This Python environment is only needed for populating the database.

---

### Application setup (Java)

