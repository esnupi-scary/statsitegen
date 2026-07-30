import unittest

from converter import markdown_to_html_node

class TestConverter(unittest.TestCase):
    def test_paragraphs(self):
            md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

- this is a list 
- it can contain **bold text**
- and also _italic text_ 

1. this is an ordered list
2. this can also contain **bold** text
3. and also _italic_ text
    """
            node = markdown_to_html_node(md)
            html = node.to_html()
            print(html)
            self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p><ul><li>this is a list </li><li>it can contain <b>bold text</b></li><li>and also <i>italic text</i></li></ul><ol><li>this is an ordered list</li><li>this can also contain <b>bold</b> text</li><li>and also <i>italic</i> text</li></ol></div>",
            )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )