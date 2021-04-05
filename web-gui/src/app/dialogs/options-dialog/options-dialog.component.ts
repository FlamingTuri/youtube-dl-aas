import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-options-dialog',
  templateUrl: './options-dialog.component.html',
  styleUrls: ['./options-dialog.component.scss']
})
export class OptionsDialogComponent {

  youtubeDlOptions: string;

  constructor(@Inject(MAT_DIALOG_DATA) public ydlOpts: Map<string, string | number>) {
    const ydlOptsObj = Object.fromEntries(ydlOpts);
    this.youtubeDlOptions = JSON.stringify(ydlOptsObj, null, 2);
  }

}
