import { Component } from '@angular/core';
import { DocService } from 'src/app/services/doc/doc.service';

@Component({
  selector: 'app-doc-dialog',
  templateUrl: './doc-dialog.component.html',
  styleUrls: ['./doc-dialog.component.scss']
})
export class DocDialogComponent {

  youtubeDlDoc: string = '';

  constructor(private docService: DocService) {
    docService.getYoutubeDlDoc().then(result => this.youtubeDlDoc = result.content);
  }

}
