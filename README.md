# Custom Logger Wrapper

Custom Logger Wrapper is a Python package that provides a simple and convenient way to set up a custom logging configuration in your Python projects. It allows you to configure logging with a specific time zone and a pre-defined log format, making it easy to use across different modules in your project.

## Installation

You can install Custom Logger Wrapper using `pip`. To install the package, run the following command:

```
pip3 install git+https://github.com/SPHTech-Data/mlops-custom-logger.git@main#egg=custom_logger

```
Add following is snippet when using within requirements.txt 

```
git+https://github.com/SPHTech-Data/mlops-custom-logger.git@main#egg=custom_logger

```

This custom logger uses pytz package as dependency - This dependancy automatically added.

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
logger = custom_logger.setup_custom_logger("custom_logger")

def main():
    # Logging messages
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

if __name__ == "__main__":
    main()

## Example log output
2023-08-08 13:25:41 - DEBUG    - test.main - This is a debug message
2023-08-08 13:25:41 - INFO     - test.main - This is an info message
2023-08-08 13:25:41 - WARNING  - test.main - This is a warning message
2023-08-08 13:25:41 - ERROR    - test.main - This is an error message
2023-08-08 13:25:41 - CRITICAL - test.main - This is a critical message

## Log level
"The default log level is set to 'Debug,' allowing it to display logs of all levels. 
To limit the display to only 'Error' logs, you can export the log level by using the command 'export log_level=error'."

## Brief description of custom logging format
format="%(asctime)s - %(levelname)-8s - %(module)s.%(funcName)s - %(message)s"

%(asctime)s: This placeholder is replaced with the current SGT timestamp when a log message is emitted.
 The s stands for "string," and the asctime represents the human-readable timestamp of the log message.

%(levelname)s: This placeholder is replaced with the log level name (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL) of the log message.

%(module)s: This placeholder is replaced with the name of the Python module where the log message was emitted.

%(funcName)s: This placeholder is replaced with the name of the Python function where the log message was emitted.

%(message)s: This placeholder is replaced with the actual log message content.


