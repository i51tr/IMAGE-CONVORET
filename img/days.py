from PIL import Image

def convert_image_to_ascii(image_path, color='green'): 
    # Define the ASCII characters to represent different pixel brightness 
    ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
    
    if color == "green":
        # If color is set to white, use reversed ASCII characters to give a white-on-black effect 
        ascii_chars = ascii_chars[::-1]
    
    # Load the image and resize it to the desired width
    img = Image.open(image_path)
    width, height = img.size
    new_width = 80 
    new_height = int((float(height) / float(width)) * new_width) 
    img = img.resize((new_width, new_height))
    img = img.convert('L')  # Convert image to grayscale

    # Convert each pixel to ASCII representation
    ascii_image = ''
    for y in range(new_height):
        for x in range(new_width):
            pixel = img.getpixel((x, y)) 
            brightness = 255 - pixel 
            ascii_image += ascii_chars[brightness // 25] 
        ascii_image += '\n' 
        
    return ascii_image


# Example usage 
image_path = 'slo.webp'
ascii_image = convert_image_to_ascii(image_path, color='green') 
print(ascii_image)

   
