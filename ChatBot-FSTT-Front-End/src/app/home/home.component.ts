import { Component } from '@angular/core';
import { ChatComponent } from "../chat/chat.component";
import { LoadingindicatorComponent } from '../loadingindicator/loadingindicator.component';

@Component({
    selector: 'app-home',
    standalone: true,
    templateUrl: './home.component.html',
    styleUrl: './home.component.css',
    imports: [ChatComponent,LoadingindicatorComponent]
})
export class HomeComponent {

}
