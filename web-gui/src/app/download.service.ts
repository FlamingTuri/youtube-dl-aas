import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { UrlBuilder } from 'http-url-builder';

@Injectable({
  providedIn: 'root'
})
export class DownloadService {

  readonly base = new UrlBuilder('http://0.0.0.0:5000/youtube-dl');

  constructor(private httpClient: HttpClient) { }

  getFile(name: string): Promise<HttpResponse<Blob>> {
    const url = this.base.addPath('file')
      .addPath(name)
      .build()
    return this.httpClient.get(url, { responseType: 'blob', observe: 'response' }).toPromise();
  }

  getFiles(names: string[]): Promise<HttpResponse<Blob>> {
    if (names.length === 1) {
      return this.getFile(names[0]);
    } else {
      const url = this.base.addPath('files').build()
      return this.httpClient.post(url, names, { responseType: 'blob', observe: 'response' }).toPromise();
    }
  }

  download(urls: string[]): Promise<HttpResponse<Blob>> {
    const url = this.base.addPath('download-and-send').build()
    const body = {
      'urls': urls,
      'temporary': true
    }
    return this.httpClient.post(url, JSON.stringify(body), {
      headers : new HttpHeaders({ 'Content-Type': 'application/json' }),
      responseType: 'blob',
      observe: 'response'
    }).toPromise();
  }

  getFileNameFromHeaders(headers: HttpHeaders): string {
    const contenDisposition = headers.get('content-disposition');
    if (contenDisposition === null) {
      return 'unknown';
    }
    // https://stackoverflow.com/a/23054920/7380828
    const fileName = contenDisposition.match(/filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/);
    return fileName === null ? 'unknown' : fileName[1];
  }
}
