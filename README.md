# discorddump

Scripts that parse the GDPR analytics dumps from Discord and dumps them into a Postgres database for querying.

## Setup
```sh
# Setup the virtual environment and source it
virtualenv env
source env/bin/activate

# Install the requirements and app into the environment.
pip install -r requirements.txt
python setup.py develop

# Use any favored method to set DB_URL to any Postgres server.
# Example DB_URL: postgres://john:hunter2@127.0.0.1/discorddump
```

# Scripts
* load.py - Parses and loads all the activity event JSON files into the database.
