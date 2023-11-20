## Django Fullstack Ecommerce

<div align="center">

<img src="https://static.djangoproject.com/img/logos/django-logo-positive.svg" alt="Django Logo">

</div>

### DEMO

![](https://i.ibb.co/FBtCP1j/Ecom-Django-MRAALu.gif)

### Project Structure

SOON

## How to RUN using DOCKER

1. Goto main folder where docker-compose.yml file is and run command (Building typically takes less than 60secs) :

```
docker-compose up
```

2. To Clear the Docker Cache(For Fresh Setup and Install)

```
docker system prune -a
```

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

5. Setup .ENV File  
   -Else this error will be given : decouple.UndefinedValueError: SOCIALACCOUNT_PROVIDERS_github_APP_client_id not found. Declare it as envvar or define a default value...or Something SIMILAR

```
Create a file with name .env and copy all the contents of '.env.example' to newly created '.env' file
```

6. Models Migrations

```

    py manage.py makemigrations

```

7. Models Migrate

```

    py manage.py migrate

```

8. Populate Database with Products

```

    py manage.py loaddata populateDatabase.json

```

9. Run the Server

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
