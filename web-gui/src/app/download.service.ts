import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DownloadService {

  readonly base = 'http://0.0.0.0:5000/youtube-dl';

  constructor(private httpClient: HttpClient) { }

  getFile(name: string): Promise<HttpResponse<Blob>> {
    return this.httpClient.get(this.base + '/file' + `/${name}`,
      { responseType: 'blob', observe: 'response' }).toPromise();
  }

  getFiles(names: string[]): Promise<HttpResponse<Blob>> {
    if (names.length === 1) {
      return this.getFile(names[0]);
    } else {
      return this.httpClient.post(this.base + '/files', names,
        { responseType: 'blob', observe: 'response' }).toPromise();
    }
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
