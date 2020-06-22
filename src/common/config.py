class Config:

    def __init__(
        self, 
        keywords, 
        topLevelKeywords,
        newlineKeywords,
        topLevelKeywordsNoIndent,
        stringTypes,
        openParens,
        closeParens,
        lineCommentTypes,
        keyWordUppercase,
        linesBetweenQueries,
        specialWordChars,
        indent
    ):
        self.keywords = keywords
        self.topLevelKeywords = topLevelKeywords
        self.newlineKeywords = newlineKeywords
        self.topLevelKeywordsNoIndent = topLevelKeywordsNoIndent
        self.stringTypes = stringTypes
        self.openParens = openParens
        self.closeParens = closeParens
        self.lineCommentTypes = lineCommentTypes
        self.keyWordUppercase = keyWordUppercase
        self.linesBetweenQueries = linesBetweenQueries
        self.specialWordChars = specialWordChars
        self.indent = indent