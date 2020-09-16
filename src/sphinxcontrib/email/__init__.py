from sphinx.application import Sphinx

from .handlers import html_page_context_handler
from .roles import EmailRole


def setup(app: Sphinx) -> None:
    app.add_config_value(name="email_automode", default=False, rebuild="env")
    if app.config["email_automode"]:
        app.connect("html-page-context", html_page_context_handler)
    app.add_role("email", EmailRole())
