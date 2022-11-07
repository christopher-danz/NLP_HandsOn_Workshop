# Setting up development environment
## Software needed
### 1. Install Python with Miniconda

How to install Miniconda: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)


Conda/Miniconda is used to create Python environments. Python environments are used to install only the required libraries with the correct version, and each project should have its own individual environment. 

New libraries can be installed with `pip install <LIBRARY_NAME>`. All installed libraries should be tracked and maintained in requirements.txt.

How to use conda: [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

### 2. (Recommended) Git 
How to install git: [https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

We recommend using git for code versioning and storing it online in repositories offered by Github or other websites.

How to use git: [Git Cheat Sheet](https://about.gitlab.com/images/press/git-cheat-sheet.pdf)



### 3. (Recommended) VsCode
How to install VsCode: [https://code.visualstudio.com/](https://code.visualstudio.com/)

VsCode is a free IDE and very suitable as a development environment for Python.

Useful VsCode Extensions:
 * Python
 * Jupyter
 * Pylance
 * Python Indent
 * Python Test Explorer
 * Prettier - Code formatter
 * autoDocstring
 * Markdown All in One

## How to install Python libraries

Create a python environment:
```console
conda create --name nlp_p39 python=3.9
activate nlp_p39
```

Install libraries in the currently enabled environment:
```console
cd <INSERT_PATH_TO_THIS_FOLDER>
pip install -r requirements.txt
```

Install required spaCy models:
```console
python -m spacy download en_core_web_sm
python -m spacy download de_core_news_sm
python -m spacy download de_core_news_lg
python -m spacy download de_dep_news_trf
```



# Usage
## Run Jupyter Notebook

```console
cd <INSTERT_PATH_TO_THIS_FOLDER> 
activate nlp_p39
jupyter notebook
```

# To get started you need to get the data which is stored in a folder on Google Drive

to do so, navigate to your destination folder and type:
```
wget "https://drive.google.com/drive/folders/1F_GRZfyeHKfxmcyrb1mc0uYp3HbwObjw"
```

# TO DO: Write manual to use notebooks
