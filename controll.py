from camera_image import get_capture_image
from manage_book_data import show_book_data, get_book_list

def show_command_explain():
    print("-" * 34)
    print("| command | explain            |")
    print("-" * 34)
    print("| new     | add new book data    |")
    print("| show    | show all book data   |")
    print("| explain | show command explain |")
    print("| quit    | end book app         |")
    print("-" * 34)
    
show_command_explain()
while True:
    command = input("Please enter command: ")
    if command == "new":
        get_capture_image()

    elif command == "show":
        book_list = get_book_list()
        for book in book_list:
            show_book_data(book)

    elif command == "explain":
        show_command_explain()

    elif command == "quit":
        print("End book app")
        break

    else:
        print("Command is invalid")
