import pandas as pd
import os
import matplotlib.pyplot as plt

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
								parse_dates = True, usecols=["Date","Adj Close"],
								na_values = ["nan"])
		dfSYMBOL = dfSYMBOL.rename(columns={"Adj Close" : symbol})
		df = df.join(dfSYMBOL)
		df = df.dropna()

	return df

def plot_data(df, title="Stock Prices"):
	# Plot stock prices
	ax = df.plot(title=title, fontsize=2)
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	plt.show()

def plot_selected(df, columns, start_index, end_index):
	dfGRAPH = df.ix[start_index:end_index, columns]
	plot_data(dfGRAPH)

def normalize(df):
	return df/df.ix[0,:]


def test_run():
	start_date = "2017-01-03"
	end_date="2017-01-31"
	dates = pd.date_range(start_date, end_date)
	symbols = ["SPY","APPL", "IBM"]

	df = get_data(symbols,dates)
	df = normalize(df)

	plot_selected(df, symbols, start_date, end_date)	


if __name__ == '__main__':
	test_run()