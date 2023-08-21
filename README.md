# Custom Logger Wrapper

Custom Logger Wrapper is a Python package that provides a simple and convenient way to set up a custom logging configuration in your Python projects. It allows you to configure logging with a specific time zone and a pre-defined log format, making it easy to use across different modules in your project.
## Installation

Install this as a package to your project and import custom_logger - Please following below commands.

```
You can install Custom Logger Wrapper using `pip`. To install the package, run the following command:

```
pip3 install git+https://github.com/SPHTech-Data/mlops-custom-logger.git@main#egg=custom_logger

```
Add following is snippet when using within requirements.txt 

```
git+https://github.com/SPHTech-Data/mlops-custom-logger.git@main#egg=custom_logger

```
## Usage

After installing the package, you can use the custom logger in your Python modules like this:

```
Below is the example test.py  
## Example
```
from flask import Flask, request
import custom_logger  # Import the custom logger wrapper
import os
app = Flask(__name__)
# The logger is already set up with the desired configuration, default log-level is "DEBUG"
log_level = os.environ.get("LOG_LEVEL", "DEBUG")
logger = custom_logger.get_logger(__name__, log_level) # Set up custom logger

@app.route('/')
def home():
    logger.debug('Received request for home page')
    return "Welcome to the home page!"

@app.route('/demo')
def demo():
    logger.info('Received request for Flask Demo app')
    return "Flask Demo application is up and running!"

@app.route('/divide')
def divide_by_zero():
    try:
        result = 10 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError as e:
        logger.error(f'Error: {str(e)}')
        return "Error occurred: Division by zero"
    return "Division result: " + str(result)

@app.route('/bad_request')
def bad_request():
    logger.warning('Received a bad request')
    return "Bad request"

@app.route('/error')
def create_error():
    raise Exception("This is a custom exception")
    return "Should not be reached"

if __name__ == '__main__':
    logger.info("Starting Flask app...")
    app.run(host="0.0.0.0", port=80, debug=True)
```

This custom logger uses pytz package as dependency - This dependancy automatically added.

Here is the format

Git over SSH:
pip install git+ssh://git@github.com/SPHTech-Data/mlops-custom-logger.git@main#egg=custom_logger

Git over HTTPS:
pip install git+https://github.com/SPHTech-Data/mlops-custom-logger.git@main#egg=custom_logger

## Note: Custom_logger is in SGT datetime format

## Log level
"The default log level is set to 'Debug,' allowing it to display logs of all levels. 
To limit the display to only 'Error' logs, you can export the log level by using the command 'export log_level=error'."

## Brief description of custom logging format
format="%(levelname)s: %(asctime)s - %(module)s.%(funcName)s - %(message)s"


%(levelname)s: This placeholder is replaced with the log level name (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL) of the log message.

%(asctime)s: This placeholder is replaced with the current SGT timestamp when a log message is emitted.
 The s stands for "string," and the asctime represents the human-readable timestamp of the log message.

%(module)s: This placeholder is replaced with the name of the Python module where the log message was emitted.

%(funcName)s: This placeholder is replaced with the name of the Python function where the log message was emitted.

%(message)s: This placeholder is replaced with the actual log message content.