import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Api } from 'src/app/services/api';

@Injectable({
  providedIn: 'root'
})
export class VersionService {

  constructor(private httpClient: HttpClient) { }

  getVersion(): Promise<any> {
    const url = Api.base.addPath('version').build()
    return this.httpClient.get(url).toPromise();
  }
}
