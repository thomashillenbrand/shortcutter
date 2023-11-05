import sys
from tkinter import PhotoImage, StringVar, Tk, filedialog, messagebox, ttk

from data.constants import DESKTOP_TEMPLATE
from models.desktop_file_entry_form import FileContentsEntryForm


class ShortcutterApp:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry('400x300')

        # TEH TODO: plenty to do with regard to formatting andf making it look pretty..

        # self.title_label = ttk.Label(
        #     self.root, name='title', text='Welcome to Shortcutter')
        # # self.title_label.pack(anchor='n')
        # self.title_label.grid(column=0, row=0)

        self.selected_app = StringVar(value=None)
        self.app_label = ttk.Label(
            self.root, name='app_label', textvariable=self.selected_app)
        # self.app_label.pack(anchor='e')
        self.app_label.grid(column=1, row=1)
        self.select_app_btn = ttk.Button(
            self.root, name='select_app_btn', text='Select Application', command=self.select_application)
        # self.select_app_btn.pack(anchor='w', padx=10, pady=10)
        self.select_app_btn.grid(column=0, row=1, padx=10, pady=10)

        self.selected_icon = StringVar(value=None)
        self.icon_label = ttk.Label(
            self.root, name='icon_label', textvariable=self.selected_icon)
        # self.icon_label.pack(anchor='e')
        self.icon_label.grid(column=1, row=2)
        self.select_icon_btn = ttk.Button(
            self.root, name='select_icon_btn', text='Select Icon', command=self.select_icon)
        # self.select_icon_btn.pack(anchor='w', padx=10, pady=10)
        self.select_icon_btn.grid(column=0, row=2, padx=10, pady=10)

        self.generate_btn = ttk.Button(
            self.root, text='Generate .desktop file', command=self.generate_desktop_file)
        # self.generate_btn.pack()
        self.generate_btn.grid(column=0, row=3, padx=10)

        self.clear_btn = ttk.Button(
            self.root, text='Clear selections', command=self.clear_selections)
        # self.clear_btn.pack(anchor='s')
        self.clear_btn.grid(column=0, row=4, padx=10, pady=3)

    def show_message(self, message):
        messagebox.showinfo(message=message)

    def select_application(self):
        file_types = (('All files', '*.*'), )
        selected_app_path = filedialog.askopenfilename(
            initialdir='~', filetypes=file_types)

        self.selected_app.set(selected_app_path)

    def select_icon(self):
        file_types = (('png files', '*.png'), )
        selected_icon_path = filedialog.askopenfilename(
            initialdir='~', filetypes=file_types)

        self.selected_icon.set(selected_icon_path)
        icon_image = PhotoImage(file=selected_icon_path)
        self.icon_label['image'] = icon_image
        self.icon_label.image = icon_image

    def generate_desktop_file(self):

        if (self.selected_app.get() and self.selected_app.get() != '' and
                self.selected_icon.get() and self.selected_icon != ''):

            dialog = FileContentsEntryForm(self.root)

            file_content = DESKTOP_TEMPLATE.format(
                entry_type='Application',
                app_name=dialog.app_name,
                version=dialog.version,
                comment=dialog.comment,
                executable=self.selected_app.get(),
                icon_path=self.selected_icon.get(),
                is_terminal='False',
                categories=dialog.categories)

            file_name = f'/usr/share/applications/{dialog.app_name.lower()}.desktop'
            desktop_file = open(file_name, 'w')
            desktop_file.write(file_content)

            self.show_message(
                f'.desktop file created successfully: {file_name}')

        elif (self.selected_app.get()):
            self.show_message("Please select an icon!")
        elif (self.selected_icon.get()):
            self.show_message("Please select an application!")
        else:
            self.show_message("Please select an application and icon!")

    def clear_selections(self):
        self.selected_app.set('')
        self.selected_icon.set('')
        self.icon_label['image'] = None
        self.icon_label.image = None

    def run(self):
        self.root.mainloop()


def main():
    try:
        ShortcutterApp().run()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()
