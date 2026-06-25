from finance.analyzer import FinancialAnalyzer

analyzer = FinancialAnalyzer()

analysis = analyzer.analyze("AAPL")

print("\n========== ALPHAFORGE AI ==========\n")

for key, value in analysis.items():
    print(f"{key}: {value}")