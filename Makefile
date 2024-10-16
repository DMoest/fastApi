#!/usr/bin/make -f

.PHONY: help poetry-version poetry-config-list poetry-install \
poetry-install-all-extras poetry-install-extras poetry-install-with \
poetry-install-no-root poetry-install-only-root poetry-install-only \
poetry-install-without poetry-install-sync poetry-lock poetry-lock-update \
poetry-lock-no-update poetry-update poetry-update-dry-run poetry-env-list \
poetry-env-info-path poetry-env-remove-all poetry-add-package \
poetry-remove-package poetry-pip-freeze poetry-pip-freeze-to-txt-file \
poetry-add-requirements-txt poetry-add-group poetry-remove-group \
poetry-remove-lock-file poetry-show-latest-top-level \
poetry-export-to-requirements uvicorn-run-app-on-port uvicorn-run \
alembic-init alembic-init-template alembic-revision \
alembic-revision-and-upgrade alembic-upgrade alembic-downgrade \
alembic-show-history alembic-show-current alembic-show-heads \
alembic-show-branches alembic-list-templates alembic-show-revision-details \
alembic-help docker-build docker-run docker-stop docker-remove



help:  # Show the available commands
	@echo "Available commands:"
	@echo "  poetry-version"
	@echo "  poetry-config-list"
	@echo "  poetry-install"
	@echo "  poetry-install-all-extras"
	@echo "  poetry-install-extras"
	@echo "  poetry-install-with"
	@echo "  poetry-install-no-root"
	@echo "  poetry-install-only-root"
	@echo "  poetry-install-only"
	@echo "  poetry-install-without"
	@echo "  poetry-install-sync"
	@echo "  poetry-lock"
	@echo "  poetry-lock-update"
	@echo "  poetry-lock-no-update"
	@echo "  poetry-update"
	@echo "  poetry-update-dry-run"
	@echo "  poetry-env-list"
	@echo "  poetry-env-info-path"
	@echo "  poetry-env-remove-all"
	@echo "  poetry-add-package"
	@echo "  poetry-remove-package"
	@echo "  poetry-pip-freeze"
	@echo "  poetry-pip-freeze-to-txt-file"
	@echo "  poetry-add-requirements-txt"
	@echo "  poetry-add-group"
	@echo "  poetry-remove-group"
	@echo "  poetry-remove-lock-file"
	@echo "  poetry-show-latest-top-level"
	@echo "  poetry-export-to-requirements"
	@echo "  uvicorn-run-app-on-port"
	@echo "  uvicorn-run"
	@echo "  alembic-init"
	@echo "  alembic-init-template"
	@echo "  alembic-revision"
	@echo "  alembic-revision-and-upgrade"
	@echo "  alembic-upgrade"
	@echo "  alembic-downgrade"
	@echo "  alembic-show-history"
	@echo "  alembic-show-current"
	@echo "  alembic-show-heads"
	@echo "  alembic-show-branches"
	@echo "  alembic-list-templates"
	@echo "  alembic-show-revision-details"
	@echo "  alembic-help"
	@echo "  docker-build"
	@echo "  docker-run"
	@echo "  docker-stop"
	@echo "  docker-remove"



# --- POETRY COMMANDS --------------------------------------------------------
poetry-version:  # Show poetry version
	poetry --version

poetry-config-list:  # List all the configuration settings
	poetry config --list

# poetry install commands
poetry-install:  # Install the dependencies
	poetry install

poetry-install-all-extras:  # Install all the extras dependencies
	poetry install --all-extras

poetry-install-extras:  # Install the extras dependency group
	@read -p "Enter the extras dependency group to install: " package_name; \
	poetry install --extras $$package_name

poetry-install-with:  # Install the package group with the dependencies
	@read -p "Enter the package group name to install with: " package_name; \
	poetry install --with $$package_name

poetry-install-no-root:  # Install the dependencies without the root package
	poetry install --no-root

poetry-install-only-root:  # Install only the root package
	poetry install --only-root

poetry-install-only:  # Install only the package
	@read -p "Enter the package name to install: " package_name; \
	poetry install --only $$package_name

poetry-install-without:  # Install the package without the dependencies
	@read -p "Enter the package name to install without: " package_name; \
	poetry install --without $$package_name

poetry-install-sync:  # Install the dependencies and sync the lock file
	poetry install --sync

# Poetry lock file commands
poetry-lock:  # Lock the dependencies
	poetry lock

poetry-lock-update:  # Update the lock file
	poetry lock --update

poetry-lock-no-update:  # Lock the dependencies without updating the lock file
	poetry lock --no-update

poetry-update:  # Update the dependencies
	poetry update

poetry-update-dry-run:  # Update the dependencies without installing
	poetry update --dry-run

# poetry environment management commands
poetry-env-list:  # List all the environments
	poetry env list

poetry-env-info-path:  # Show the path of the  virtual environment
	poetry env info --path

poetry-env-remove-all:  # Remove all the environments
	poetry env remove --all

# poetry package management commands
poetry-add-package:  # Add the package
	@read -p "Enter the package name to add: " package; \
	poetry add $$package

poetry-remove-package:  # Remove the package
	@read -p "Enter the package name to remove: " package; \
	poetry remove $$package

poetry-add-group:  # Add the group
	@read -p "Enter the group name to add: " group_name; \
	poetry add --group $$group_name

poetry-remove-group:  # Remove the group
	@read -p "Enter the group name to remove: " group_name; \
	poetry remove --group $$group_name

poetry-remove-lock-file:  # Remove the lock file
	rm -f poetry.lock

poetry-show-latest-top-level:  # Show the latest top-level package
	poetry show --latest --top-level

# poetry export plugin https://pypi.org/project/poetry-plugin-export/
poetry-export-to-requirements:  # Export the dependencies to a requirements file
	poetry export -f requirements.txt --output requirements.txt --without-hashes

poetry-pip-freeze:  # Show the pip freeze
	poetry run pip freeze

poetry-pip-freeze-to-txt-file:  # Show the pip freeze
	poetry run pip freeze > requirements.txt

poetry-add-requirements-txt:  # Add the requirements file
	@read -p "Enter the requirements file path to add: " requirements_file; \
	poetry add cat(requirements.txt)

pytest:  # Run the pytest
	poetry run pytest -v

pylint:  # Run the pylint on the src directory
	poetry run pylint src


# --- FastAPI UVICORN Commands -----------------------------------------------
uvicorn-run:  # Run the FastAPI app using Uvicorn
	poetry run uvicorn src.main:app --reload

uvicorn-run-app-on-port:  # Run the command in the virtual environment
	@read -p "Enter the PORT you like the application to run on: " port; \
	poetry run uvicorn app.main:app --reload --port $$port



# --- Alembic Commands -------------------------------------------------------
alembic-init:  # Initialize the Alembic
	@read -p "Enter the Alembic directory path: " directory_path; \
	poetry run alembic init "$$directory_path"

alembic-init-template:  # Initialize the Alembic with a template
	poetry run tree . -d
	@read -p "Enter the Alembic directory path: " directory_path; \
	poetry run alembic list_templates
	@read -p "Enter the alembic template name: " template_name; \
	poetry run alembic init "$$directory_path" --template $$template_name

alembic-revision:  # Create a new revision
	@read -p "Enter the revision message: " message; \
	poetry run alembic revision --autogenerate -m "$$message"

alembic-revision-and-upgrade:  # Create a new revision and upgrade
	@read -p "Enter the revision message: " message; \
	poetry run alembic revision --autogenerate -m "$$message"
	poetry run alembic upgrade head

alembic-upgrade:  # Upgrade to the head
	poetry run alembic upgrade head

alembic-downgrade:  # Downgrade to the previous version
	poetry run alembic downgrade -1

alembic-show-history:  # Show the alembic history
	poetry run alembic history

alembic-show-current:  # Show the current revision
	poetry run alembic current

alembic-show-heads:  # Show the alembic heads
	poetry run alembic heads

alembic-show-branches:  # Show the alembic branches
	poetry run alembic branches

alembic-list-templates:  # List the available templates
	poetry run alembic list_templates

alembic-show-revision-details:  # Show the Alembic configuration
	poetry run alembic history
	@read -p "Enter the revision id: " revision_id; \
	poetry run alembic show $$revision_id

alembic-help:  # Show the Alembic help
	poetry run alembic --help



# --- Docker Commands ----------------------------------------------------------
docker-build:  # Build the Docker image
	docker build -t fastapi-app .

docker-run:  # Run the Docker container
	docker run -d --name fastapi-app -p 8000:8000 fastapi-app

docker-stop:  # Stop the Docker container
	docker stop fastapi-app

docker-remove:  # Remove the Docker container
	docker rm fastapi-app
