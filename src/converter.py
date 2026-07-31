

import re

from block import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from utils import text_to_textnodes


def markdown_to_html_node(markdown:str) -> HTMLNode:
    # split markdown into blocks
    parent_children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_node = block_to_htmlnode(block, block_to_block_type(block))

        parent_children.append(block_node)
    main_parent = ParentNode("div", parent_children)
    return main_parent

def block_to_htmlnode(block: str ,type: BlockType) -> HTMLNode:
    match type:
        case BlockType.PARAGRAPH:
           return simple_block_to_html_node(block, "p")
        case BlockType.HEADING:
            header_text, header_type = text_to_heading_tag(block)
            return simple_block_to_html_node(header_text, header_type)
        case BlockType.CODE:
            # created a TextNode manually to do all this
            # trim the code blocks backticks from the block before processing
            sanitized_block = block.replace("```\n","").replace("```","")
            return ParentNode("pre", [text_node_to_html_node(TextNode(sanitized_block, TextType.CODE))])
        case BlockType.QUOTE:
            sanitized_block = sanitize_quotes(block)
            return simple_block_to_html_node(sanitized_block, "blockquote")
        # every new line will have to be wrapped in a <li> tag
        # this might need a separate function
        case BlockType.UNORDERED_LIST:
            return list_block_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return list_block_to_html_node(block, is_ordered=True)
        case _:
            raise Exception("Encountered unknown BlockType!")


def simple_block_to_html_node(block: str, parent_tag: str) -> ParentNode:
    replaced_str = block.replace("\n", " ")
    p_node = ParentNode(parent_tag, text_to_children(replaced_str))
    return p_node     

def list_block_to_html_node(block: str, is_ordered:bool=False):
    children = []
    regex = r"- (.+)"
    if is_ordered:
        regex = r"\d\. (.+)"
    for item in re.findall(regex, block):
        prepared_item = text_to_children(item)
        # must be encapsulated in a list item tag - <li>
        children.append(ParentNode("li", prepared_item))
    p_node = ParentNode("ol" if is_ordered else "ul", children)
    return p_node

def text_to_heading_tag(block:str)->tuple[str, str]:
    count_hash = 0
    end_hash = 0
    for i in range(len(block)):
        if block[i] == "#":
            count_hash += 1
        else:
            end_hash = i
            break
    if count_hash >= 1 and count_hash <= 6:
        return block[end_hash:].strip(), f"h{count_hash}"
    else:
        # this should probably just downgrade the header to a regular paragraph tag, but keeping here for testing
        # raise ValueError("improper header!! ")
        return block, "p"

def sanitize_quotes(block:str)->str:
    lines = block.split("\n")
    res_block = ""
    for line in lines:
        res_line = line[1:].strip()
        res_block += res_line + "\n"
    return res_block


def text_to_children(text:str):
    text_nodes = text_to_textnodes(text)
    children = list(map(lambda node: text_node_to_html_node(node), text_nodes))
    return children