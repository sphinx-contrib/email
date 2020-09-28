from __future__ import annotations

from typing import Any

import sphinx.util
from sphinx.application import Sphinx

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

logger = sphinx.util.logging.getLogger(__name__)


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_config_value(name="email_automode", default=False, rebuild="env")
    app.connect("html-page-context", html_page_context_handler)
    app.add_role("email", EmailRole())
    return {"version": ".".join(__version__.split(".")[:3])}
