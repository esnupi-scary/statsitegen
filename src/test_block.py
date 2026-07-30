import unittest
from block import block_to_block_type, BlockType, markdown_to_blocks

class TestBlock(unittest.TestCase):
    def test_block_to_block_type(self):
        block="""
> this
> is
> a 
> quote
"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_btbt_ordered_list(self):
        block="""
1. this is
2. an ordered
3. list of
4. items
"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_btbt_malformed_ordered_list(self):
        block="""
1. this is
3. an ordered
3. list of
4. items
"""
        self.assertNotEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_markdown_to_block(self):
            
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
    def test_markdown_to_block_collapse_newlines(self):
            
        md = """
This is **bolded** paragraph






    

    


    

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
        