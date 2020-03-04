# Starter Flask Application

### Requirements

- Python 3
- Virtualenv
- Virtualenvwrapper

### Running Locally

Step 1. Clone this repo

`$ git clone https://github.com/jqn/flask-boilerplate.git`

Step 2. Move into the project root directory

`$ cd flask_boilerplate`

Step 2. Create and activate a new virtual environment

`$ mkvirtualenv flask_boilerplate`

`$ workon flask_boilerplate`

Step 4. Set your environment variables

`$ vi ~/.virtualenvs/flask_boilerplate/bin/postactivate`

```bash
#!/bin/bash
# This hook is sourced after this virtualenv is activated.
export FLASK_ENV=development
export FLASK_CONFIG=development
export FLASK_APP=run.py
export FLASK_DEBUG=True
```

Step 5. Install the project dependencies

`$ pip install -r requirements.txt`

Step 6. Start the server

`$ flask run`
