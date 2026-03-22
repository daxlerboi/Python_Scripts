from PIL import Image
import os

def reduce_png_size(input_path, output_path, max_size_mb=1):
    max_size_bytes = max_size_mb * 1024 * 1024
    img = Image.open(input_path)

    # Try saving with optimization first
    img.save(output_path, optimize=True)

    # Check file size
    filesize = os.path.getsize(output_path)
    
    # If still larger than max size, resize proportionally
    if filesize > max_size_bytes:
        width, height = img.size
        scale_factor = 0.9  # reduce by 10% at a time
        while filesize > max_size_bytes:
            width = int(width * scale_factor)
            height = int(height * scale_factor)
            img_resized = img.resize((width, height), Image.Resampling.LANCZOS)
            img_resized.save(output_path, optimize=True)
            filesize = os.path.getsize(output_path)

    print(f"Reduced image saved to {output_path} ({filesize/1024:.2f} KB)")

# Example usage
input_file = "/mnt/c/Users/daxle/OneDrive/Desktop/Py/img.png"
output_file = "/mnt/c/Users/daxle/OneDrive/Desktop/Py/img.png"

reduce_png_size(input_file, output_file)
