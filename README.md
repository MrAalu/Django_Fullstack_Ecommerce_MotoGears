## Django Fullstack Ecommerce

<div align="center">
  <img src="https://static.djangoproject.com/img/logos/django-logo-positive.svg" alt="Django Logo">
</div>

### Project Structure

SOON

## How to RUN Locally

**_Make Sure Python is installed on your Machine with PIP File Path Setuped_**

1. Clone the Project

```
   git clone https://github.com/MrAalu/Django_Fullstack_Ecommerce_MotoGears
```

2. Create Virtual Environment (Windows)
   **_If you're using Linux/Mac then you can lookup 'how to create python django virtual environment on linux/mac'_**

```
   py -m venv env
```

3. Activate Virtual Environment (WINDOWS)

```
   env\Scripts\activate
```

4. After Virtual Environment is Activated ,Install Required Packages

```
pip install -r requirements.txt
```

5. Models Migrations

```
py manage.py makemigrations
```

6. Models Migrate

```
py manage.py migrate
```

7. Populate Database with Products

```
py manage.py loaddata populateOne.json
```

```
py manage.py loaddata populateTwo.json
```

8. Run the Server

```
py manage.py runserver
```

### TestCase

1. TestCase : used when you want to test DB
2. SimpleTestCase : used when DB is not necessary
3. TransactionTestCase : directly test DB Transactions
4. LiveServerTestCase : launches liveserver thread useful for testing with Browser-based tools like selenium.

## Tech Stack

**Front-End :** Html, CSS, JavaScript(AXIOS is Used for API call), BootStrap

**Back-End :** Django, DjangoRestFramework(API Only), Sql

#### My VSCode Settings

```
{
  "editor.formatOnSave": true,
  "editor.fontSize": 20,
  "files.autoSave": "off",
  "editor.tabSize": 1,
  "editor.wordWrap": "on",
  "terminal.integrated.fontSize": 20,
  "emmet.includeLanguages": {
    "javascript": "javascriptreact",
    "html": "html"
  },
  "editor.cursorBlinking": "expand",
  "git.openRepositoryInParentFolders": "never",
  "workbench.iconTheme": "vscode-icons-mac",
  "security.workspace.trust.untrustedFiles": "open",
  "terminal.integrated.defaultProfile.windows": "Command Prompt",
  "terminal.integrated.cursorStyle": "line",

  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  },
  "[django-html]": {
    "editor.defaultFormatter": "junstyle.vscode-django-support"
  },
  "[html]": {
    "editor.defaultFormatter": "vscode.html-language-features"
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```
