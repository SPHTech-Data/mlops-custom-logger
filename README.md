## Custom Logger Wrapper

Custom Logger Wrapper is a Python package that provides a simple and convenient way to set up a custom logging configuration in your Python projects. It allows you to configure logging with a specific time zone and a pre-defined log format, making it easy to use across different modules in your project.
### Installation
    git+https://github.com/SPHTech-Data/mlops-custom-logger.git@main#egg=custom_logger
### Example
```
    import custom_logger as logger
    if __name__ == '__main__':
        logger.get_logger('__shankar__').info("Hello World!")

```

This custom logger uses pytz package as dependency - This dependancy automatically added.

Here is the format

Git over SSH:
pip install git+ssh://git@github.com/SPHTech-Data/mlops-custom-logger.git@main#egg=custom_logger

Git over HTTPS:
pip install git+https://github.com/SPHTech-Data/mlops-custom-logger.git@main#egg=custom_logger

### Note: 
    Custom_logger is in SGT datetime format

### Log level
    "The default log level is set to 'Debug,' allowing it to display logs of all levels. 
    To limit the display to only 'Error' logs, you can export the log level by using the command 'export log_level=error'."

### Brief description of custom logging format
    format="%(levelname)s: %(asctime)s - %(module)s.%(funcName)s - %(message)s"


    %(levelname)s: This placeholder is replaced with the log level name (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL) of the log message.

    %(asctime)s: This placeholder is replaced with the current SGT timestamp when a log message is emitted.
    The s stands for "string," and the asctime represents the human-readable timestamp of the log message.

    %(module)s: This placeholder is replaced with the name of the Python module where the log message was emitted.

    %(funcName)s: This placeholder is replaced with the name of the Python function where the log message was emitted.

    %(message)s: This placeholder is replaced with the actual log message content.