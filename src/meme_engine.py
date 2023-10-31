"""A meme_engine is able to create, edit and save memes."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


class MemeEngine:
    """Meme Engine class that is consists of different methods to generate memes."""

    def __init__(self, destination: str):
        """Create a new MemeEngine Object."""
        self.destination = destination

    def resize_img(self, image, new_width=500):
        """Resize image if needed."""
        original_width, original_height = image.size
        if original_width == new_width:
            print("Size is already according to expectations.")
        else:
            new_height = int((original_height / original_width) * new_width)
            resized_image = image.resize((new_width, new_height))
            resized_width, resized_height = resized_image.size
            print(
                f"Original image dimensions: {original_width}x{original_height} pixels"
            )
            print(f"Resized image dimensions: {resized_width}x{resized_height} pixels")
            image = resized_image
        return image

    def save_img(self, image):
        """Save meme."""
        image.save("image_example.jpg")

    def add_quote(self, image, quote, author):
        """Add quotes to meme"."""
        draw = ImageDraw.Draw(image)
        font_quote = ImageFont.truetype("fonts/impact.ttf", size=30)
        font_author = ImageFont.truetype("fonts/impact.ttf", size=20)
        draw.text((40, 80), quote, font=font_quote, fill="white")
        draw.text((45, 115), "-" + author, font=font_author, fill="white")
        return image

    def make_meme(self, img_path, text, author):
        """Make meme by using earlier defined methods."""
        try:
            image = Image.open(img_path)
            image = self.resize_img(image)
            print("Starting to add quote...")
            image = self.add_quote(image, text, author)
            print("Saving image...")
            output_path = Path(self.destination) / "meme.jpg"
            print(f"Image saved to: {output_path}")
            image.save(output_path)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return output_path
