import re
import textwrap

from docutils import nodes

# The obfuscation code was adapted from
#
#   http://pypi.python.org/pypi/bud.nospam
#
# where was released by Kevin Teague <kevin at bud ca> under
# a BSD license.


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


def js_obfuscated_text(text):
    """ROT 13 encryption with embedded in Javascript code to decrypt in the browser."""
    snippet = textwrap.dedent(
        """\
        <script type="text/javascript">document.write(
            "{text}".replace(/[a-zA-Z]/g,
                function(c){{
                    return String.fromCharCode(
                        (c<="Z"?90:122)>=(c=c.charCodeAt(0)+13)?c:c-26
                    );
                }}
            )
        );</script>"""
    ).format(text=rot_13_encrypt(text))
    return snippet


def js_obfuscated_mailto(email, displayname=None):
    """ROT 13 encryption within an Anchor tag w/ a mailto: attribute"""
    snippet = """<a href="mailto:{email}">{displayname}</a>""".format(
        email=email, displayname=(displayname or email)
    )
    return js_obfuscated_text(snippet)


# -- end bud.nospam


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
