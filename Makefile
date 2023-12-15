setup:
	poetry install
	poetry run pre-commit install

black:
	poetry run black .

bandit:
	poetry run bandit -c pyproject.toml -r hf_insights/

pre-commit:
	poetry run pre-commit run --all-files

deps: ## Install/Update dependencies
	poetry update
	poetry run pre-commit autoupdate

reqs:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

ui:
	poetry run streamlit run hf_insights/01_Home.py
