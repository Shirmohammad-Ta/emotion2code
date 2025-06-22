import os
from jinja2 import Template

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")

def generate_code(emotion: str) -> str:
    template_file = os.path.join(TEMPLATE_DIR, f"{emotion}_template.py")
    if not os.path.exists(template_file):
        return "# No template available for this emotion."

    with open(template_file, "r") as file:
        template_text = file.read()

    # قالب Jinja را پر می‌کنیم (در آینده می‌تونیم دیتا هم بدیم)
    template = Template(template_text)
    code = template.render()
    return code
