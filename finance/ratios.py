def price_to_book(price_per_share, book_value_per_share):
    """
    Calculate the Price-to-Book (P/B) Ratio.
    """

    if book_value_per_share == 0:
        return None

    return round(price_per_share / book_value_per_share, 2)