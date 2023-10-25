from tkinter import simpledialog, ttk


class FileContentsEntryForm(simpledialog.Dialog):

    def body(self, master):
        self.title("Please provide the following information")

        # Create labels and entry fields for each input
        self.app_name_label = ttk.Label(master, text="App Name")
        self.app_name_label.pack()  # (row=0)
        self.app_name_entry = ttk.Entry(master)
        self.app_name_entry.pack()  # (row=0, column=1)

        self.version_label = ttk.Label(master, text="Version")
        self.version_label.pack()  # (row=1)
        self.version_entry = ttk.Entry(master)
        self.version_entry.pack()  # (row=1, column=1)

        self.comment_label = ttk.Label(master, text="Comment")
        self.comment_label.pack()  # (row=2)
        self.comment_entry = ttk.Entry(master)
        self.comment_entry.pack()  # (row=2, column=1)

        self.categories_label = ttk.Label(master, text="Categories")
        self.categories_label.pack()  # (row=3)
        self.categories_entry = ttk.Entry(master)
        self.categories_entry.pack()  # (row=3, column=1)

        # Set initial focus on the first entry field
        self.initial_focus = self.app_name_entry

    def apply(self):
        self.app_name = self.app_name_entry.get()
        self.version = self.version_entry.get()
        self.comment = self.comment_entry.get()
        self.categories = self.categories_entry.get()
