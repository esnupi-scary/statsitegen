import unittest
from block import block_to_block_type, BlockType

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