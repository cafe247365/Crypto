import pyupbit

#티커 조회
tickers = pyupbit.get_tickers(fiat="KRW")
print(tickers)