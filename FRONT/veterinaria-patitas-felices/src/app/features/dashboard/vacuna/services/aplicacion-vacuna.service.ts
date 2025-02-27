import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AplicacionVacunaService {

  private apiUrl = 'http://localhost:8000/api/aplicacion-vacunas/'; // Cambia la URL si es necesario

  constructor(private http: HttpClient) { }

  createAplicacionVacuna(data: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }
}