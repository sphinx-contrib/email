"""Set of helpers to build the email role."""

import re
import textwrap
import xml.sax.saxutils
from xml.etree import ElementTree as ET

from sphinx.util import logging

logger = logging.getLogger(f"sphinxcontrib-email.{__name__}")


class Obfuscator:
    """Obfuscator for html output."""

    def __init__(self):
        """Obfuscator for html output."""
        self.rot_13_trans = str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
        )

    def rot_13_encrypt(self, line: str) -> str:
        """Rotate 13 encryption."""
        line = line.translate(self.rot_13_trans)
        line = re.sub("\n", r"\n", line)
        line = re.sub(r"@", r"\\100", line)
        line = re.sub(r"\.", r"\\056", line)
        line = re.sub(r"/", r"\\057", line)
        return line

    def xml_to_unesc_string(self, node: ET.Element) -> str:
        """Return unescaped xml string."""
        text = xml.sax.saxutils.unescape(
            ET.tostring(node, encoding="unicode", method="html"),
            {"&apos;": "'", "&quot;": '"'},
        )
        return text

    def js_obfuscated_text(self, text: str) -> str:
        """ROT 13 encryption embedded in Javascript code to decrypt in the browser."""
        xml_node = ET.Element("script")
        xml_node.attrib["type"] = "text/javascript"
        xml_node.attrib["class"] = "obfuscated-email"
        js_script = textwrap.dedent(
            """
            document.write(
              '{text}'.replace(
                /[a-zA-Z]/g,
                function (c) {{
                  return String.fromCharCode(
                    (c <= "Z" ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26
                  );
                }}
              )
            );
            """
        )
        xml_node.text = js_script.format(text=self.rot_13_encrypt(text))

        return self.xml_to_unesc_string(xml_node)

    def js_obfuscated_mailto(self, email: str, displayname: str = "") -> str:
        """ROT 13 encryption within an Anchor tag w/ a mailto: attribute."""
        xml_node = ET.Element("a")
        xml_node.attrib["class"] = "reference external"
        xml_node.attrib["href"] = f"mailto:{email}"
        xml_node.text = displayname or email

        return self.js_obfuscated_text(self.xml_to_unesc_string(xml_node))
