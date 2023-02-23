"""Email role."""

import re
from typing import List, Tuple

from docutils import nodes
from docutils.nodes import Node, system_message
from sphinx.util import logging
from sphinx.util.docutils import SphinxRole

from .utils import Obfuscator

logger = logging.getLogger(f"sphinxcontrib-email.{__name__}")


class EmailRole(SphinxRole):
    """Role to obfuscate e-mail addresses.

    Handle addresses of the form "name@domain.org" and "Name Surname <name@domain.org>"
    """

    def run(self) -> Tuple[List[Node], List[system_message]]:
        """Setup the role in the builder context."""
        pattern = (
            r"^(?:(?P<name>.*?)\s*<)?(?P<email>\b[-.\w]+@[-.\w]+\.[a-z]{2,4}\b)>?$"
        )
        match = re.search(pattern, self.text)
        if not match:
            return [], []
        data = match.groupdict()

        obfuscated = Obfuscator().js_obfuscated_mailto(
            email=data["email"], displayname=data["name"]
        )
        node = nodes.raw("", obfuscated, format="html")
        return [node], []
