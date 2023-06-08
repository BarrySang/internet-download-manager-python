# imports
import os
import requests

class Downloader:
    def __init__(self, url, save_filename):
        self.url = url
        self.save_filename = save_filename

    def download_file(self):
        #set the save path
        save_path = "downloads/" + self.save_filename

        # set a default file size of 0
        file_size = 0

        # check if the file already exists
        if os.path.exists(save_path):
            file_size = os.path.getsize(save_path)

        # get byte range to resume download from
        headers = {'Range': f'bytes={file_size}-'}

        # send http request
        response = requests.get(self.url, headers=headers, stream=True)

        # raise an exception in case of an error
        response.raise_for_status()

        # open the file in append mode
        with open(save_path, 'wb') as file:
            # write downloaded data to the download file in chunks
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print("File downloaded successfully.")