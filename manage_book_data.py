import json
import unicodedata

def get_book_list():
    with open("./books.json", "rb") as f:
        books = json.load(f)["Books"]
        return books

def save_book_list(book_list):
    books_data = {"Books": book_list}
    with open("./books.json", "w") as f:
        json.dump(books_data, f)

def get_book_ids(book_list):
    book_ids = []
    for book in book_list:
        id = book["id"]
        book_ids.append(id)

    return book_ids

def show_book_data(book_data):
    title = book_data["title"]
    id = book_data["id"]
    explain = book_data["explain"]
    author = book_data["author"]
    price = str(book_data["price"]) + "円"

    title = check_word_count(title, 50)
    id = check_word_count(id, 50)
    author = check_word_count(author, 50)
    price = check_word_count(price, 50)
    explains = check_explain_data(explain)

    print("-" * 64)
    print("| title   | {} |".format(title))
    print("| ISBN    | {} |".format(id))
    print("| author  | {} |".format(author))
    print("| price   | {} |".format(price))
    print("-" * 64)
    print("| {} |".format(" " * 26 + "explain" + " " * 27))
    for explain in explains:
        print("| {} |".format(check_word_count(explain, 60)))
    print("-" * 64)

def check_explain_data(explain):
    paragraphs = explain.split("\n")
    explains = []
    for paragraph in paragraphs:
        count = get_word_count(paragraph)
        n = 30
        line_list = [paragraph[i : i + n] for i in range(0, count, n)]

        for line in line_list:
            if line != "":
                explains.append(line)

    return explains

def check_word_count(word, limit):
    count = get_word_count(word)
    if count > limit:
        word = word[:limit - 3] + "..."

    else:
        space_count = limit - count
        word += " " * space_count

    return word

def get_word_count(text):
    count = 0
    words = ["〉", "）", "※", "―", "】"]
    for c in text:
        if c in words:
            count += 2
        elif unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count
