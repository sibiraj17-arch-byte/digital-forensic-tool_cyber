import os

def recover_files(disk_image, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Example: Recover deleted .jpg files
    with open(disk_image, 'rb') as disk:
        data = disk.read()
        start = 0
        while (start := data.find(b'\xff\xd8', start)) != -1:  # JPEG magic number
            end = data.find(b'\xff\xd9', start)
            if end == -1:
                break
            end += 2
            recovered_file = os.path.join(output_dir, f"recovered_{start}.jpg")
            with open(recovered_file, 'wb') as out:
                out.write(data[start:end])
            print(f"Recovered: {recovered_file}")
            start = end

if __name__ == "__main__":
    recover_files("disk_image.jpeg", "recovered_files")
