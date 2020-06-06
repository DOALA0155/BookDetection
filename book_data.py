from bs4 import BeautifulSoup
import requests
from detect_barcode import get_book_id

def get_result_url(book_id):
    base_url = "https://www.kinokuniya.co.jp/disp/CSfDispListPage_001.jsp?qsd=true&ptk=01&gtin={}&q=&title=&author-key=&publisher-key=&pubdateStart=&pubdateEnd=&thn-cod-b=&ndc-dec-key=&rpp=20&SEARCH.x=62&SEARCH.y=30"
    result_url = base_url.format(book_id)
    return result_url

def get_book_url(result_url):
    res = requests.get(result_url)
    soup = BeautifulSoup(res.content, "html.parser")
    book = soup.find("div", class_="list_area")
    book_url = book.find("h3", class_="heightLine-2").find("a")["href"]

    return book_url

def extract_book_data(book_url):
    res = requests.get(book_url)
    soup = BeautifulSoup(res.content, "html.parser")

    book_title = soup.find("h3", attrs={"itemprop": "name"}).text.strip(" ")
    book_author = soup.find("div", class_="infobox").find("a").text
    book_price = int(soup.find("span", class_="sale_price").text.replace("¥", "").replace(",", ""))
    book_explain = soup.find("div", class_="career_box").text.strip("\n")

    book_data = {"title": book_title, "author": book_author, "price": book_price, "explain": book_explain}
    return book_data

def get_book_data(book_id):
    result_url = get_result_url(book_id)
    book_url = get_book_url(result_url)
    book_data = extract_book_data(book_url)
    return book_data
