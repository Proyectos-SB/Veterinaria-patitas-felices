import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Usuario } from '../../features/auth/models/usuario.model';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';
import { RegistroResponse } from '../../features/auth/models/registroResponse.model';
import { UsuarioInterface } from '../../features/auth/models/usuarioInterface.model';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {
  private baseUrl = 'http://localhost:8000/api/usuarios'; 

  constructor(private http: HttpClient, private authService: AuthService) {}



  // Obtener datos del usuario autenticado
  getUsuario(): Observable<UsuarioInterface> {
    return this.http.get<UsuarioInterface>(`${this.baseUrl}/me/`)}

  // Actualizar datos del usuario
  updateUsuario(data: Partial<Usuario>): Observable<RegistroResponse> {
    return this.http.put<RegistroResponse>(`${this.baseUrl}/me/editar/`, data );
  }
}