class YoutubeDlProgressHook:

    download_locations = []
    download_prefix = '[download] Destination: '

    def progress_hook(self, d):
        status = d['status']
        print(status)
        if status == 'finished':
            print(d['filename'])
            self.download_file_location = d['filename']
            self.download_locations.append(d['filename'])

    def get_downloaded_files_locations(self):
        return self.download_locations
