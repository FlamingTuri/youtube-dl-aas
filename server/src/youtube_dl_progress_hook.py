class YoutubeDlProgressHook:

    download_prefix = '[download] Destination: '

    def progress_hook(self, d):
        status = d['status']
        print(status)
        if status == 'finished':
            print(d['filename'])
            self.download_file_location = d['filename']

    def get_download_file_location(self):
        return self.download_file_location
