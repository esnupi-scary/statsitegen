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
    delims = {"- ":BlockType.UNORDERED_LIST, ">": BlockType.QUOTE }
    for delimiter in delims: 
        if block.startswith(delimiter):
            for line in block.split("\n"):
                if not line.startswith(delimiter):
                    return BlockType.PARAGRAPH
            return delims[delimiter]
    #. REPLACED BECAUSE OF A BUG WITH REGEX. OF COURSE IT'S A BUG WITH REGEX, WHAT ELSE COULD IT HAVE BEEN 
    # if len(re.findall(r"- .+", block)) > 0:
    #     return BlockType.UNORDERED_LIST
    # quote
    # if len(re.findall(r">.*", block)) > 0:
    #     print("Got here")
    #     return BlockType.QUOTE
    # heading
    if len(re.findall(r"#{1,6} .+", block)) > 0:
        return BlockType.HEADING
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


def markdown_to_blocks(markdown:str)->list[str]:
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        cleaned_block = block.strip()
        if cleaned_block != "":
            result.append(cleaned_block)
    return result
