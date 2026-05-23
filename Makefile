.PHONY: setup lint test run

setup:
	python -m pip install -r requirements.txt

lint:
	python -m ruff check src tests dashboard
	python -m black --check src tests dashboard

test:
	python -m pytest tests/ -v

run:
	python -m streamlit run dashboard/app.py
