from token_type import TokenType

INLINE_MAX_LENGTH = 120

class InlineBlock:

    """
    Inline blocks are parenthesized expressions that are shorter than INLINE_MAX_LENGTH.
    These blocks are formatted on a single line, unlike longer parenthesized expressions where open-parenthesis causes newline and increase of indentation.
    """

    def __init__(self):
        self.level = 0

    def begin_if_possible(self, tokens, index):
        """
        Begins inline block when lookahead through upcoming tokens determines that the block would be smaller than INLINE_MAX_LENGTH.

        Paramters
        tokens: list
            array of tokens
        index: int
            current token position
        """
        if self.level == 0 and self.is_inline_block(tokens, index):
            self.level = 1
        elif self.level > 0:
            self.level += 1
        else:
            self.level = 0
    
    def end(self):
        """
        Finishes current inline block. There might be several nested ones.
        """
        self.level -= 1