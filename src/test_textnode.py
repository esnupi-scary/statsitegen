import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("Testing inequality 1", TextType.ITALIC)
        node2 = TextNode("Testing inequality 2", TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_url(self):
        node = TextNode("Testing url", TextType.LINK, "https://google.com")
        self.assertEqual(node.url, "https://google.com")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()