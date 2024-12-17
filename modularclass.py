import tkinter as tk

class ObjectWithAttributes:
    def __init__(self, foo, bar, number, label):
        self.foo = foo
        self.bar = bar
        self.number = number
        self.label = label

objects = {}

root = tk.Tk()

def main():
    objects["o1"] = ObjectWithAttributes("lorem", "ipsum", 69, tk.Label(root, text="Object 1"))
    objects["o2"] = ObjectWithAttributes("twin", "tower", 911, tk.Label(root, text="Object 2"))

    print(objects["o1"].foo) # Prints lorem
    print(objects["o2"].number) # Prints 911

    objects["o1"].label.pack(anchor=tk.CENTER) # Displays "Object 1" label

main()
root.mainloop()