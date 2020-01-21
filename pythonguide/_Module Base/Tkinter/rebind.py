import tkinter as tk


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.text = tk.Text(self)
        self.text.pack(fill="both", expand=True)

        # add a tag that lets us apply the overstrike attribute
        self.text.tag_configure("overstrike", overstrike=True)

        # add a binding on the backspace key
        self.text.bind("<BackSpace>", self.handleBackspace)

    def handleBackspace(self, event):
        # add the overstrike to the character before the
        # insertion cursor
        self.text.tag_add("overstrike", "insert-1c", "insert")

        # move the cursor to the previous position
        self.text.mark_set("insert", "insert-1c")

        # prevent the default behaviour
        return "break"


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
