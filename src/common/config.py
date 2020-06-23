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
        keywordUppercase,
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
        self.keywordUppercase = keywordUppercase
        self.linesBetweenQueries = linesBetweenQueries
        self.specialWordChars = specialWordChars
        self.indent = indent