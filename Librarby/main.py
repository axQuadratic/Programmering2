from work import *
from book_generator import work_list
import os

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
        except:
            main()
    else:
        choice = 1
    
    view_category(work_list[list(work_list.keys())[choice - 1]])

def view_category(category):
    clear()
    print(f"List of {list(work_list.keys())[list(work_list.values()).index(category)]}:")
    index = 1
    for i in category:
        print(f"{index} - {i.title.capitalize()}")
        index += 1
    try:
        choice = int(input())
    except:
        view_category(category)

    view_work(category[choice - 1])

def view_work(work):
    clear()
    properties = vars(work)
    print(properties["title"])
    del properties["title"]
    for i in list(properties.keys()):
        print(f"{i.replace('_', ' ').capitalize()} - {properties[i]}")
    
    input()
    main()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

main()