# PubMed Scraper

A command-line tool to fetch research papers from PubMed based on a user-specified query. The tool identifies papers with at least one author affiliated with a pharmaceutical or biotech company and outputs the results as a CSV.

## Features

- Fetches papers using the [PubMed E-utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- Filters authors affiliated with biotech/pharmaceutical companies
- Saves results as CSV or prints to console
- Supports full PubMed query syntax
- Easy CLI usage
- Installable as a Python package

---

## Installation (from TestPyPI)

```bash
pip install --index-url https://test.pypi.org/simple/ pubmed-scraper
```

---

### From Source

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rashijain2709/pubmed_scraper.git
   cd pubmed_scraper
   ```

## Tools Used

| Tool         | Purpose                                      |
|--------------|----------------------------------------------|
| [Poetry]     | Dependency management and packaging          |
| [Requests]   | Making HTTP requests to the PubMed API       |
| [argparse]   | CLI argument parsing                         |
| [Python Typing] | Type hints and type safety                |
| [pytest]     | Unit testing                                 |

---

## Project Structure

```
pubmed_scraper/
│
├── cli/                     # Command-line interface logic
│   └── main.py
│
├── pubmed_scraper/          # Core module for fetching and processing PubMed data
│   ├── __init__.py
│   ├── api.py
│   ├── parser.py
│   └── writer.py
│
├── tests/                   # Unit tests
│   └── test_parser.py
│
├── pyproject.toml           # Poetry configuration
├── README.md                # Project documentation
└── LICENSE                  # MIT License
```

---

# Poetry Project Execution Guide

This guide helps you set up, test, and publish your PubMed scraper project using **Poetry** and **TestPyPI**.

---

## 1. Initial Setup

Install required dependencies and dev tools:

```bash
poetry add requests

poetry add pytest --dev

poetry install
```

---

## 2. Check and Lock Dependencies

```bash
poetry check

poetry lock
```

---

## 3. Run Tests

```bash
poetry run pytest
```

---

## 4. Configure TestPyPI

```bash
poetry config repositories.test-pypi https://test.pypi.org/legacy/

# Verify the configuration (Windows)
poetry config --list | findstr pypi

# On macOS/Linux
poetry config --list | grep pypi
```

---

## 5. Build the Package

```bash
# Optional: Clean previous builds
rm -r dist/*   # Use 'rmdir /S /Q dist' on Windows

# Build the package
poetry build
```

---

## 6. Publish to TestPyPI

```bash
# Publish the package to TestPyPI
poetry publish --build -r test-pypi
```

---

## 7. Run Your Program

```bash
# Run the scraper with a query and output file
poetry run get-papers-list "cancer immunotherapy" --file papers.csv --debug

# Another example
poetry run get-papers-list "cancer therapy" --file results.csv --debug
```

---

## Optional: Clean and Rebuild Everything

```bash
rm -r dist/*
poetry build
poetry publish --build -r test-pypi
```

---