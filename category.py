import os
import json

class BookCategory:
    def __init__(self):
        self.current_category = ["Books"]
        self.category_data = self.get_categories()

    def get_categories():
        with open("./category.json", "rb") as f:
            category_data = json.loads(f.read())
        return category_data

    def check_command(slef):
        self.command_detail()

        print("[command mode]")
        command = input("please enter command:")

        if command == "new":
            self.create_category()

        elif command == "select":
            self.select_category()

        elif command == "move":
            self.move_category()

        elif command == "back":
            self.back_category()

        elif commad == "q":

        else:
            print("Your command is invalid.")
            self.command_detail()

    def command_detail(self):
        print("--------------------------------------------------------------")
        print("| command | detail                                           |")
        print("--------------------------------------------------------------")
        print("| new     | create a new category                            |")
        print("| select  | select category where you want to save book data |")
        print("| move    | move other category                              |")
        print("| back    | move to parent category                          |")
        print("--------------------------------------------------------------")

    def create_category(self):
        print("[new mode]")
        category_list = self.get_category_list()
        while True:
            category_name = input("Please enter category name(if you enter 'q', you can back [command mode]):")
            if category_name not in category_list:
                category_path = self.get_category_path
                os.mkdir(category_path)


            else:
                print("Category {} is already exist.".format(category_name))

    def get_category_path(self, category_name):
        category_path = "./"
        for level in self.current_category:
            category_path = os.path.join(category_path, level)

        return category_path

    def get_category_list(self):
        category_data = self.category_data
        for level in self.current_category:
            category_data = category_data[level]

        return category_data

    def update_category_list(self, new_category_list):
        category_data = self.category_data

        for level in self.current_category[:-1]:
            category_data = category_data[level]

        category_data[self.current_category[-1]] = new_category_list

def select_category():
    while True:
        category_data = get_categories()
        category_name = input("Please enter category name(if you want to create new category, please enter 'new'):")
        if category_name == "new":
            create_category()

        elif category_name in categories:
            return category_name

        else:
            print("Category {} was not found.".format(category_name))
