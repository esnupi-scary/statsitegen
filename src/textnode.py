from enum import Enum

class TextType(Enum):
    PLAIN='plain'
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
