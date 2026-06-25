import yfinance as yf


class MarketDataService:

    def get_company_info(self, ticker):

        stock = yf.Ticker(ticker)

        info = stock.info

        return {
            "company": info.get("longName"),
            "ticker": ticker.upper(),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "market_cap": info.get("marketCap"),
            "current_price": info.get("currentPrice"),
            "book_value": info.get("bookValue"),
            "trailing_pe": info.get("trailingPE")
        }