from __future__ import annotations

import re

from docutils import nodes
from docutils.nodes import Element, Node, system_message
from docutils.parsers.rst.states import Inliner
from sphinx.util.docutils import SphinxRole

from .utils import Obfuscator


class EmailRole(SphinxRole):
    def run(self) -> tuple[list[Node], list[system_message]]:
        """Role to obfuscate e-mail addresses.

        Handle addresses of the form
        "name@domain.org"
        "Name Surname <name@domain.org>"
        """
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
