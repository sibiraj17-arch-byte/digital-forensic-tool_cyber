import os

def create_disk_image(disk_path, output_file):
    with open(disk_path, 'rb') as source, open(output_file, 'wb') as target:
        while chunk := source.read(1024 * 1024):  # Read in 1MB chunks
            target.write(chunk)
    print(f"Disk image saved to {output_file}")

if __name__ == "__main__":
   create_disk_image("C:/Users/SIBIRAJ B/OneDrive/Documents/soundarrr/disk_image.jpeg", "disk_image.jpeg")
 # Replace with your disk path
