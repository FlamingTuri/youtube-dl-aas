import { Injectable } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { DocDialogComponent } from 'src/app/dialogs/doc-dialog/doc-dialog.component';
import { ErrorDialogComponent } from 'src/app/dialogs/error-dialog/error-dialog.component';
import { MultipleDownloadsDialogComponent } from 'src/app/dialogs/multiple-downloads-dialog/multiple-downloads-dialog.component';
import { OptionsDialogComponent } from 'src/app/dialogs/options-dialog/options-dialog.component';

@Injectable({
  providedIn: 'root'
})
export class DialogService {

  private readonly defaultWidth = '60%';
  private readonly defaultHeight = '80%';

  constructor(private dialog: MatDialog) { }

  openErrorDialog(error: Error) {
    console.error(error);
    this.dialog.open(ErrorDialogComponent, {
      data: error
    });
  }

  openOptionsDialog(ydlOpts: Map<string, string | number>): Promise<Map<string, string | number>> {
    const dialogRef = this.dialog.open(OptionsDialogComponent, {
      width: this.defaultWidth,
      height: this.defaultHeight,
      data: ydlOpts
    });

    return dialogRef.afterClosed().toPromise();
  }

  openYoutubeDlDocsDialog(ydlDocs: string): void {
    this.dialog.open(DocDialogComponent, {
      width: this.defaultWidth,
      height: this.defaultHeight,
      data: ydlDocs
    });
  }

  openMultipleDownloadDialog(urls: string[]): Promise<string[]>  {
    const dialogRef = this.dialog.open(MultipleDownloadsDialogComponent, {
      width: this.defaultWidth,
      height: this.defaultHeight,
      data: urls
    });

    return dialogRef.afterClosed().toPromise();
  }
}
