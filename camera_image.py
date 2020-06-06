import cv2
from detect_barcode import  get_book_id
from book_data import get_book_data
from manage_book_data import get_book_list, save_book_list, get_book_ids
import json

def get_capture_image():
    book_list = get_book_list()
    book_ids = []
    new_book_ids = []

    if len(book_list) != 0:
        book_ids = get_book_ids(book_list)

    capture = cv2.VideoCapture(0)

    while True:
        ret, image = capture.read()
        show_image = cv2.flip(image, 1)
        cv2.imshow("Video", show_image)
        book_id = get_book_id(image)

        if book_id != "" and book_id is not None:
            if book_id not in book_ids:
                print("book_id: {}".format(book_id))
                new_book_ids.append(book_id)
                book_ids.append(book_id)
                
        if cv2.waitKey(1) & 0xFF == ord("q"):
            capture.release()
            cv2.destroyAllWindows()

            for book_id in new_book_ids:
                print("collecting book data...")
                book_data = get_book_data(book_id)
                book_data["id"] = book_id
                book_list.append(book_data)

            print("saving book data...")
            save_book_list(book_list)
            break
