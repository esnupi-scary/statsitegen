from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT='text'
    BOLD='bold'
    ITALIC='italic'
    CODE='code'
    LINK='link'
    IMAGE='image'

class TextNode():
    def __init__(self, text:str, type: TextType, url:str | None=None):
        self.text=text
        self.type=type
        self.url=url

    def __eq__(self, tn: object) -> bool:
        if isinstance(tn, TextNode):
            if self.text == tn.text and self.type == tn.type and self.url == tn.url:
                return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"



def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text)
        case TextType.IMAGE:
            return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("Invalid TextType")
    
