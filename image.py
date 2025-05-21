from PIL import Image, ImageTk
from waifu2x_ncnn_py import Waifu2x
from rembg import remove

class Img:
    """Class for managing images."""

    def __init__(self, path) -> None:
        self.img = Image.open(path)

    def image_tkinter(self, max_size) -> ImageTk.PhotoImage:
        """Convert the image for insertion into Tkinter.

        Args:
            max_size (int): maximum width and height for the image.

        Returns:
            ImageTk.PhotoImage: image object compatible with Tkinter.
        """
        self.new_image = self.img.copy()
        self.new_image.thumbnail((max_size, max_size))
        return ImageTk.PhotoImage(self.new_image)

    def save(self, path):
        """Save the image to the specified path.

        Args:
            path (str): destination path for saving the image.
        """
        self.img.save(path)

    def rotate(self, degrees):
        """Rotate the image and expand the canvas to fit.

        Args:
            degrees (int | float): rotation angle in degrees.
        """
        self.img = self.img.rotate(degrees, expand=True)

    def black_white(self):
        """Convert the image to grayscale."""
        self.img = self.img.convert("L")

    def scale_image(self, model, scale, noise):
        """Scale the image using waifu2x.

        Args:
            model (str): 'Anime' or 'Photo'.
            scale (str): 'x2', 'x4' or 'x8'.
            noise (str): 'Nothing', 'Low', 'Medium', 'High' or 'Highest'.
        """

        model = "models-upconv_7_anime_style_art_rgb" if model == "Anime" else "models-upconv_7_photo"

        if scale == "x2":
            scale = 1
        elif scale == "x4":
            scale = 2
        elif scale == "x8":
            scale = 3

        if noise == "Nothing":
            noise = -1
        elif noise == "Low":
            noise = 0
        elif noise == "Medium":
            noise = 1
        elif noise == "High":
            noise = 2
        else:
            noise = 3

        waifu2x = Waifu2x(model=model, scale=2, noise=noise)
        for x in range(scale):
            self.img = waifu2x.process_pil(self.img)

    def remove_bg(self):
        """Remove the background from the image."""
        self.img = remove(self.img)
