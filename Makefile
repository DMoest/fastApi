#!/usr/bin/make -f

.PHONY: poetry-version poetry-config-list poetry-install poetry-install-all-extras \
	poetry-install-extras poetry-install-with poetry-install-no-root poetry-install-only-root \
	poetry-install-only poetry-install-without poetry-env-list poetry-env-remove-all \
	poetry-add-package poetry-remove-package env-list env-use poetry-add-package \
	poetry-remove-package poetry-install-sync poetry-lock poetry-lock-update \
	poetry-lock-no-update poetry-remove-lock-file poetry-show-latest-top-level


# --- POETRY COMMANDS ----------------------------------------------------------
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

poetry-add-requirements:  # Add the requirements file
	@read -p "Enter the requirements file path to add: " requirements_file; \
	poetry add cat(requirements.txt)

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

# poetry export plugin
# https://pypi.org/project/poetry-plugin-export/
poetry-export-to-requirements:  # Export the dependencies to the requirements file
	poetry export -f requirements.txt --output requirements.txt --without-hashes



# --- FastAPI Commands ---------------------------------------------------------
fastapi-uvicorn-run:  # Run the FastAPI app using Uvicorn
	uvicorn app.main:app --reload

fastapi-run-cli:  # Run the FastAPI app using the fastapi-cli
	fastapi run app.main:app --reload



# --- Alembic Commands ---------------------------------------------------------
alembic-init:  # Initialize the Alembic
	alembic init alembic

alembic-revision:  # Create a new revision
	@read -p "Enter the revision message: " message; \
	alembic revision --autogenerate -m "$$message"

alembic-upgrade:  # Upgrade to the head
	alembic upgrade head

alembic-downgrade:  # Downgrade to the previous version
	alembic downgrade -1

alembic-history:  # Show the alembic history
	alembic history

alembic-show-current:  # Show the current revision
	alembic current

alembic-show-head:  # Show the alembic heads
	alembic heads

alembic-show-branches:  # Show the alembic branches
	alembic branches



# --- Docker Commands ----------------------------------------------------------
docker-build:  # Build the Docker image
	docker build -t fastapi-app .

docker-run:  # Run the Docker container
	docker run -d --name fastapi-app -p 8000:8000 fastapi-app

docker-stop:  # Stop the Docker container
	docker stop fastapi-app

docker-remove:  # Remove the Docker container
	docker rm fastapi-app
