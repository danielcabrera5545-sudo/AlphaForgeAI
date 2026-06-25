from backend.services.market_data import MarketDataService

service = MarketDataService()

apple = service.get_company_info("AAPL")

print(apple)