# Python Logging

This repository was created to demonstrate an example setup for logging in python. 
The main focus of this example is to set up your logging in such a way that your 
application logs will also capture any logging done in modules that your application
imports and uses such as the `requests` library.

## The Root Logger
Logging in python is hierarchical and at the very top is the Root Logger. Every logger
created will inherit the properties of this logger, like the `handler` and `formatter` 
for example. To get the root logger, you need the following code:

```python
import logging
root_logger = logging.getLogger()
```

Setting the formatter and handler on this will cause every log-line in your application
(including third party modules) will follow the format and be handled by the handler. Most modules 
`DEBUG` log-lines only so that you won't see them unless your log-level is low enough. 

## Logging in your Application

At the top of every python file that logs messages you should have the following:  

```python
import logging
logger = logging.getLogger(__name__)
```

Now anytime you log something in that file with `logger.info`, `logger.error`, etc, it will work as 
expected and be logged as the root logger was configured. 

## This Example
This example sets up logging in a simple `setup_logging` function that configures the root logger
and returns nothing. An advantage of this setup is that none of your code gets run globally, 
which can make testing and debugging much cleaner. This example also uses a RotatingFileHandler
to demonstrate how to keep logs and conserve space. The `maxBytes` is set to `2MB`, which is a 
recommended size so that is small enough to email if need be.