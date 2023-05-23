import requests
import random
import string
import threading
import os
import uuid

def generate_random_file(file_size):
    unique_filename = str(uuid.uuid4())  # Generate a unique filename
    content = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size))
    with open(unique_filename, 'w') as file:
        file.write(content)
    return unique_filename

def upload_file(url, file_path):
    try:
        with open(file_path, 'rb') as file:
            response = requests.post(url, files={'file': file})
            response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
            print(f'File uploaded successfully: {file_path}')
    except requests.exceptions.RequestException as e:
        print(f'File upload failed: {e}')

    # Delete the file after upload
    os.remove(file_path)
    print(f'File deleted: {file_path}')

def upload_files(url, num_uploads, file_size):
    for _ in range(num_uploads):
        # Generate a random file
        file_path = generate_random_file(file_size)

        # Upload the file
        upload_file(url, file_path)

if __name__ == '__main__':
    url = 'https://footballreview.altervista.org/tpsit/upload.php';
    num_uploads = 1
    file_size = 10000000

    threads = []
    for _ in range(num_uploads):
        t = threading.Thread(target=upload_files, args=(url, 1, file_size))
        t.start()
        threads.append(t)

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print('All files uploaded and deleted successfully!')
