from tkinter import Toplevel, Label, Scale, Button, HORIZONTAL, RIGHT, BOTH
import cv2


class AdjustFrame(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image

        self.s_label = Label(self, font=("arial bold", 10), text="Độ bão hòa")
        self.s_scale = Scale(self, background="#ccc", from_=-100, to=100, troughcolor="#f5eaab",
                             length=250, resolution=1, orient=HORIZONTAL)
        self.v_label = Label(self, font=("arial bold", 10), text="Độ sáng")
        self.v_scale = Scale(self, background="#ccc", from_=-100, to=100, troughcolor="#f5eaab",
                             length=250, resolution=1, orient=HORIZONTAL)

        self.apply_button = Button(self, font=("arial bold", 10), text="Áp dụng", activebackground='green')
        self.preview_button = Button(self, font=("arial bold", 10), text="Xem trước", activebackground='green')
        self.cancel_button = Button(self, font=("arial bold", 10), text="Thoát", activebackground='green')

        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.preview_button.bind("<ButtonRelease>", self.show_button_release)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.s_label.pack(fill=BOTH)
        self.s_scale.pack(fill=BOTH)
        self.v_label.pack(fill=BOTH)
        self.v_scale.pack(fill=BOTH)
        self.cancel_button.pack(side=RIGHT, padx=10, pady=5)
        self.preview_button.pack(side=RIGHT, padx=10, pady=5)
        self.apply_button.pack(side=RIGHT, padx=10, pady=5)

    def apply_button_released(self, event):
        self.master.undo_save = self.master.processed_image
        self.master.u.append(self.master.undo_save)
        self.master.processed_image = self.processing_image
        self.close()

    def show_button_release(self, event):
        self.processing_image = cv2.cvtColor(self.processing_image, cv2.COLOR_RGB2HSV)
        h, s, v = cv2.split(self.processing_image)

        for s_value in s:
            cv2.add(s_value, self.s_scale.get(), s_value)
        for v_value in v:
            cv2.add(v_value, self.v_scale.get(), v_value)

        self.processing_image = cv2.merge((h, s, v))
        self.processing_image = cv2.cvtColor(self.processing_image, cv2.COLOR_HSV2RGB)
        self.show_image(self.processing_image)

    def cancel_button_released(self, event):
        self.close()

    def show_image(self, img=None):
        self.master.image_viewer.show_image(img=img)

    def close(self):
        self.show_image()
        self.destroy()
