import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UrlBuilder } from 'http-url-builder';

@Injectable({
  providedIn: 'root'
})
export class DocService {

  private readonly base = new UrlBuilder('http://0.0.0.0:5000/youtube-dl');

  constructor(private httpClient: HttpClient) { }

  getYoutubeDlDoc(): Promise<any> {
    const url = this.base.addPath('doc').build()
    return this.httpClient.get(url).toPromise();
  }

}
