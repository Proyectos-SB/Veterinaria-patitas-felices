import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VacunaService {

  private apiUrl = 'http://localhost:8000/api/vacunas/'; // Cambia la URL si es necesario

  constructor(private http: HttpClient) { }

  getVacunas(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }
}