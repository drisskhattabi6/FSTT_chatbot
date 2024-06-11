import { Component, Input, OnInit } from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatToolbarModule} from '@angular/material/toolbar';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ChatService } from '../chat.service';
import { LoadingService } from '../loading.service';
import { MatCommonModule } from '@angular/material/core';
import {MatMenuModule} from '@angular/material/menu';
@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule,MatMenuModule,MatToolbarModule, MatToolbarModule, MatButtonModule, MatIconModule, RouterModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent implements OnInit{
  @Input() model: string = "";
  constructor(private loadingService: LoadingService,private chatService : ChatService,private route: ActivatedRoute){}
  ngOnInit(): void {
    this.chatService.model$.subscribe(model => {
      this.model = model;
      console.log(this.model);
    });
  }

  selectModel(model: string) {
    this.loadingService.loadingOn();
    this.chatService.loadModel(model).subscribe(() => {
      this.loadingService.loadingOff();
    });
  }


}
