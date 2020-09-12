from sphinx.application import Sphinx

from .roles import EmailRole


def setup(app: Sphinx) -> None:
    app.add_role("email", EmailRole())
