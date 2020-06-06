from pyzbar.pyzbar import decode
import cv2

def get_book_id(image):
    detect_data = decode(image)
    
    if len(detect_data) != 0:
        for id in detect_data:
            id_data = id[0].decode('utf-8', 'ignore')
            if id_data[:3] == "978":
                return id_data

    else:
        return ""
