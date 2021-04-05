import { Injectable } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ErrorDialogComponent } from 'src/app/dialogs/error-dialog/error-dialog.component';
import { OptionsDialogComponent } from 'src/app/dialogs/options-dialog/options-dialog.component';

@Injectable({
  providedIn: 'root'
})
export class DialogService {

  constructor(private dialog: MatDialog) { }

  openErrorDialog(error: Error) {
    const dialogRef = this.dialog.open(ErrorDialogComponent, {
      data: error
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  openOptionsDialog() {
    const dialogRef = this.dialog.open(OptionsDialogComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }
}
