from __future__ import annotations

from typing import Any

from sphinx.application import Sphinx
from sphinx.util import logging

from .handlers import html_page_context_handler
from .roles import EmailRole

try:
    from importlib import metadata
except ImportError:
    import importlib_metadata as metadata

try:
    __version__ = metadata.version("sphinxcontrib-email")
except metadata.PackageNotFoundError:
    pass

logger = logging.getLogger("sphinxcontrib-email")


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_config_value(name="email_automode", default=False, rebuild="env")
    app.connect(event="html-page-context", callback=html_page_context_handler)
    app.add_role(name="email", role=EmailRole())

    metadata = {
        "version": ".".join(__version__.split(".")[:3]),
        "parallel_read_safe": True,
    }
    return metadata
