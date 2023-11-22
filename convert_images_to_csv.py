import os
import csv

def convert_images_to_csv(image_folder, csv_file_path):
    image_paths = []
    labels = []

    for root, _, files in os.walk(image_folder):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                image_path = os.path.join(root, file)
                label = os.path.basename(root)  # Assuming labels are based on folder names

                image_paths.append(image_path)
                labels.append(label)

    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['image_path', 'label'])

        for i in range(len(image_paths)):
            writer.writerow([image_paths[i], labels[i]])