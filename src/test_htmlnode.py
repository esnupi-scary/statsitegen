import unittest
from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(None, None, None, {"href": "test", "rel":"test"})
        self.assertEqual(node.props_to_html(), ' href="test" rel="test"')

    def test_raise(self):
        node = HTMLNode(None, None, None, {"href": "test", "rel":"test"})
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_def(self):
        node = HTMLNode("testiiiing", None, None, {"href": "test", "rel":"test"})
        self.assertEqual(node.tag, "testiiiing")
        

if __name__ == "__main__":
    unittest.main()