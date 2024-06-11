import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from "./header/header.component";
import { ChatComponent } from "./chat/chat.component";
import {MatGridListModule} from '@angular/material/grid-list';
import { LoadingindicatorComponent } from "./loadingindicator/loadingindicator.component";
@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.css',
    imports: [CommonModule, RouterOutlet, HeaderComponent, ChatComponent, MatGridListModule, LoadingindicatorComponent]
})
export class AppComponent {
  title = 'FSTT Chat';
}
