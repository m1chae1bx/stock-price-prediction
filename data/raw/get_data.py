import requests


def get_batch_stock_data_from_marketwatch(stock_code: str, start_year: int, end_year: int):
    stock_code = stock_code.lower()

    with open(f"{stock_code.upper()}_{start_year}_{end_year}.csv", "wb") as f:
        for i, year in enumerate(range(start_year, end_year + 1), 1):
            url = f"https://www.marketwatch.com/investing/stock/{stock_code}/downloaddatapartial?startdate=01/01/{year}%2000:00:00&enddate=12/31/{year}%2000:00:00&daterange=d30&frequency=p1d&csvdownload=true&downloadpartial=false&newdates=false&countrycode=ph"
            response = requests.get(url)
            content = response.content
            if i != 1:
                # remove the header
                data = content.splitlines()[1:]
                # reverse content because the data is in descending order
                data = data[::-1]
                content = b"\n".join(data) + b"\n" if data else None
            else:
                lines = content.splitlines()
                header = lines[0]
                data = lines[1:]
                # reverse content because the data is in descending order
                data = data[::-1]
                content = b"\n".join([header, *data]) + b"\n"
            if content:
                f.write(content)


# get_batch_stock_data_from_marketwatch("AC", 1995, 2022)
# get_batch_stock_data_from_marketwatch("JFC", 1995, 2022)
# get_batch_stock_data_from_marketwatch("BDO", 1995, 2022)
# get_batch_stock_data_from_marketwatch("BPI", 1995, 2022)
# get_batch_stock_data_from_marketwatch("SMC", 1995, 2022)
# get_batch_stock_data_from_marketwatch("SM", 1995, 2022)
# get_batch_stock_data_from_marketwatch("URC", 1995, 2022)
# get_batch_stock_data_from_marketwatch("TEL", 1995, 2022)
# get_batch_stock_data_from_marketwatch("MAXS", 1995, 2022)
# get_batch_stock_data_from_marketwatch("PIZZA", 1995, 2022)
# get_batch_stock_data_from_marketwatch("FB", 1995, 2022)
# get_batch_stock_data_from_marketwatch("MPI", 1995, 2022)
# get_batch_stock_data_from_marketwatch("GLO", 1995, 2022)
# get_batch_stock_data_from_marketwatch("ICT", 1995, 2022)
# get_batch_stock_data_from_marketwatch("ACEN", 1995, 2022)
# get_batch_stock_data_from_marketwatch("MEG", 1995, 2022)
# get_batch_stock_data_from_marketwatch("ALI", 1995, 2022)
# get_batch_stock_data_from_marketwatch("SECB", 1995, 2022)
# get_batch_stock_data_from_marketwatch("SMPH", 1995, 2022)
# get_batch_stock_data_from_marketwatch("AUB", 1995, 2022)
# get_batch_stock_data_from_marketwatch("2GO", 1995, 2022)
# get_batch_stock_data_from_marketwatch("DMC", 1995, 2022)
# get_batch_stock_data_from_marketwatch("AP", 1995, 2022)
# get_batch_stock_data_from_marketwatch("FGEN", 1995, 2022)
# get_batch_stock_data_from_marketwatch("CEB", 1995, 2022)
# get_batch_stock_data_from_marketwatch("GMA7", 1995, 2022)
# get_batch_stock_data_from_marketwatch("PAL", 1995, 2022)
# get_batch_stock_data_from_marketwatch("MONDE", 1995, 2022)
# get_batch_stock_data_from_marketwatch("JGS", 1995, 2022)

# get_batch_stock_data_from_marketwatch("RLC", 1995, 2022)
# get_batch_stock_data_from_marketwatch("HVN", 1995, 2022)
# get_batch_stock_data_from_marketwatch("MBT", 1995, 2022)
# get_batch_stock_data_from_marketwatch("UBP", 1995, 2022)
# get_batch_stock_data_from_marketwatch("PCOR", 1995, 2022)
# get_batch_stock_data_from_marketwatch("SCC", 1995, 2022)
# get_batch_stock_data_from_marketwatch("STR", 1995, 2022)
# get_batch_stock_data_from_marketwatch("RRHI", 1995, 2022)
# get_batch_stock_data_from_marketwatch("SEVN", 1995, 2022)
# get_batch_stock_data_from_marketwatch("DELM", 1995, 2022)
# get_batch_stock_data_from_marketwatch("EMI", 1995, 2022)
# get_batch_stock_data_from_marketwatch("GSMI", 1995, 2022)
# get_batch_stock_data_from_marketwatch("MBC", 1995, 2022)
# get_batch_stock_data_from_marketwatch("TBGI", 1995, 2022)
# get_batch_stock_data_from_marketwatch("ABS", 1995, 2022)
# get_batch_stock_data_from_marketwatch("CNVRG", 1995, 2022)
# get_batch_stock_data_from_marketwatch("NOW", 1995, 2022)
# get_batch_stock_data_from_marketwatch("C", 1995, 2022)
# get_batch_stock_data_from_marketwatch("ATI", 1995, 2022)
# get_batch_stock_data_from_marketwatch("FPH", 1995, 2022)
# get_batch_stock_data_from_marketwatch("MER", 1995, 2022)
# get_batch_stock_data_from_marketwatch("AEV", 1995, 2022)
# get_batch_stock_data_from_marketwatch("MWC", 1995, 2022)

# PGOLD, FNI
# get_batch_stock_data_from_marketwatch("PGOLD", 1995, 2022)
# get_batch_stock_data_from_marketwatch("FNI", 1995, 2022)
# PX
# get_batch_stock_data_from_marketwatch("PX", 1995, 2022)
# MB
# get_batch_stock_data_from_marketwatch("MB", 1995, 2022)
# DITO
# get_batch_stock_data_from_marketwatch("DITO", 1995, 2022)
# SCC, MER
get_batch_stock_data_from_marketwatch("SCC", 1995, 2022)
get_batch_stock_data_from_marketwatch("MER", 1995, 2022)
