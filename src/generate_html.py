import os

from block_markdown import markdown_to_html_node
from pathlib import Path


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    raise Exception("No title was specified in the markdown")


def generate_page(from_path, template_path, dest_path):
    print(f"GENERATING PAGE: {from_path} -> {dest_path} | USING TEMPLATE - {template_path}")

    from_file = open(from_path)
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path)
    template = template_file.read()
    template_file.close()

    html_node = markdown_to_html_node(markdown)
    content = html_node.to_html()

    title = extract_title(markdown)

    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", content)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    new_page = open(dest_path, "x")
    
    new_page.write(html)
    new_page.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(src_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(src_path, template_path, dest_path)
        else:
            generate_pages_recursive(src_path, template_path, dest_path)
