from typing import Dict

import lxml.html  # nosec  # noqa DUO107
from sphinx.application import Sphinx
from sphinx.util import logging

from .utils import Obfuscator

logger = logging.getLogger(f"sphinxcontrib-email.{__name__}")


def html_page_context_handler(
    app: Sphinx, pagename: str, templatename: str, context: Dict, doctree: bool
):
    """Search html for 'mailto' links and obfuscate them"""
    if not app.config["email_automode"]:
        return
    if not doctree:
        return

    tree = lxml.html.fragment_fromstring(context["body"], create_parent="body")
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

    child_strs = [
        lxml.html.tostring(child, pretty_print=True, encoding="unicode")
        for child in tree.iterchildren()
    ]
    context["body"] = "".join(child_strs)
