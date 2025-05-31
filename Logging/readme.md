### LOGGING
Python has a built-in logging module that lets you write log messages to console, files, or external systems — and it's way more flexible and powerful than using print() statements.
Example:
```python
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("This is an error")
logging.critical("This is critical")
```
By default, only messages with level WARNING or higher are shown. To see more (like INFO or DEBUG), set level=logging.INFO or level=logging.DEBUG.<br>

Deafult level fo logging in python is set to WARNING. So, bydefault it will log everything that is above or equal to WARNING(i.e. WARNING, ERROR, and CRITICAL)

#### Log Levels in Python:
   Level	 Purpose
1. DEBUG	 Detailed diagnostic info(10)
2. INFO	     General info about app flow(20)
3. WARNING	 Something unexpected, non-fatal(30)
4. ERROR	 A serious problem occurred(40)
5. CRITICAL	 Very serious error, crash likely(50)

#### Why Logging:
1. Logging gives structured, level-based messages.

2. It makes it easier to debug, monitor, and maintain code — especially in larger or production systems.

3. You can log to files, consoles, remote services, or monitoring tools.

#### Setting Logging Level:

```python
logging.basicConfig(level=logging.DEBUG)
```

### Log Files
Instead of just printing logs to the console, you can log to a file using Python’s built-in logging module. This is useful for:
1. Debugging long-running scripts
2. Auditing application behavior
3. Storing historical logs for future analysis

example:
```python
import logging

# Configure logging to write to a file
logging.basicConfig(
    filename='app.log',           # File name
    level=logging.DEBUG,          # Minimum log level to capture
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING")
logging.error("This is an ERROR")
logging.critical("This is CRITICAL")
```

