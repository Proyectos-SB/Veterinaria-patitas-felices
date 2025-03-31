import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Articulo } from '../articulos/model/articulo.model';


@Injectable({
  providedIn: 'root'
})
export class ArticuloService {
  private apiUrl = 'http://localhost:8000/api/articulos/'; //
  constructor(private http: HttpClient) {}

  obtenerArticulos(): Observable<Articulo[]> {
    return this.http.get<Articulo[]>(this.apiUrl);
  }

  obtenerArticuloPorId(id: number): Observable<Articulo> {
    return this.http.get<Articulo>(`${this.apiUrl}${id}/`);
  }

  
}
