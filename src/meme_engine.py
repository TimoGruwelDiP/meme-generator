from PIL import Image, ImageDraw, ImageFont

#image = Image.open("_data/photos/dog/xander_test.jpg")

class MemeEngine():

    # def __init__(self, img_path, text, author):
    #     self.img_path = img_path
    #     self.name = self.img_path.rsplit('/', 1)[-1]
    #     self.text = text
    #     self.author = author
    #     self.image = Image.open(self.img_path)

    def __init__(self, destination):
        self.destination = destination

    def resize_img(self, image, new_width=500):
        original_width, original_height = image.size
        if original_width == 500:
            print("Size is already according to expectations.")
        else: 
            new_height = int((original_height / original_width) * new_width)
            resized_image = image.resize((new_width, new_height))
            resized_width, resized_height = resized_image.size
            print(f"Original image dimensions: {original_width}x{original_height} pixels")
            print(f"Resized image dimensions: {resized_width}x{resized_height} pixels")
            image = resized_image
    
    def save_img(self, image):
        image.save('image_example.jpg')


    def add_quote(self, image, quote, author):
        draw = ImageDraw.Draw(image)
        font_quote = ImageFont.truetype('fonts/impact.ttf', size=30)
        font_author = ImageFont.truetype('fonts/impact.ttf', size=20)
        draw.text((40, 80), quote, font=font_quote, fill='white')
        draw.text((45, 115), '-' + author, font=font_author, fill='white')
        return image

    def make_meme(self, img_path, text, author):
        try:
            image = Image.open(img_path)
            self.resize_img(image)
            print('Starting to add quote...')
            self.add_quote(image, text, author)
            print('Saving image...')
            output_path = self.destination + '_meme.jpg'
            image.save(output_path)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return output_path
