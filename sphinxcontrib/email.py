import re
import textwrap
import xml.dom.minidom  # nosec  # noqa DUO107
import xml.sax.saxutils  # nosec

from docutils import nodes

rot_13_trans = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
)


def rot_13_encrypt(line):
    """Rotate 13 encryption."""
    line = line.translate(rot_13_trans)
    line = re.sub(r"(?=[\"])", r"\\", line)
    line = re.sub("\n", r"\n", line)
    line = re.sub(r"@", r"\\100", line)
    line = re.sub(r"\.", r"\\056", line)
    line = re.sub(r"/", r"\\057", line)
    return line


def extended_unescape(text):
    """Return unescaped xml string"""
    return xml.sax.saxutils.unescape(text, {"&apos;": "'", "&quot;": '"'})


def js_obfuscated_text(text):
    """ROT 13 encryption with embedded in Javascript code to decrypt in the browser."""
    xml_doc = xml.dom.minidom.Document()
    xml_node = xml_doc.createElement("script")
    xml_node.attributes["type"] = "text/javascript"

    js_script = textwrap.dedent(
        """\
        document.write(
            "{text}".replace(/[a-zA-Z]/g,
                function(c){{
                    return String.fromCharCode(
                        (c<="Z"?90:122)>=(c=c.charCodeAt(0)+13)?c:c-26
                    );
                }}
            )
        );"""
    )
    xml_text_node = xml_doc.createTextNode(js_script.format(text=rot_13_encrypt(text)))
    xml_node.appendChild(xml_text_node)

    return extended_unescape(xml_node.toxml())


def js_obfuscated_mailto(email, displayname=None):
    """ROT 13 encryption within an Anchor tag w/ a mailto: attribute"""
    xml_doc = xml.dom.minidom.Document()
    xml_node = xml_doc.createElement("a")
    xml_node.attributes["href"] = f"mailto:{email}"

    xml_text_node = xml_doc.createTextNode(displayname or email)
    xml_node.appendChild(xml_text_node)

    return js_obfuscated_text(extended_unescape(xml_node.toxml()))


def email_role(
    typ, rawtext, text, lineno, inliner, options={}, content=[]  # noqa B006
):
    """Role to obfuscate e-mail addresses.

    Handle addresses of the form
    "name@domain.org"
    "Name Surname <name@domain.org>"
    """
    pattern = r"^(?:(?P<name>.*?)\s*<)?(?P<email>\b[-.\w]+@[-.\w]+\.[a-z]{2,4}\b)>?$"
    match = re.search(pattern, text)
    if not match:
        return [], []
    data = match.groupdict()

    obfuscated = js_obfuscated_mailto(email=data["email"], displayname=data["name"])
    node = nodes.raw("", obfuscated, format="html")
    return [node], []


def setup(app):
    app.add_role("email", email_role)
