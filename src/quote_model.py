"""A QuoteModel is used to create quotes."""


class QuoteModel:
    """QuoteModel that consists of a body and author."""

    def __init__(self, body, author):
        """Initialize the QuoteModel."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a representation of QuoteModel."""
        return f"<{self.body}, {self.author}>"
