#!/bin/python
import customtkinter as CTk
from tkinter import filedialog, PhotoImage
from image import Img

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("blue")

class App(CTk.CTk):
    """windows the my app
    """
    def __init__(self) -> None:
        super().__init__()
        self.title("See Image")
        self.geometry("800x700")
        self.resizable(0,0)
        self.size_button = 50
        self.max_image = 600
        
        
        
        
        ######## button box #######
        self.frame_buttons = CTk.CTkFrame(self,
                                          width=750,
                                          height=80)
        self.frame_buttons.pack(pady=10, ipadx=10, ipady=10)
        
        ######## app button #######
        self.btn_new_image = PhotoImage(file="icon/file-plus.png")
        self.btn_new = CTk.CTkButton(self.frame_buttons,
                                     image=self.btn_new_image,
                                     text="",
                                     width=self.size_button,
                                     height=self.size_button,
                                     command=self.button_new)
        self.btn_new.pack(side="left", padx=5)
        
        self.btn_rotate_left_image = PhotoImage(file="icon/rotate-left.png")
        self.btn_rotate_left = CTk.CTkButton(self.frame_buttons,
                                     image=self.btn_rotate_left_image,
                                     text="",
                                     width=self.size_button,
                                     height=self.size_button,
                                     state="disabled",
                                     command=lambda:self.button_rotate(90))
        self.btn_rotate_left.pack(side="left", padx=5)
        
        self.btn_rotate_right_image = PhotoImage(file="icon/rotate-right.png")
        self.btn_rotate_right = CTk.CTkButton(self.frame_buttons,
                                     image=self.btn_rotate_right_image,
                                     text="",
                                     width=self.size_button,
                                     height=self.size_button,
                                     state="disabled",
                                     command=lambda:self.button_rotate(-90))
        self.btn_rotate_right.pack(side="left", padx=5)
        
        self.btn_black_white_image = PhotoImage(file="icon/black-and-white.png")
        self.btn_black_white = CTk.CTkButton(self.frame_buttons,
                                     image=self.btn_black_white_image,
                                     text="",
                                     width=self.size_button,
                                     height=self.size_button,
                                     state="disabled",
                                     command=self.button_black_white)
        self.btn_black_white.pack(side="left", padx=5)
        
        self.btn_scale_ia_image = PhotoImage(file="icon/scale-ia.png")
        self.btn_scale_ia = CTk.CTkButton(self.frame_buttons,
                                     image=self.btn_scale_ia_image,
                                     text="",
                                     width=self.size_button,
                                     height=self.size_button,
                                     state="disabled",
                                     command=self.button_scale_ia)
        self.btn_scale_ia.pack(side="left", padx=5)
        
        self.btn_save_image = PhotoImage(file="icon/save.png")
        self.btn_save = CTk.CTkButton(self.frame_buttons,
                                     image=self.btn_save_image,
                                     text="",
                                     width=self.size_button,
                                     height=self.size_button,
                                     state="disabled",
                                     command=self.button_save)
        self.btn_save.pack(side="right", padx=5)
        
        
        
        
        ######## image diplay #######
        self.display = CTk.CTkFrame(self, width=self.max_image, height=self.max_image)
        self.display.pack()
        
        self.image = CTk.CTkLabel(self.display,
                                  text="",
                                  width=self.max_image,
                                  height=self.max_image)
        self.image.pack()

    
    def button_new(self):
        """look a file jpg or png. create and insert in
        the window the image
        """
        self.file_image = filedialog.askopenfilename(title="Add Image", parent=self,
                                                filetypes=[
                                                    ("ALL files", ("*.jpg","*.png","*.webp"))
                                                ])
        if self.file_image != ():
            self.image.destroy()
            self.img = Img(self.file_image)
            self.img_Tk = self.img.image_tkinter(self.max_image)
            self.image = CTk.CTkLabel(master=self.display,
                                      image=self.img_Tk,
                                      width=self.max_image,
                                      text="",
                                      height=self.max_image)
            self.image.image = self.img
            self.image.pack()
            
            self.activate_button()
    
    def activate_button(self):
        """activate the edition button and save
        """
        self.btn_save.configure(state="normal")
        self.btn_rotate_left.configure(state="normal")
        self.btn_rotate_right.configure(state="normal")
        self.btn_black_white.configure(state="normal")
        self.btn_scale_ia.configure(state="normal")
    
    def button_save(self):
        """save image
        """
        path_save = filedialog.asksaveasfilename(title="Save Image",parent=self,
                                                filetypes=[
                                             ("PNG", "*.png"),
                                            ])
        path_save = path_save + ".png" if path_save[-4:] != ".png" else path_save
        self.img.save(path_save)

    def button_rotate(self, degrees):
        """rotate the image and update image display
        """
        self.img.rotate(degrees)
        self.update_image()

    def button_black_white(self):
        """tranform color image in black and white and image update
        """
        self.img.black_white()
        self.update_image()
    
    def button_scale_ia(self):
        """Create windows for scale."""

        window_scale = CTk.CTkToplevel(self)
        window_scale.title("Scale IA")

        window_scale.geometry("400x500")

        label_model = CTk.CTkLabel(window_scale, text="Model:")
        label_model.pack(pady=20)

        box_model = CTk.CTkComboBox(window_scale, values=["Anime","Photo"])
        box_model.pack()

        label_noise = CTk.CTkLabel(window_scale, text="Noise:")
        label_noise.pack(pady=20)

        box_noise = CTk.CTkComboBox(window_scale, values=["Nothing","Low","Medium","High","Highest"])
        box_noise.pack()


        btn_window_close = CTk.CTkButton(window_scale, text="Scale", command=lambda: self.window_scale_close(window_scale,box_model.get(),box_noise.get()))
        btn_window_close.pack(pady=20)


    def window_scale_close(self, window, model, noise):
        """close window and scale image"""
        self.img.scale_image(model,noise)
        window.destroy()
 
    def update_image(self):
        """resize image and update the label in tkinter
        """
        self.img_Tk = self.img.image_tkinter(self.max_image)
        self.image.configure(image=self.img_Tk)
        self.image.image = self.img_Tk

if __name__ == "__main__":
    program = App()
    program.mainloop()
