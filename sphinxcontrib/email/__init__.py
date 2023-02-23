"""Provide an email obfuscator for Sphinx-based documentation."""

from typing import Any, Dict

from importlib_metadata import version
from sphinx.application import Sphinx
from sphinx.util import logging

from .handlers import html_page_context_handler
from .roles import Email

__version__ = version("sphinxcontrib-email")

logger = logging.getLogger("sphinxcontrib-email")


def setup(app: Sphinx) -> Dict[str, Any]:
    """Setup email role parameters."""
    app.add_config_value(name="email_automode", default=False, rebuild="env")
    app.connect(event="html-page-context", callback=html_page_context_handler)
    app.add_role(name="email", role=Email())

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
