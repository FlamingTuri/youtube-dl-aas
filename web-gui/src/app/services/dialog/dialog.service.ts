import { Injectable } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { DocDialogComponent } from 'src/app/dialogs/doc-dialog/doc-dialog.component';
import { ErrorDialogComponent } from 'src/app/dialogs/error-dialog/error-dialog.component';
import { OptionsDialogComponent } from 'src/app/dialogs/options-dialog/options-dialog.component';

@Injectable({
  providedIn: 'root'
})
export class DialogService {

  constructor(private dialog: MatDialog) { }

  openErrorDialog(error: Error) {
    console.error(error);
    this.dialog.open(ErrorDialogComponent, {
      data: error
    });
  }

  openOptionsDialog(ydlOpts: Map<string, string | number>): Promise<Map<string, string | number>> {
    const dialogRef = this.dialog.open(OptionsDialogComponent, {
      width: '60%',
      height: '80%',
      data: ydlOpts
    });

    return dialogRef.afterClosed().toPromise();
  }

  openYoutubeDlDocsDialog(ydlDocs: string): void {
    this.dialog.open(DocDialogComponent, {
      width: '60%',
      height: '80%',
      data: ydlDocs
    });
  }
}
