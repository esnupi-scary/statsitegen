from enum import Enum
import re 

class BlockType(Enum):
    PARAGRAPH= "paragraph",
    HEADING= "heading"
    CODE= "code"
    QUOTE= "quote"
    UNORDERED_LIST= "unordered_list"
    ORDERED_LIST= "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    # check for code type
    code_type = block.split('```')
    if len(code_type) == 3:
        return BlockType.CODE
    # simple delimiters (unordered list, heading, quote block)
    # unordered list
    if len(re.findall(r"- .+", block)) > 0:
        return BlockType.UNORDERED_LIST
    # heading
    if len(re.findall(r"#{1,6} .+", block)) > 0:
        return BlockType.HEADING
    # quote
    if len(re.findall(r">.+", block)) > 0:
        return BlockType.QUOTE
    # complex delimiter - Ordered list (incrementing digit + . and space )
    # ordered list 
    ol_numbers = re.findall(r"(\d)\. .+", block)
    if len(ol_numbers) > 0:
        ol_cond = True
        for i in range(1, len(ol_numbers)):
            if int(ol_numbers[i]) - int(ol_numbers[i-1]) != 1:
                ol_cond = False
        if ol_cond:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
