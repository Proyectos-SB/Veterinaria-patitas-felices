import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LoginRequest } from '../../features/auth/models/loginRequest.model';
import { catchError, Observable, tap ,throwError} from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private LOGIN_URLs = 'http://localhost:3000/login';
  private tokenKey = 'authToken';
     
  constructor(private http: HttpClient,private router: Router) {}

  login(usuario: LoginRequest): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(this.LOGIN_URLs, usuario).pipe(
      tap(response => {
        if (response.token) {
          console.log(response.token);
          console.log('El Logeo fue un éxito');
          this.setToken(response.token);
        } else {
          console.error("Authentication failed");
        }
      }),
      catchError(error => {
        console.error("Login error:", error);
        return throwError(() => new Error(error.message || "Error en el login"));
      })
    );
  }

  private setToken(token: string): void {
    localStorage.setItem(this.tokenKey, token);
  }
  private getToken(): string | null {
    return localStorage.getItem(this.tokenKey); 
  }
  isAuthenticated(): boolean {
    return !!this.getToken(); // Devuelve true si hay token, false si no
  }
  logOut(): void {
    localStorage.removeItem(this.tokenKey);
    this.router.navigate(['/login']);
  } 
}
