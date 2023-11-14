# RequirementsGen

## Overview
RequirementsGen is a Python utility designed to simplify the management of Python project dependencies. It automatically generates a clean and updated `requirements.txt` file by analyzing the installed packages in your Python environment.

## Features
- **Automatic Extraction**: Runs `pip freeze` to get a list of installed packages.
- **Filtering**: Filters out unnecessary details, keeping only the package names and versions.
- **Update Detection**: Compares the current environment with the existing `requirements.txt` file to identify and list new or updated packages.

## How to Use
1. Clone the repository.
2. Run `python requirements_gen.py` in your Python environment.
3. The script will create or update `requirements.txt` and `requirementsUpdate.txt` files in your project directory.

## Contributing
Contributions to improve RequirementsGen are always welcome. Feel free to fork the repository and submit your pull requests.
