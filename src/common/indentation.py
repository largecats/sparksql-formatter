INDENT_TYPE_TOP_LEVEL = 'top-level' # increased by open parentheses
INDENT_TYPE_BLOCK_LEVEL = 'block-level' # increased by TOPLEVEL_KEYWORD tokens

class Indentation:

    def __init__(self, indent):
        self.indent = indent or '   '
        self.indentTypes = []
    
    def get_indent(self):
        """
        Get indentation at current level. 
        """
        return self.indent * len(self.indentTypes)
    
    def increase_top_level(self):
        """
        Increases indentation by one top-level indent.
        """
        self.indentTypes.append(INDENT_TYPE_TOP_LEVEL)
    
    def incrase_block_level(self):
        """
        Increases indentation by one block-level indent.
        """
        self.indentTypes.append(INDENT_TYPE_BLOCK_LEVEL)
    
    def decrease_top_level(self):
        """
        Decreases indentation by one top-level indent.
        Does nothing if the previous indent is not top-level.
        """
        if (self.indentTypes[-1] == INDENT_TYPE_TOP_LEVEL):
            self.indentTypes.pop()
    
    def decrease_block_level(self):
        """
        Decreases indentation by one block-level indent.
        If there are top-level indents within the block-level indent, throws away these as well.
        """
        while len(self.indentTypes) > 0:
            type = self.indentTypes.pop()
            if (type != INDENT_TYPE_TOP_LEVEL):
                break

    def reset_indentation(self):
        self.indentTypes = []
