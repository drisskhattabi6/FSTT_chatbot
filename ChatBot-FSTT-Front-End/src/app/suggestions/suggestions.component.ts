import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Output } from '@angular/core';
import {MatChipsModule} from '@angular/material/chips';
@Component({
  selector: 'app-suggestions',
  standalone: true,
  imports: [CommonModule, MatChipsModule],
  templateUrl: './suggestions.component.html',
  styleUrl: './suggestions.component.css'
})
export class SuggestionsComponent {
  @Output() question = new EventEmitter<string>();

  questions: string[] = [
    'Quels programmes sont offerts à la FSTT ?',
    'Comment puis-je postuler à la FSTT ?',
    'Quelles sont les conditions d\'admission à la FSTT ?',
    'Quels sont les frais de scolarité pour les programmes de la FSTT ?',
    'Puis-je obtenir une aide financière ou des bourses à la FSTT ?',
    'Où se trouve la FSTT ?',
    'Quelles sont les opportunités de recherche à la FSTT ?',
    'Qui puis-je contacter pour plus d\'informations ?'
  ];

  onChipClick(question: string) {
    this.question.emit(question);
  }
  
}
