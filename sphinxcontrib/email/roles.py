"""Email role."""

import re
from typing import List, Tuple

from docutils import nodes
from docutils.nodes import Node
from sphinx.util import logging
from sphinx.util.docutils import SphinxRole

from .utils import Obfuscator

logger = logging.getLogger(f"sphinxcontrib-email.{__name__}")

PATTERN = r"^(?:(?P<name>.*?)\s*<)?(?P<email>\b[-.\w]+@[-.\w]+\.[a-z]{2,4}\b)>?$"
"email adress pattern"


class Email(SphinxRole):
    """Role to obfuscate e-mail addresses.

    Handle addresses of the form "name@domain.org" and "Name Surname <name@domain.org>"
    """

    def run(self) -> Tuple[List[Node], List[str]]:
        """Setup the role in the builder context."""
        match = re.search(PATTERN, self.text)
        if not match:
            return [], []
        data = match.groupdict()

        obfuscated = Obfuscator().js_obfuscated_mailto(
            email=data["email"], displayname=data["name"]
        )
        node = nodes.raw("", obfuscated, format="html")  # type: ignore
        return [node], []
