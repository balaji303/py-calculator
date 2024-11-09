# py-calculator
This is an example for Github Actions

[![Python Tests](https://github.com/balaji303/py-calculator/actions/workflows/python-test.yml/badge.svg)](https://github.com/balaji303/py-calculator/actions/workflows/python-test.yml)
[![codecov](https://codecov.io/gh/balaji303/py-calculator/graph/badge.svg?token=pS9BQUtSBP)](https://codecov.io/gh/balaji303/py-calculator)

## How to create requirements.txt file

1. Create requirements.in file and add the library
2. Run this command 'python -m piptools compile requirements.in'
3. requirements.txt file is created

## To Create HTML report in your local PC
1. pytest --html=report.html test_calculator.py


name: Python Tests

on: 
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests and generate HTML report
        run: |
          pytest --html=report.html test_calculator.py

      - name: Upload HTML report
        uses: actions/upload-artifact@v3
        with:
          name: test-report
          path: report.html
