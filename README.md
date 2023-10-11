## Django Fullstack Ecommerce

<div align="center">
  <img src="https://static.djangoproject.com/img/logos/django-logo-positive.svg" alt="Django Logo">
</div>

### Project Structure

SOON

## Django Commands

1. Create a Requirements.txt

```
   py -m pip freeze > requirements.txt
```

2. Install modules from Requirements.txt

```
   pip install -r requirements.txt
```

3. Create a VirtualEnv in WINDOWS

```
   py -m venv virtual_env_name
```

4. Activate VirtualEnv in WINDOWS

```
   virtual_env_name\Scripts\activate.bat
```

5. Create a VirtualEnv in LINUX

```
 python3 -m venv virtual_env_name
```

6. Activate VirtualEnv in LINUX

```
source virtual_env_name/bin/activate
```

### VSCode Settings

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
