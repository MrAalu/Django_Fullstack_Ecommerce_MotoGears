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
  "editor.fontSize": 20,

  "files.autoSave": "off",

  "editor.tabSize": 1,

  "editor.wordWrap": "on",

  "terminal.integrated.fontSize": 20,

  "emmet.includeLanguages": {
    "javascript": "javascriptreact"
  },

  "prettier.jsxSingleQuote": true,

  "prettier.semi": false,

  "prettier.singleQuote": true,

  "javascript.updateImportsOnFileMove.enabled": "always",

  "editor.formatOnPaste": true,

  "editor.formatOnSave": true,

  "editor.defaultFormatter": "esbenp.prettier-vscode",

  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  },
  "python.formatting.provider": "none",

  "editor.cursorBlinking": "expand",
  "git.openRepositoryInParentFolders": "never",
  "workbench.iconTheme": "vscode-icons-mac",
  "security.workspace.trust.untrustedFiles": "open",

  "redhat.telemetry.enabled": false,
  "workbench.startupEditor": "none",
  "terminal.integrated.defaultProfile.windows": "Command Prompt",
  "terminal.integrated.cursorStyle": "line",
  "liveServer.settings.donotShowInfoMsg": true,
  "[java]": {
    "editor.defaultFormatter": "mwpb.java-prettier-formatter"
  },
  "[html]": {
    "editor.defaultFormatter": "vscode.html-language-features"
  },
  "workbench.editorAssociations": {
    "*.sqlite3": "sqlite3-editor.editor"
  },
  "php.validate.executablePath": "C:/xampp/php/php.exe",
  "[php]": {
    "editor.defaultFormatter": "bmewburn.vscode-intelephense-client"
  },
  "[blade]": {
    "editor.defaultFormatter": "shufo.vscode-blade-formatter"
  }
}
```
