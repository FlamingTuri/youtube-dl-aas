import { UrlBuilder } from 'http-url-builder';

export class Api {
  
  static readonly protocol = window.location.protocol;
  static readonly hostname = window.location.hostname;
  static readonly port = window.location.port;
  static readonly baseUrl =`${Api.protocol}//${Api.hostname}:${Api.port}/youtube-dl`
  static readonly base = new UrlBuilder(Api.baseUrl);
}