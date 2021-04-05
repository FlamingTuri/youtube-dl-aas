import { Inject } from '@angular/core';
import { Component } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-error-dialog',
  templateUrl: './error-dialog.component.html',
  styleUrls: ['./error-dialog.component.scss']
})
export class ErrorDialogComponent {

  errorMessage: string

  constructor(@Inject(MAT_DIALOG_DATA) public data: any) {
    this.errorMessage = data.message;

    const error = data.error;
    if (error instanceof Blob) {
      this.parseErrorMessageFromBlob(error);
    }
  }

  parseErrorMessageFromBlob(error: Blob) {
    error.text().then(content => {
      const blobContentType = error.type;
      if (blobContentType === 'application/json') {
        this.errorMessage = JSON.parse(content).message;
      } else {
        console.warn(`no blob parser specified for ${blobContentType}`);
      }
    });
  }
}
