from work import *
import os
import atexit
import pickle
import sys
from math import pow

work_list = {
    "books": [Nonfiction("Travelling at Night, Vol. 1", 1923, False, "The Malleary", True, 0, None, "Christopher Illopoly", 1, "Nyctrodomy")],
    "audiobooks": [Audiobook("Travelling at Night, Vol. 1", 2011, False, "The Haustorum", True, 0, "Maltese Audiobooks Inc.", None, "Maltese Man")],
    "hentai": [Hentai("Metamorphosis", 2013, False, "Hell", True, 0, "Pain", "Art", "FAKKU", False)]
}

def main():
    clear()
    print("=== HUSH HOUSE LIBRARY & ARCHIVES ===")
    if len(work_list.keys()) > 1:
        print("Select a category:")
        index = 1
        for i in list(work_list.keys()):
            print(f"{index} - {i.capitalize()}")
            index += 1
        try:
            choice = int(input())
        except Exception as e:
            if type(e) == KeyboardInterrupt:
                sys.exit()
            main()
    else:
        choice = 1
    
    view_category(work_list[list(work_list.keys())[choice - 1]])

def view_category(category):
    clear()
    print(f"List of {list(work_list.keys())[list(work_list.values()).index(category)]}:")
    index = 1
    for i in category:
        print(f"{index} - {i.title}")
        index += 1
    try:
        choice = int(input())
    except Exception as e:
        if type(e) == KeyboardInterrupt:
            sys.exit()
        view_category(category)

    view_work(category[choice - 1])

def view_work(work):
    clear()
    properties = vars(work)
    print(properties["title"])
    for i in list(properties.keys()):
        if i == "title" or i == "borrowed_at": continue
        print(f"{i.replace('_', ' ').capitalize()} - {properties[i]}")

    cur_cat = None
    cur_index = 0
    for i in list(work_list.keys()):
        cur_index = 0
        cur_cat = i
        for j in work_list[i]:
            if j == work:
                break
            cur_index += 1
        else: continue
        break

    if work.in_library:
        print("\n1 - Borrow")

        try:
            assert int(input()) == 1
        except Exception as e:
            if type(e) == KeyboardInterrupt:
                sys.exit()
            main()

        work_list[cur_cat][cur_index].borrow()
        if Book.read in dir(work):
            work.read()
        else:
            print(f"{work.title} has been borrowed.")
        input()

    else:
        print("\nWork is borrowed\n1 - Restore")

        try:
            assert int(input()) == 1
        except Exception as e:
            if type(e) == KeyboardInterrupt:
                sys.exit()
            main()

        days_passed = work_list[cur_cat][cur_index].restore()
        debt = round(pow(1.25, (days_passed - 2)))
        if debt >= 1:
            input(f"{work.title} has been restored; you now owe the library ${debt}.")
        else:
            input(f"{work.title} has been restored.\n")

    main()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def save_state():
    with open("books.dat", "wb") as file:
        file.write(pickle.dumps(work_list))

def load_works():
    global work_list
    with open("books.dat", "rb") as file:
        work_list = pickle.loads(file.read())

atexit.register(save_state)
load_works()
main()