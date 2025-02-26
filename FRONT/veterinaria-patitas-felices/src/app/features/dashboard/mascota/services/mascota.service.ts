import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Mascota {
  id?: number;
  nombre: string;
  raza: string;
  edad: number;
  sexo: string;
  tipo: number; // ID del tipo de mascota
}

@Injectable({
  providedIn: 'root',
})
export class MascotaService {
  private apiUrl = 'http://localhost:8000/api/mascotas/';

  constructor(private http: HttpClient) {}

  getMascotas(): Observable<Mascota[]> {
    return this.http.get<Mascota[]>(this.apiUrl);
  }

  createMascota(mascota: Mascota): Observable<Mascota> {
    return this.http.post<Mascota>(this.apiUrl, mascota);
  }

  updateMascota(id: number, mascota: Mascota): Observable<Mascota> {
    return this.http.put<Mascota>(`${this.apiUrl}${id}/`, mascota);
  }

  deleteMascota(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }
}
