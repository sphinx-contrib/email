"""Test sphinxcontrib.video extension."""

from pathlib import Path

import pytest
from bs4 import BeautifulSoup, formatter

fmt = formatter.HTMLFormatter(indent=2, void_element_close_prefix=" /")


@pytest.mark.sphinx(testroot="email")
def test_email(app, status, warning, file_regression):
    """Build a video without options."""
    app.builder.build_all()

    raw_html = (app.outdir / "simple_email.html").read_text(encoding="utf8")
    html = BeautifulSoup(raw_html, "html.parser")
    script = html.select("script.obfuscated-email")[0].prettify(formatter=fmt)
    Path("test.txt").write_text(script)
    file_regression.check(script, basename="email", extension=".html")


@pytest.mark.sphinx(testroot="email")
def test_named_email(app, status, warning, file_regression):
    """Build a video without options."""
    app.builder.build_all()

    raw_html = (app.outdir / "named_email.html").read_text(encoding="utf8")
    html = BeautifulSoup(raw_html, "html.parser")
    script = html.select("script.obfuscated-email")[0].prettify(formatter=fmt)
    file_regression.check(script, basename="named-email", extension=".html")
