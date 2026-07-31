import os
import re

from converter import markdown_to_html_node

def extract_title(markdown:str):
    header = re.search(r"(?<!#)# (.+)", markdown)
    if header:
        return header.group(1) # 0 is the whole match, 1 is the first subgroup (.+) weirdly enough
    else:
        raise Exception("No title header found!")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not from_path:
        raise ValueError("from_path not provided!")
    if not template_path:
        raise ValueError("template_path not provided!")
    if not dest_path:
        raise ValueError("dest_path not provided!")

    markdown_content = ""
    html_content = ""

    with open(from_path) as f:
        markdown_content = f.read()
    
    with open(template_path) as f:
        html_content = f.read()

    node = markdown_to_html_node(markdown_content)
    body = node.to_html()
    title = extract_title(markdown_content)
    final_html = html_content.replace("{{ Content }}", body).replace("{{ Title }}", title).replace('src="/', f'src="{basepath}').replace('href="/', f'href="{basepath}')

    os.makedirs("/".join(dest_path.split("/")[:-1],), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    if not dir_path_content:
        raise ValueError("from_path not provided!")
    if not template_path:
        raise ValueError("template_path not provided!")
    if not dest_dir_path:
        raise ValueError("dest_path not provided!")

    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for content in os.listdir(dir_path_content):
        print(content)
        if os.path.isdir(f"{dir_path_content}/{content}"):
            generate_pages_recursive(f"{dir_path_content}/{content}", template_path, f"{dest_dir_path}/{content}", basepath)
        else:
            dest_dir_path_to_html = content.split(".md")[0]+".html"
            generate_page(f"{dir_path_content}/{content}", template_path, f"{dest_dir_path}/{dest_dir_path_to_html}", basepath)

    