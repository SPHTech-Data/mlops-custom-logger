# Custom Logger Wrapper

Custom Logger Wrapper is a Python package that provides a simple and convenient way to set up a custom logging configuration in your Python projects. It allows you to configure logging with a specific time zone and a pre-defined log format, making it easy to use across different modules in your project.

## Installation

You can install Custom Logger Wrapper using `pip`. To install the package, run the following command:

```
pip3 install git+https://github.com/SPHTech-Data/mlops-custom-logger.git@main#egg=custom_logger

```
This package requires "pytz". Hence please add following in requirements.txt 

```
pytz
git+https://github.com/SPHTech-Data/mlops-custom-logger.git@main#egg=custom_logger

```
Here is the format

Git over SSH:
pip install git+git@github.com:username/repo.git@branch_or_commit#egg=package_name
Git over HTTPS:
pip install git+https://github.com/username/repo.git@branch_or_commit#egg=package_name

## Usage

After installing the package, you can use the custom logger in your Python modules like this:

## Note: Custom_logger is in SGT datetime format

```python
import custom_logger

# The logger is already set up with the desired configuration.
logger = custom_logger.logger

# Logging messages
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

## Example log output
2023-08-07 11:53:29 - custom_logger - ERROR    - test.main - This is a debug message
2023-08-07 11:53:29 - custom_logger - DEBUG    - test.main - This is a debug message
2023-08-07 11:53:29 - custom_logger - INFO     - test.main - This is an info message
2023-08-07 11:53:29 - custom_logger - WARNING  - test.main - This is a warning message

