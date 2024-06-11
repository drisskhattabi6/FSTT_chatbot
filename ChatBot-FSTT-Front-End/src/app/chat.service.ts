import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, map } from 'rxjs';
import { Message } from './message';

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  private apiUrl = 'http://localhost:8500/query'; // Replace with your API URL
  private modelUrl = 'http://localhost:8500/model';
  private modelSubject = new BehaviorSubject<string>('');
  model$ = this.modelSubject.asObservable();

  setModel(model: string) {
    this.modelSubject.next(model);
  }
  constructor(private http: HttpClient) { }
  loadModel(model: string): Observable<Boolean> {
    this.setModel(model)
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = { model: model };

    return this.http.post<{ response: boolean }>(this.modelUrl, body, { headers })
      .pipe(
        map(response => {
          return response.response
        })
      );
  }

  sendMessage(message: string): Observable<Message> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = { prompt: message };

    return this.http.post<{ response: string }>(this.apiUrl, body, { headers })
      .pipe(
        map(response => {
          return {
            user: 'Bot',
            text: response.response
          };
        })
      );
  }


}
