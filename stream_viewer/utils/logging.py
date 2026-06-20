import logging
import os
import sys
from pathlib import Path


LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s: %(message)s"


def configure_logging(app_name: str = "stream_viewer", level: str | None = None) -> Path:
    log_level_name = (level or os.environ.get("STREAM_VIEWER_LOG_LEVEL", "INFO")).upper()
    log_level = getattr(logging, log_level_name, logging.INFO)

    log_dir = Path.home() / ".stream_viewer" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{app_name}.log"

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    formatter = logging.Formatter(LOG_FORMAT)

    has_stream_handler = any(
        isinstance(handler, logging.StreamHandler) and not isinstance(handler, logging.FileHandler)
        for handler in root_logger.handlers
    )
    if not has_stream_handler:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(formatter)
        root_logger.addHandler(stream_handler)

    file_handler = next(
        (
            handler for handler in root_logger.handlers
            if isinstance(handler, logging.FileHandler) and Path(handler.baseFilename) == log_path
        ),
        None,
    )
    if file_handler is None:
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

    logging.captureWarnings(True)
    root_logger.debug("Logging configured for %s at %s -> %s", app_name, log_level_name, log_path)
    return log_path


def install_excepthook(logger_name: str):
    logger = logging.getLogger(logger_name)
    previous_hook = sys.excepthook

    def _excepthook(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            previous_hook(exc_type, exc_value, exc_traceback)
            return
        logger.exception("Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback))
        previous_hook(exc_type, exc_value, exc_traceback)

    sys.excepthook = _excepthook
