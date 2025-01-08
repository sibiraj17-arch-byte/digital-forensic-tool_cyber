from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        if exif_data:
            metadata = {TAGS.get(tag, tag): value for tag, value in exif_data.items()}
            return metadata
        else:
            print("No metadata found.")
    except Exception as e:
        print(f"Error extracting metadata: {e}")

if __name__ == "__main__":
    metadata = extract_metadata("recovered_files/recovered_0.jpg")
    print(metadata)
