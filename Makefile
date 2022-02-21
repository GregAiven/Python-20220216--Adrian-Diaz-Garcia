default: help

.PHONY: help
help: ## Show help for all commands
	@echo
	@echo "Available commands:"
	@echo
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z0-9-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: build
build: ## Build docker images for monitor and etl
	@echo "Building etl and monitor..."
	docker-compose -f docker-compose.yml build

.PHONY: down
down: ## Stop services
	@echo "Stopping etl and monitor..."
	@docker-compose -f docker-compose.yml down

.PHONY: up
up: create-tables ## Start all services and provision db
	@echo "Starting etl and monitor..."
	@docker-compose -f docker-compose.yml up -d

.PHONY: create-tables
create-tables: ## Create tables from defined models
	@docker-compose -f docker-compose.yml run --rm etl ./etl/scripts/initdb.sh

.PHONY: black
black: ## Run black formatter
	@echo "Running black formatter"
	@docker-compose -f docker-compose.yml run --entrypoint= --rm etl black etl/
	@docker-compose -f docker-compose.yml run --entrypoint= --rm monitor black monitor/

.PHONY: isort
isort: ## Run isort formatter
	@echo "Running isort formatter"
	@docker-compose -f docker-compose.yml run --entrypoint= --rm etl isort etl/
	@docker-compose -f docker-compose.yml run --entrypoint= --rm monitor isort monitor/

.PHONY: formatters
formatters: black isort ## Run all formatters

.PHONY: flake8
flake8: ## Run flake8 linter
	@echo "Running flake8 linter"
	@docker-compose -f docker-compose.yml run --rm --entrypoint= etl flake8 --config=/app/etl/.flake8 etl/
	@docker-compose -f docker-compose.yml run --rm --entrypoint= monitor flake8 --config=/app/monitor/.flake8 monitor/

.PHONY: tests
test: ## Run tests
	@echo "Running tests"
	@docker-compose -f docker-compose.yml run -w /app --rm monitor python -m pytest monitor --cov=monitor
	@docker-compose -f docker-compose.yml run -w /app --rm etl python -m pytest etl --cov=etl