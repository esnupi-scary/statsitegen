from textnode import TextNode, TextType
import re

def text_to_textnodes(text:str)-> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

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


# TODO: CONSOLIDATE THE LOGIC OF THESE TWO FUNCTIONS TO A SINGLE COMMON FUNCTION 

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    if len(old_nodes) < 1: 
        return []
    result = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) < 1:
            result.append(node)
            continue
        node_text = node.text
        for image in images: 
            node_text_split = node_text.split(f"![{image[0]}]({image[1]})", maxsplit=1)
            if len(node_text_split) > 0:
                if len(node_text_split[0]) > 0:
                    result.append(TextNode(node_text_split[0], TextType.TEXT))
                result.append(TextNode(image[0], TextType.IMAGE, image[1]))
                node_text = node_text_split[1]
        if len(node_text) > 0:
            result.append(TextNode(node_text, TextType.TEXT))
    return result

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    if len(old_nodes) < 1: 
            return []
    result = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) < 1:
            result.append(node)
            continue
        node_text = node.text
        for link in links: 
            node_text_split = node_text.split(f"[{link[0]}]({link[1]})", maxsplit=1)
            if len(node_text_split) > 0:
                if len(node_text_split[0]) > 0:
                    result.append(TextNode(node_text_split[0], TextType.TEXT))
                result.append(TextNode(link[0], TextType.LINK, link[1]))
                node_text = node_text_split[1]
        if len(node_text) > 0:
                result.append(TextNode(node_text, TextType.TEXT))
    return result

def extract_markdown_images(text:str):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text);

def extract_markdown_links(text:str):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text);


def markdown_to_blocks(markdown:str)->list[str]:
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        cleaned_block = block.strip()
        if cleaned_block != "":
            result.append(cleaned_block)
    return result