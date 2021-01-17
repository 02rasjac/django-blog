# Gymnasiearbete: How to create a blog with Python Django?
This is the repository for my gymnasiearbete on how to create a blog using the webframework *Django* for *Python*.

**Note:** This project is not finished yet.

## Technologies
* Python 3.9
* [Django](https://www.djangoproject.com/) 3.1

## Installation
First, create a *Virtual Environment*:
```powershell
python -m venv ./venv
```
Start the environment (windows):
```powershell
. .\venv\Scripts\Activate.ps1
```
In case of an **error** about the *executionpolicy*:
```powershell
Set-ExecutionPolicy RemoteSigned
```
Now you should be able to activate the venv.

Next, you have to [install Django](https://docs.djangoproject.com/en/3.1/intro/install/):
```powershell
python -m pip install Django
```

Lastly, you have to create a folder called *constants* in the root-folder and inside it create a file called *SECRET_KEY*. Go to https://djecrety.ir/ and generate a new SECRET_KEY and paste it on a single line in *constants/SECRET_KEY*.
An alternative to this is to create a *environment variable*, which might be a better choice.

## Full Report on my Work
[Original (Swedish)](https://docs.google.com/document/d/13Ra1vYrSRzTljm7wMcN3h5smfmmkv7ZIt2tWqVAphm8/edit?usp=sharing)
Translated (English) (Comming soon)

## Contact
**Name** - Rasmus Jacklin\
**Email** - rasmusjacklin2002@gmail.com