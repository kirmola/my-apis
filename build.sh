
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -;
export PATH="/vercel/.local/bin:$PATH";

# Install poetry packages
poetry install;
poetry self add poetry-plugin-export;
poetry export --without-hashes --with dev > requirements.txt;


# Install from requirements.txt
pip3 install -r requirements.txt

# # Generate CSS
# poetry run python3 manage.py collectstatic --noinput --settings=api.settings.prod;

# # Generate Static files
# poetry run python3 manage.py collectstatic --noinput;