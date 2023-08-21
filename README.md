## Custom Logger Wrapper

Custom Logger Wrapper is a Python package that provides a simple and convenient way to set up a custom logging configuration in your Python projects. It allows you to configure logging with a specific time zone and a pre-defined log format, making it easy to use across different modules in your project.

### Installation
    git+https://github.com/SPHTech-Data/mlops-custom-logger.git@main#egg=custom_logger
    
### Example
```
    * This custom logger uses pytz package as a dependency - This dependancy is automatically added.

    import custom_logger as logger
    if __name__ == '__main__':
        logger.get_logger('__shankar__').info("Hello World!")

```



### Note: 
    Custom_logger is in SGT datetime format

### Log level
    "The default log level is set to 'Debug,' which can be changed with 'export log_level=error'.

### Logging format description
    format="%(levelname)s: %(asctime)s - %(module)s.%(funcName)s - %(message)s"

    levelname: Log leven name (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
    asctime: Current SGT timestamp when a log message is emitted.
    module: Python module name where the log message was emitted.
    funcName: Python function where the log message was emitted.
    message: Actual log message content.
