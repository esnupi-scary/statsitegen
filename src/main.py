from generator import generate_pages_recursive
from textnode import TextType, TextNode
from asset_mgmt import copy_contents
import sys

def main():
    basepath = sys.argv[1] if sys.argv else "/"
    print(basepath)
    copy_contents("static","public")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()