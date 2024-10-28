import tkinter as tk
from tkinter import ttk
from edit_bar import EditBar
from viewer import ImageViewer


class Main(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.configure(background="#f5eaab")
        self.filename = ""
        self.original_image = None
        self.processed_image = None
        self.is_image_selected = False
        self.is_draw_state = False
        self.is_crop_state = False

        self.filter_frame = None
        self.adjust_frame = None

        self.title("Image Editor")

        self.editbar = EditBar(master=self)
        separator1 = ttk.Separator(master=self, orient=tk.HORIZONTAL)
        self.image_viewer = ImageViewer(master=self)

        self.editbar.pack(pady=10, padx=10)
        separator1.pack(fill=tk.X, padx=20)
        self.image_viewer.pack(fill=tk.BOTH, padx=20, pady=5, expand=1)


root = Main()
root.mainloop()
