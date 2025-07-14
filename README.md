# 🧬 PubMed Scraper

A Python CLI tool to fetch research papers from PubMed based on a search query, filtering results to only include those with at least one non-academic (pharmaceutical/biotech) author.

---

## 🚀 Features

- Fetches papers using the [PubMed E-utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- Filters authors affiliated with biotech/pharmaceutical companies
- Saves results as CSV or prints to console
- Supports full PubMed query syntax
- Easy CLI usage
- Installable as a Python package

---

## 🧪 Installation (from TestPyPI)

```bash
pip install --index-url https://test.pypi.org/simple/ pubmed-scraper