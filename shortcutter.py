import sys
from tkinter import PhotoImage, StringVar, Tk, filedialog, ttk

from data.constants import DESKTOP_TEMPLATE
from models.desktop_file_entry_form import FileContentsEntryForm


class ShortcutterApp:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry('400x300')
        self.root.title = ('Shortcutter')

        self.title_label = ttk.Label(
            self.root, name='title', text="Welcome to Shortcutter")
        self.title_label.pack()

        self.selected_app = StringVar(value=None)
        self.app_entry = ttk.Entry(
            self.root, name='app_entry', textvariable=self.selected_app)
        self.app_entry.pack()
        self.select_app_btn = ttk.Button(
            self.root, name='select_app_btn', text="Select from File", command=self.select_application)
        self.select_app_btn.pack()

        self.selected_icon = StringVar(value=None)
        self.icon_entry = ttk.Entry(
            self.root, name='icon_entry', textvariable=self.selected_icon)
        self.icon_entry.pack()
        self.select_icon_btn = ttk.Button(
            self.root, name='select_icon_btn', text='Select from File', command=self.select_icon)
        self.select_icon_btn.pack()

        self.generate_btn = ttk.Button(
            self.root, text='Generate .desktop file', command=self.generate_desktop_file)
        self.generate_btn.pack()

    def select_application(self):
        file_types = (('All files', '*.*'), )
        selected_app_path = filedialog.askopenfilename(
            initialdir='/opt/cursor', filetypes=file_types)

        self.selected_app.set(selected_app_path)

    def select_icon(self):
        file_types = (('png files', '*.png'), )
        selected_icon_path = filedialog.askopenfilename(
            initialdir='/home/tomhillenbrand', filetypes=file_types)

        self.selected_icon.set(selected_icon_path)
        # TEH TODO: display the icon image
        # icon_image = PhotoImage(file=selected_icon_path)
        # icon_label['image'] = icon_image
        # icon_label.image = icon_image
        # icon_label['text'] = selected_icon_path
        # icon_label.text = selected_icon_path
        # icon_label.pack()  # (column=1, row=3)

    def generate_desktop_file(self):

        dialog = FileContentsEntryForm(self.root)

        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Entry):
                breakpoint()
                # if widget._name == '!label':
                #     icon_path = widget['text']
                # elif widget._name == '!label2':
                #     exec_path = widget['text']

        file_content = DESKTOP_TEMPLATE.format(
            entry_type="Application",
            app_name=dialog.app_name,
            version=dialog.version,
            comment=dialog.comment,
            # path_to_executable="hello",
            # executable=exec_path,
            # icon_path=icon_path,
            is_terminal="False",
            categories=dialog.categories)

        file_name = f'/usr/share/applications/{dialog.app_name.lower()}.desktop'
        # desktop_file = open(file_name, 'w')
        # desktop_file.write(file_content)
        print(file_name)
        print(file_content)

    def run(self):
        self.root.mainloop()


def main():
    try:
        app = ShortcutterApp()
        app.run()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
