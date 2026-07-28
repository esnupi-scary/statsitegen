import unittest
from utils import split_nodes_delimiter
from textnode import TextNode, TextType

class TestUtils(unittest.TestCase):
    def test_malformed(self):
        node = TextNode("`This `is` text `with` a `code block` word", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        delimited = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(delimited, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)])
    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        delimited = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(delimited, [TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT)])
    def test_italic_delimiter(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        delimited = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(delimited, [TextNode("This is text with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT)])

