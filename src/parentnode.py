from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag cannot be None type")
        if self.children == None or len(self.children) < 1:
            raise ValueError("ParentNode must have children")
        res_html = f"<{self.tag}>"
        for child in self.children: 
            res_html += child.to_html()
        res_html += f"</{self.tag}>"
        return res_html