from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}


def converter(amount: int, from_cur: str, to_cur: str):
    r = requests.get(f'https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={from_cur}&To={to_cur}',
                     headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    res = soup.find('p', class_='sc-1c293993-1 fxoXHw').get_text(strip=True)
    return float(res[:4])


print(converter(1, 'EUR', 'AZN'))
