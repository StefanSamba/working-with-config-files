# 3 ways of working with config files

[Medium Article](https://medium.com/@stefan-samba/3-ways-of-working-with-configuration-files-in-python-fb25d7ae7a3a)

## Usage

Create virtual env
`virtualenv venv`

Activate virtual env
`source venv/bin/activate`

Install packages
`pip3 install -r requirements.txt`

Commands to run for each option

Example of configuration in the python code (this is NOT recommended)

- `python3 1_in_py_file/main.py` or

### 1. Python dotenv .env

Example of configuration in a .env file

- `python3 2_in_dotenv/main.py` or

### 2. Box to read .yaml

Example of configuration in a .yaml file and reading via Box

- `python3 3_in_json_or_yaml/main_box.py` or

### 3. Hydra to read .yaml

Example of configuration in a .yaml file and reading via Hydra

- `python3 3_in_json_or_yaml/main_hydra.py`
