from __future__ import annotations

import html
import urllib.parse

import lxml.html  # nosec  # noqa DUO107
from sphinx.application import Sphinx

from .utils import Obfuscator


def html_page_context_handler(
    app: Sphinx, pagename: str, templatename: str, context: dict, doctree: bool
):
    """Search html for 'mailto' links and obfuscate them"""
    if not doctree:
        return

    tree = lxml.html.fragment_fromstring(context["body"])
    links = tree.iterlinks()
    links = filter(lambda link: link[2].startswith("mailto:"), list(links))

    for link in links:
        old_node = link[0]
        old_node_str = lxml.html.tostring(old_node, encoding="unicode", with_tail=False)
        tail_str = old_node.tail

        obfuscated = Obfuscator().js_obfuscated_text(old_node_str)
        new_node = lxml.html.fragment_fromstring(obfuscated)
        new_node.tail = tail_str

        old_node.getparent().replace(old_node, new_node)
    context["body"] = lxml.html.tostring(tree, encoding="unicode")
