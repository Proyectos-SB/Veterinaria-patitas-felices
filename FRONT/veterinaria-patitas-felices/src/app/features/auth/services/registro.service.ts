import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError, Observable, tap, throwError } from 'rxjs';
import { Usuario } from '../models/usuario.model';
import { RegistroResponse } from '../models/registroResponse.model';
@Injectable({
  providedIn: 'root'
})
export class RegistroService {
  private REGISTRO_URL = 'http://localhost:8000/api/usuarios/registro/';

  constructor(private http: HttpClient) {}

  registrarUsuario(usuario: Usuario): Observable<RegistroResponse> {
    return this.http.post<RegistroResponse>(this.REGISTRO_URL, usuario).pipe(
      tap((response: RegistroResponse) => {
        console.log('Registro exitoso', response);
      }),
      catchError(error => {
        console.error("Login error:", error);
        return throwError(() => new Error(error.message || "Error en el login"))
      })
    );
  }
}