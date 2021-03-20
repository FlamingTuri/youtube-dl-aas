import { HttpResponse } from '@angular/common/http';
import { Component } from '@angular/core';
import { saveAs } from 'file-saver';
import { DownloadService } from './download.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  urls: string[] = [
    'url1',
    'url2'
  ];

  constructor(private downloadService: DownloadService) { }

  download() {
    let response: Promise<HttpResponse<Blob>>;
    if (this.urls.length === 1) {
      const url = this.urls[0];
      response = this.downloadService.getFile(url);
    } else {
      response = this.downloadService.getFiles(this.urls)
    }
    response.then(response => this.promptSaveData(response));
  }

  promptSaveData(response: HttpResponse<Blob>) {
    const fileName = this.downloadService.getFileNameFromHeaders(response.headers)
    const data = response.body;
    if (data !== null) {
      saveAs(data, fileName)
    }
  }
}
