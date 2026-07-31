from generator import generate_pages_recursive
from textnode import TextType, TextNode
from asset_mgmt import copy_contents

def main():
    text = TextNode("hello world", TextType.ITALIC)
    print(text)
    copy_contents("static","public")
    generate_pages_recursive("content", "template.html", "public")

main()