import csv

import requests
from bs4 import BeautifulSoup

stock_codes = [
    "JFC",
    "MAXS",
    "PIZZA",
    "FCG",
    "SMPH",
    "HVN",
    "ALI",
    "AC",
    "MEG",
    "RLC",
    "BDO",
    "BPI",
    "MBT",
    "UBP",
    "SECB",
    "AUB",
    "SMC",
    "PCOR",
    "TFHI",
    "ACEN",
    "DMC",
    "SCC",
    "SM",
    "STR",
    "MONDE",
    "RRHI",
    "SEVN",
    "URC",
    "JGS",
    "DELM",
    "FB",
    "EMI",
    "GSMI",
    "GMA7",
    "MBC",
    "TBGI",
    "ABS",
    "TEL",
    "GLO",
    "CNVRG",
    "NOW",
    "CEB",
    "PAL",
    "2GO",
    "C",
    "ICT",
    "ATI",
    "AP",
    "FPH",
    "FGEN",
    "MER",
    "AEV",
    "MPI",
    "MWC",
    # New
    "FNI",
    "PX",
    "APX",
    "NIKL",
    "MB",
    "PGOLD",
    "MRSGI",
    "DITO",
]


def get_info(soup: BeautifulSoup, label: str) -> str | None:
    """
    Get company info from soup object with the following format:
    <th>label</th><td>value</td>
    """
    th_element = soup.find("th", string=label)
    if th_element is None:
        print("Label %s not found", label)
        return None

    td_element = th_element.find_next_sibling("td")
    if td_element is None:
        print("Value for label %s not found", label)
        return None

    value = td_element.text.strip()

    return value


def fetch_company_id(stock_symbol: str) -> int | None:
    """Fetch company ID from PSE website based on stock symbol"""
    stock_symbol = stock_symbol.lower()
    search_url = (
        f"https://edge.pse.com.ph/autoComplete/searchCompanyNameSymbol.ax?term={stock_symbol}"
    )
    response = requests.get(search_url, timeout=10)
    response.raise_for_status()

    try:
        search_results = response.json()
        for stock in search_results:
            symbol = stock["symbol"]
            if symbol.lower() == stock_symbol:
                company_id = int(stock["cmpyId"])
                return company_id
            else:
                continue
        print(f"Company ID not found for stock symbol {stock_symbol}")
        return None
    except IndexError:
        print(f"Company ID not found for stock symbol {stock_symbol}")
        return None


company_info = []

for stock_code in stock_codes:

    company_id = fetch_company_id(stock_code)
    if company_id is None:
        continue
    url = f"https://edge.pse.com.ph/companyInformation/form.do?cmpy_id={company_id}"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    sector = get_info(soup, "Sector")
    sub_sector = get_info(soup, "Subsector")
    company_info.append({"stock_code": stock_code, "sector": sector, "sub_sector": sub_sector})

# Sort company_info by sector, then sub_sector
# company_info.sort(key=lambda x: (x["sector"], x["sub_sector"]))
company_info.sort(key=lambda x: (x["sector"], x["sub_sector"]))

with open("company_info.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["stock_code", "sector", "sub_sector"])
    writer.writeheader()
    writer.writerows(company_info)
