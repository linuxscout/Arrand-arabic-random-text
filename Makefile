# Makefile for Arrand: Arabic Random Text Generator
.PHONY: all clean backup install install3 wheel wheel3 test docs publish publish_docs dev cli md2html

# Default target
default: all

# Build everything: wheel, docs, etc.
all: wheel docs

# Install in development mode
dev:
	pip install -e .[dev]

# Run tests
test:
	python3 -m unittest discover -s tests

# Build wheel
wheel:
	python3 -m build --wheel

# Upload to PyPI (manual safety guard)
upload:
	@echo "📦 Use: twine upload dist/*"

# Build docs using Sphinx
docs:
	cd docs && make html

# Publish docs to GitHub Pages
publish_docs:
	ghp-import -n -p -f docs/_build/html

# Convert README to HTML
md2html:
	pandoc -s -r markdown -w html README.md -o README.html

# Clean build artifacts
clean:
	rm -rf dist build *.egg-info \
		docs/_build __pycache__ .pytest_cache .mypy_cache \
		*.log .coverage htmlcov .tox

# CLI usage examples
cli:
	@echo "▶ Run CLI examples:"
	@echo "  python -m arrand"
	@echo "  python -m arrand --category aya"
	@echo "  python -m arrand -c poem -n 3"
	@echo "  python -m arrand -c phrase --vocalized"
	@echo "  python -m arrand -c nonsense -n 2"

# Push code to GitHub
publish:
	git push origin master
