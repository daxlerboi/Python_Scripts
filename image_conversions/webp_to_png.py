from PIL import Image

# Open the WebP image
webp_image = Image.open("/mnt/c/Users/daxle/OneDrive/Desktop/Py/img.webp")
# Convert and save as PNG
webp_image.save("/mnt/c/Users/daxle/OneDrive/Desktop/Py/img.png", "PNG")

print("Conversion completed!")
