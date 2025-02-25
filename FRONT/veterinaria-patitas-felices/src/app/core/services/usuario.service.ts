import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Usuario } from '../../features/auth/models/usuario.model';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {
  private baseUrl = 'http://localhost:8000/api/usuarios'; 

  constructor(private http: HttpClient, private authService: AuthService) {}



  // Obtener datos del usuario autenticado
  getUsuario(): Observable<Usuario> {
    return this.http.get<Usuario>(`${this.baseUrl}/me/`, this.authService.getAuthHeaders());
  }

  // Actualizar datos del usuario
  updateUsuario(data: Partial<Usuario>): Observable<Usuario> {
    return this.http.put<Usuario>(`${this.baseUrl}/me/editar/`, data, this.authService.getAuthHeaders());
  }
}