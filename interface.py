import customtkinter as CTk
from tkinter import filedialog, PhotoImage
from image import Img

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("blue")

class App(CTk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("See Image")
        self.geometry("800x700")
        self.resizable(0,0)
        self.size_button = 50
        
        
        
        self.frame_buttons = CTk.CTkFrame(self,
                                          width=750,
                                          height=80)
        self.frame_buttons.pack(pady=10, ipadx=10, ipady=10)
        
        self.btn_new_image = PhotoImage(file="icon/file-plus.png")
        self.btn_new = CTk.CTkButton(self.frame_buttons,
                                     image=self.btn_new_image,
                                     text="",
                                     width=self.size_button,
                                     height=self.size_button,
                                     command=self.button_new)
        self.btn_new.pack(side="left", padx=5)
        
        self.image = CTk.CTkLabel(self, text="")
        self.image.pack()


    def loop(self):
        self.mainloop()
    
    def button_new(self):
        self.file_image = filedialog.askopenfilename(parent=self,
                                                filetypes=[
                                                    ("ALL files", ("*.jpg","*.png"))
                                                ])
        if self.file_image != ():
            self.image.destroy()
            self.img = Img(self.file_image).image_tkinter(600)
            self.image = CTk.CTkLabel(self,
                                      image=self.img)
            self.image.image = self.img
            self.image.pack()

if __name__ == "__main__":
    program = App()
    program.loop()