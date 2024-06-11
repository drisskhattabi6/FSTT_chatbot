import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatIcon, MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { Message } from '../message';
import { MessageComponent } from "../message/message.component";
import { MatGridListModule } from '@angular/material/grid-list';
import { ChatService } from '../chat.service';
import { SuggestionsComponent } from "../suggestions/suggestions.component";
import { ActivatedRoute } from '@angular/router';
@Component({
    selector: 'app-chat',
    standalone: true,
    templateUrl: './chat.component.html',
    styleUrl: './chat.component.css',
    imports: [FormsModule, CommonModule, MatInputModule, MatIconModule, MessageComponent, MatGridListModule, SuggestionsComponent]
})
export class ChatComponent implements OnInit {

 /* message: string | undefined;
  messages: string[] = [];
*/
  constructor(private chatService: ChatService) { }

  ngOnInit() {
  }

  messages: Message[] = [
    {user: "Bot" ,text: "Bonjour , je suis FSTT Chat un chat debier a vous aider"}
  ];
  showSuggestions: boolean = true;
  newMessage: string = '';
  username: string = 'User';  // In a real app, this should be dynamically set

  sendMessage() {
    if (this.newMessage.trim().length === 0) {
      return;
    }
    this.hideSuggestions()
    // Send the message to the API
    this.chatService.sendMessage(this.newMessage).subscribe(botMessage => {
      this.messages.push(botMessage);
    });
    this.messages.push({user: 'User', text: this.newMessage});
    this.newMessage = '';
  }
  hideSuggestions() {
    this.showSuggestions = false;
  }
  handleQuestion(question: string) {
    this.newMessage = question
    this.sendMessage()
  }
  }
