PYTHON ?= python3
.PHONY: test run docker
test:
	$(PYTHON) -m pytest -q
run:
	PYTHONPATH=src $(PYTHON) -m uvicorn inventory.main:app --reload --port 8080
docker:
	docker build -t cloud-resource-inventory-platform:local .
