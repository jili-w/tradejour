book = {"AAPL": 190.2, "MSFT": 410.5}
book["TSLA"] = 190.3
print(book.get("NVDA", "not found"))
for ticker, px in book.items():
    print(f"{ticker:<6}{px:>8.2f}")

seen =(1,2,3)
seen.add(2)
print (seen,3 in seen)


