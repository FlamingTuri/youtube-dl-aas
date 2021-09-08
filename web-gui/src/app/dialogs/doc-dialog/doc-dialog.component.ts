import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-doc-dialog',
  templateUrl: './doc-dialog.component.html',
  styleUrls: ['./doc-dialog.component.scss']
})
export class DocDialogComponent {

  constructor(@Inject(MAT_DIALOG_DATA) public youtubeDlDoc: string) {
  }

}
