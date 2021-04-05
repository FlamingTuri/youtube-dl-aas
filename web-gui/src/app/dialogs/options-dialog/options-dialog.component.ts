import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { DialogService } from 'src/app/services/dialog/dialog.service';

@Component({
  selector: 'app-options-dialog',
  templateUrl: './options-dialog.component.html',
  styleUrls: ['./options-dialog.component.scss']
})
export class OptionsDialogComponent {

  youtubeDlOptions: string;

  constructor(
    public dialogRef: MatDialogRef<OptionsDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public ydlOpts: Map<string, string | number>,
    private dialogService: DialogService) {
    const ydlOptsObj = Object.fromEntries(ydlOpts);
    this.youtubeDlOptions = JSON.stringify(ydlOptsObj, null, 2);
  }

  apply() {
    try {
      const newYdlOpts = new Map(Object.entries(JSON.parse(this.youtubeDlOptions)))
      this.dialogRef.close(newYdlOpts);
    } catch (error) {
      this.dialogService.openErrorDialog(error as Error);
    }
  }
}
