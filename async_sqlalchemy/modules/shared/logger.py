import os

import logzero

log_level = os.getenv("LOG_LEVEL", "DEBUG")
logzero.loglevel(log_level)

logger = logzero.logger
