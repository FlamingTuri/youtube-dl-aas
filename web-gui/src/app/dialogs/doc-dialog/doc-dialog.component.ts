import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-doc-dialog',
  templateUrl: './doc-dialog.component.html',
  styleUrls: ['./doc-dialog.component.scss']
})
export class DocDialogComponent implements OnInit {

  youtubeDlDoc: string = '';

  constructor() { }

  ngOnInit(): void {
  }

}
