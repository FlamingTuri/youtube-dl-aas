import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DownloadService {

  readonly base = 'http://0.0.0.0:5000/youtube-dl';

  constructor(private httpClient: HttpClient) { }

  download(name: string) {
    return this.httpClient.get(this.base + '/file' + `/${name}`).toPromise();
  }
}
