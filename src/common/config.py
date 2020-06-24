class Config:

    def __init__(
        self, 
        keywords,
        reservedKeywords,
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
        self.reservedKeywords = reservedKeywords
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