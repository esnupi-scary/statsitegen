from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    if len(old_nodes) < 1: 
        return []
    result = []
    for node in old_nodes:
        if node.type != TextType.TEXT:
            result.append(node)
            continue
        chunks = node.text.split(delimiter)
        if len(chunks) % 2 == 0:
            raise ValueError("Malformed input text! Check for unescaped delimiters")
        for i in range(0, len(chunks)):
            if i % 2 == 0: # ZERO INDEXED, REMEMBER? even entries are text, odd are inside delimiter
                result.append(TextNode(chunks[i], TextType.TEXT))
            else:
                result.append(TextNode(chunks[i], text_type))
    return result


def extract_markdown_images(text:str):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text);

def extract_markdown_links(text:str):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text);
