import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-options-dialog',
  templateUrl: './options-dialog.component.html',
  styleUrls: ['./options-dialog.component.scss']
})
export class OptionsDialogComponent {

  youtubeDlOptions: string;

  constructor(
    public dialogRef: MatDialogRef<OptionsDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public ydlOpts: Map<string, string | number>) {
    const ydlOptsObj = Object.fromEntries(ydlOpts);
    this.youtubeDlOptions = JSON.stringify(ydlOptsObj, null, 2);
  }

  apply() {
    this.dialogRef.close(new Map(Object.entries(JSON.parse(this.youtubeDlOptions))));
  }
}
