import pandas as pd
import os

def get_max_close(symbol):
	df = pd.read_csv("{}.csv".format(symbol))
	return df["Close"].max() 

def get_mean_volume(symbol):
	df = pd.read_csv("{}.csv".format(symbol))
	return df["Volume"].mean()

def symbol_to_path(symbol, base_dir = "data"):
	return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
	df = pd.DataFrame(index = dates)

	if('SPY' not in symbols):
		symbols.insert(0,'SPY')

	for symbol in symbols:
		symbolPath = symbol_to_path(symbol)
		dfSYMBOL = pd.read_csv(symbolPath, index_col = "Date",
								parse_dates = True, usecols=["Date","Open"],
								na_values = ["nan"])
		dfSYMBOL = dfSYMBOL.rename(columns={"Open" : symbol})
		df = df.join(dfSYMBOL)
		df = df.dropna()

	return df


def test_run():
	start_date = "2017-01-03"
	end_date="2017-01-31"
	dates = pd.date_range(start_date, end_date)
	symbols = ["SPY","APPL", "IBM"]

	df = get_data(symbols,dates)

	print(df)

	


if __name__ == '__main__':
	test_run()