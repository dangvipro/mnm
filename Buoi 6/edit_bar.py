from tkinter import Frame, Button, LEFT, messagebox
from tkinter import filedialog
from filter_frame import FilterFrame
from adjust_frame import AdjustFrame
import cv2  


class EditBar(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master)

        self.capture_button = Button(self, font=("arial bold", 12), text="Chụp ảnh", width=10, activebackground='green',
                                 background="#28217a", foreground='white')
        self.new_button = Button(self, font=("arial bold", 12), text="Chọn ảnh", width=10, activebackground='green',
                                 background="#28217a", foreground='white')
        self.save_button = Button(self, font=("arial bold", 12), text="Lưu", width=10, activebackground='green',
                                  background="#28217a", foreground='white')
        self.save_as_button = Button(self, font=("arial bold", 12), text="Lưu ảnh mới", width=10, activebackground='green',
                                     background="#28217a", foreground='white')
        self.draw_button = Button(self, font=("arial bold", 12), text="Vẽ", width=10, activebackground='green',
                                  background="#28217a", foreground='white')
        self.crop_button = Button(self, font=("arial bold", 12), text="Cắt", width=10, activebackground='green',
                                  background="#28217a", foreground='white')
        self.filter_button = Button(self, font=("arial bold", 12), text="Bộ lọc", width=10, activebackground='green',
                                    background="#28217a", foreground='white')
        self.adjust_button = Button(self, font=("arial bold", 12), text="Điều chỉnh", width=10, activebackground='green',
                                    background="#28217a", foreground='white')
        self.undo_button = Button(self,background="#28217a", font=("arial bold", 12), text="Hoàn tác",width=10,
                                  activebackground='green', foreground='white')
        self.redo_button = Button(self,background="#28217a", font=("arial bold", 12), text="Làm lại",width=10,
                                  activebackground='green', foreground='white')
        self.clear_button = Button(self, font=("arial bold", 12), text="Xóa", width=10, activebackground='green',
                                   background="#28217a", foreground='white')
        
        self.capture_button.bind("<ButtonRelease>", self.capture_button_released)
        self.new_button.bind("<ButtonRelease>", self.new_button_released)
        self.save_button.bind("<ButtonRelease>", self.save_button_released)
        self.save_as_button.bind("<ButtonRelease>", self.save_as_button_released)
        self.draw_button.bind("<ButtonRelease>", self.draw_button_released)
        self.crop_button.bind("<ButtonRelease>", self.crop_button_released)
        self.filter_button.bind("<ButtonRelease>", self.filter_button_released)
        self.adjust_button.bind("<ButtonRelease>", self.adjust_button_released)
        self.undo_button.bind("<ButtonRelease>", self.undo_button_released)
        self.redo_button.bind("<ButtonRelease>", self.redo_button_released)
        self.clear_button.bind("<ButtonRelease>", self.clear_button_released)

        self.capture_button.pack(side=LEFT, padx=3)
        self.new_button.pack(side=LEFT, padx=3)
        self.save_button.pack(side=LEFT, padx=3)
        self.save_as_button.pack(side=LEFT, padx=3)
        self.draw_button.pack(side=LEFT, padx=3)
        self.crop_button.pack(side=LEFT, padx=3)
        self.filter_button.pack(side=LEFT, padx=3)
        self.adjust_button.pack(side=LEFT, padx=3)
        self.undo_button.pack(side = LEFT, padx=3)
        self.redo_button.pack(side = LEFT, padx=3)
        self.clear_button.pack( side=LEFT, padx=3)

    def new_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.new_button:
            if self.master.is_draw_state:
                self.master.image_viewer.deactivate_draw()
            if self.master.is_crop_state:
                self.master.image_viewer.deactivate_crop()
            filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.gif")])
            if filename=="":
                image=None
            else:
                image = cv2.imread(filename)
            if image is not None:
                self.master.filename = filename
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                self.master.image_viewer.show_image()
                self.master.is_image_selected = True
                self.master.undo_save = image.copy()
                self.master.u = []
                self.master.r = []
                self.master.u.append(self.master.undo_save)
            elif (image is None) and (self.master.original_image is None):
                messagebox.showinfo("Thông báo", "Chưa tải ảnh lên")

    def save_button_released(self, event):
        if (self.master.original_image is not None):
            if self.winfo_containing(event.x_root, event.y_root) == self.save_button:
                if self.master.is_image_selected:
                    if self.master.is_crop_state:
                        self.master.image_viewer.deactivate_crop()
                    if self.master.is_draw_state:
                        self.master.image_viewer.deactivate_draw()

                    save_image = self.master.processed_image
                    image_filename = self.master.filename
                    cv2.imwrite(image_filename, save_image)
                    messagebox.showinfo("Thông báo", "Lưu thành công")
        else:
            messagebox.showinfo("Thông báo", "Chưa tải ảnh lên")

    def save_as_button_released(self, event):
        if (self.master.original_image is not None):
            if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
                if self.master.is_image_selected:
                    if self.master.is_draw_state:
                        self.master.image_viewer.deactivate_draw()
                    if self.master.is_crop_state:
                        self.master.image_viewer.deactivate_crop()

                    original_file_type = self.master.filename.split('.')[-1]
                    filename = filedialog.asksaveasfilename()
                    filename = filename + "." + original_file_type

                    save_image = self.master.processed_image
                    cv2.imwrite(filename, save_image)
                    messagebox.showinfo("Thông báo", "Lưu thành công")
                    self.master.filename = filename
        else:
            messagebox.showinfo("Thông báo", "Chưa tải ảnh lên")

    def draw_button_released(self, event):
        if (self.master.original_image is not None):
            if self.winfo_containing(event.x_root, event.y_root) == self.draw_button:
                if self.master.is_image_selected:
                    if self.master.is_crop_state:
                        self.master.image_viewer.deactivate_crop()
                    if self.master.is_draw_state:
                        self.master.image_viewer.deactivate_draw()
                    else:
                        self.master.image_viewer.activate_draw()
        else:
            messagebox.showinfo("Thông báo", "Chưa tải ảnh lên")

    def crop_button_released(self, event):
        if (self.master.original_image is not None):
            if self.winfo_containing(event.x_root, event.y_root) == self.crop_button:
                try:
                    if self.master.is_image_selected:
                        if self.master.is_draw_state:
                            self.master.image_viewer.deactivate_draw()
                        if self.master.is_crop_state:
                            self.master.image_viewer.deactivate_crop()
                        else:
                            self.master.image_viewer.activate_crop()
                except:
                    messagebox.showerror("Lỗi", "Chọn vùng cắt không hợp lệ")
        else:
            messagebox.showinfo("Thông báo", "Chưa tải ảnh lên")

    def filter_button_released(self, event):
        if (self.master.original_image is not None):
            if self.winfo_containing(event.x_root, event.y_root) == self.filter_button:
                if self.master.is_image_selected:
                    if self.master.is_draw_state:
                        self.master.image_viewer.deactivate_draw()
                    if self.master.is_crop_state:
                        self.master.image_viewer.deactivate_crop()

                    self.master.filter_frame = FilterFrame(master=self.master)
                    self.master.filter_frame.grab_set()
        else:
            messagebox.showinfo("Thông báo", "Chưa tải ảnh lên")

    def adjust_button_released(self, event):
        if (self.master.original_image is not None):
            if self.winfo_containing(event.x_root, event.y_root) == self.adjust_button:
                if self.master.is_image_selected:
                    if self.master.is_draw_state:
                        self.master.image_viewer.deactivate_draw()
                    if self.master.is_crop_state:
                        self.master.image_viewer.deactivate_crop()

                    self.master.adjust_frame = AdjustFrame(master=self.master)
                    self.master.adjust_frame.grab_set()
        else:
            messagebox.showinfo("Thông báo", "Chưa tải ảnh lên")

    def clear_button_released(self, event):
        if (self.master.original_image is not None):
            if self.winfo_containing(event.x_root, event.y_root) == self.clear_button:
                if self.master.is_image_selected:
                    if self.master.is_draw_state:
                        self.master.image_viewer.deactivate_draw()
                    if self.master.is_crop_state:
                        self.master.image_viewer.deactivate_crop()

                    self.master.u.append(self.master.processed_image)
                    self.master.processed_image = self.master.original_image.copy()
                    '''self.master.undo_save = self.master.original_image.copy()
                    self.master.u = []
                    self.master.r = []
                    self.master.u.append(self.master.undo_save)'''
                    self.master.image_viewer.show_image()
        else:
            messagebox.showinfo("Thông báo", "Chưa tải ảnh lên")

    def undo_button_released(self, event):
        if (self.master.original_image is not None):
            if self.winfo_containing(event.x_root, event.y_root) == self.undo_button:
                if self.master.is_image_selected:
                    if self.master.is_draw_state:
                        self.master.image_viewer.deactivate_draw()
                    if self.master.is_crop_state:
                        self.master.image_viewer.deactivate_crop()
                    #self.master.processed_image = self.master.undo_save.copy()
                    if (len(self.master.u) - 1 >= 0):
                        self.master.r.append(self.master.processed_image)
                        self.master.processed_image = self.master.u[len(self.master.u) - 1]
                        self.master.u.pop(-1)
                    else: 
                        pass
                    self.master.image_viewer.show_image()
        else:
            messagebox.showinfo("Thông báo", "Chưa tải ảnh lên")

    def redo_button_released(self, event):
        if (self.master.original_image is not None):
            if self.winfo_containing(event.x_root, event.y_root) == self.redo_button:
                if self.master.is_image_selected:
                    if self.master.is_draw_state:
                        self.master.image_viewer.deactivate_draw()
                    if self.master.is_crop_state:
                        self.master.image_viewer.deactivate_crop()
                    if (len(self.master.r) - 1 >= 0):
                        self.master.u.append(self.master.processed_image)
                        self.master.processed_image = self.master.r[len(self.master.r) - 1]
                        self.master.r.pop(-1)
                    else: 
                        pass
                    self.master.image_viewer.show_image()
        else:
            messagebox.showinfo("Thông báo", "Chưa tải ảnh lên")
    def open_camera(self):
        def save_captured_image( captured_image):
            if captured_image is not None:
                filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
                if filename:
                    cv2.imwrite(filename, captured_image)
                    messagebox.showinfo("Thông báo", f"Đã lưu ảnh vào {filename}")
                else:
                    messagebox.showinfo("Thông báo", "Lưu ảnh đã được hủy")
            else:
                messagebox.showinfo("Thông báo", "Không có ảnh để lưu")
        # Kết nối với camera
        cap = cv2.VideoCapture(0)

        # Hiển thị hình ảnh từ camera
        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow('Camera', frame)

                # Chờ phím nhấn từ người dùng (vd: ESC để thoát, SPACE để chụp ảnh)
                key = cv2.waitKey(1)
                if key == 27 :  # ESC key
                    break
                elif key == 32:  # SPACE key
                    # Chụp ảnh khi nhấn SPACE
                    captured_image = frame.copy()
                    save_captured_image(captured_image)
                    break

        # Giải phóng và đóng cửa sổ camera
        cap.release()
        cv2.destroyAllWindows()
    def capture_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.capture_button:
            self.open_camera()  # Gọi hàm mở camera khi nút chụp ảnh được nhấn
