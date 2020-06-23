from tokenizer import TokenType

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
    
    def is_active(self):
        """
        Returns True when inside an inline block.
        """
        return self.level > 0
    
    def is_inline_block(self, tokens, index):
        """
        Check if this should be an inline parentheses block.
        Examples are "NOW()", "COUNT(*)", "int(10)", key(`some_column`), DECIMAL(7,2)
        """
        length = 0
        level = 0

        for i in range(index, len(tokens)):
            token = tokens[i]
            length += len(token.value)

            if (length > INLINE_MAX_LENGTH):
                return False
            
            if (token.type == TokenType.OPEN_PAREN):
                level += 1
            elif token.type == TokenType.CLOSE_PAREN:
                level -= 1
                if level == 0:
                    return True
        
            if InlineBlock.is_forbidden_token(token):
                return False
        
        return False
    
    @staticmethod
    def is_forbidden_token(token):
        type, value = token.type, token.value
        return (
            type == TokenType.TOP_LEVEL_KEYWORD or
            type == TokenType.NEWLINE_KEYWORD or 
            type == TokenType.LINE_COMMENT or 
            type == TokenType.BLOCK_COMMENT or
            value == ';'
        )

