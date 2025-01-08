import hashlib

def calculate_hash(file_path, algorithm="sha256"):
    hash_func = getattr(hashlib, algorithm)()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

if __name__ == "__main__":
    file_path = "C:/Users/SIBIRAJ B/OneDrive/Documents/soundarrr/disk_image.jpeg"

    print(f"SHA256: {calculate_hash(file_path)}")
