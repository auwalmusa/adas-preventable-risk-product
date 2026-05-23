.PHONY: setup lint test run

setup:
pip install -r requirements.txt

lint:
ruff check src tests
black --check src tests

test:
pytest tests/ -v
