import random

from jinja2 import Template
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent / "templates" / "poetic_template.py"

def generate_poetry():
    # Load the poetry template
    template_text = TEMPLATE_PATH.read_text()
    template = Template(template_text)
    return template.render()

if __name__ == "__main__":
    print(generate_poetry())
