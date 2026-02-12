.PHONY: lint clean dev format

lint:
	ruff check .
	mypy fasthttp


clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf .mypy_cache
	rm -rf .ruff_cache


dev:
	pip install -e .[dev]


format:
	ruff format .
