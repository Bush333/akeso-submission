from tqdm import tqdm
import tarfile
import zipfile
import requests
import os

def download_file(url, destination):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(destination, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()

    if total_size != 0 and progress_bar.n != total_size:
        print("ERROR: Something went wrong")
    else:
        print(f"Downloaded {destination}")

def extract_dataset(file_path, extract_to):
    if file_path.endswith("tar.gz"):
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(path=extract_to)
    elif file_path.endswith("zip"):
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)
    else:
        print("Unknown file format:", file_path)



def main():
    urls = {
        "MPIIGaze": "http://datasets.d2.mpi-inf.mpg.de/MPIIGaze/MPIIGaze.tar.gz",
        "MPIIFaceGaze": "http://datasets.d2.mpi-inf.mpg.de/MPIIGaze/MPIIFaceGaze.zip"
    }

    download_directory = "datasets"
    os.makedirs(download_directory, exist_ok=True)

    for dataset_name, url in urls.items():
        destination = os.path.join(download_directory, os.path.basename(url))
        print(f"Downloading {dataset_name} from {url}...")
        download_file(url, destination)
        print(f"Downloaded {dataset_name} to {destination}")
    
    # Extract data
    # Paths to downloaded datasets
    mpiigaze_path = 'datasets/MPIIGaze.tar.gz'
    mpiifacegaze_path = 'datasets/MPIIFaceGaze.zip'

    # Extract datasets
    extract_dataset(mpiigaze_path, 'datasets/MPIIGaze')
    extract_dataset(mpiifacegaze_path, 'datasets/MPIIFaceGaze')

if __name__ == "__main__":
    main()
