
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props 

    def to_html(self):
        raise NotImplementedError("this is for overloading only!")

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        res = ""
        for val in self.props:
            res+= " " + val + '="' + self.props[val] +"\""
        return res

    def __repr__(self)->str:
        return f"HtmlNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props_to_html()})"