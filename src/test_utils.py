import unittest
from utils import split_nodes_delimiter, extract_markdown_links, extract_markdown_images
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



    # MARKDOWN EXTRACTOR TESTS

    def test_extract_markdown_links(self):
        matches_none = extract_markdown_links("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        matches = extract_markdown_links("This is text with a [link](https://i.imgur.com/zjjcJKZ.png)")
        matches_more = extract_markdown_links("This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [link again](https://i.imgur.com/zjjcJKZ.png)")

        self.assertEqual(matches, [("link", "https://i.imgur.com/zjjcJKZ.png")])
        self.assertEqual(matches_none, [])
        self.assertEqual(matches_more, [("link", "https://i.imgur.com/zjjcJKZ.png"), ("link again", "https://i.imgur.com/zjjcJKZ.png")])

    def test_extract_markdown_image(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        matches_none  = extract_markdown_images("This is text with a [link](https://i.imgur.com/zjjcJKZ.png)")
        matches_more = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image again](https://i.imgur.com/zjjcJKZ.png)")
        matches_second  = extract_markdown_images("This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and an ![image](https://i.imgur.com/zjjcJKZ.png)")

        self.assertEqual(matches, [("image", "https://i.imgur.com/zjjcJKZ.png")])
        self.assertEqual(matches_none, [])
        self.assertEqual(matches_more, [("image", "https://i.imgur.com/zjjcJKZ.png"), ("image again", "https://i.imgur.com/zjjcJKZ.png")])
        self.assertEqual(matches_second, [("image", "https://i.imgur.com/zjjcJKZ.png")])