import os
from disk_imaging import create_disk_image
from hash_verification import calculate_hash
from file_recovery import recover_files
from metadata_extraction import extract_metadata
from timeline_visualization import visualize_timeline

def main():
    disk_path = r"C:\Users\SIBIRAJ B\OneDrive\Documents\soundarrr\disk_image.jpeg"
    output_image = r"C:\Users\SIBIRAJ B\OneDrive\Documents\soundarrr\output_image.img"
    recovered_dir = r"C:\Users\SIBIRAJ B\OneDrive\Documents\soundarrr\recovered_files"

    
    print("Creating disk image...")
    create_disk_image(disk_path, output_image)
    
    print("Calculating hash...")
    file_hash = calculate_hash(output_image)
    print(f"Disk image hash: {file_hash}")
    
    print("Recovering files...")
    recover_files(output_image, recovered_dir)
    
    print("Extracting metadata...")
    events = []
    for file in os.listdir(recovered_dir):
        file_path = os.path.join(recovered_dir, file)
        metadata = extract_metadata(file_path)
        if metadata:
            print(f"Metadata for {file}: {metadata}")
            events.append({"timestamp": metadata.get("DateTime", "Unknown"), "action": f"Recovered {file}"})
    
    print("Visualizing timeline...")
    visualize_timeline(events)

if __name__ == "__main__":
    main()
