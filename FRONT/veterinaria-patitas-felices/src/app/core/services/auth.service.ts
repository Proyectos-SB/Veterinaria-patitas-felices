import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, tap, throwError, BehaviorSubject,switchMap } from 'rxjs';
import { Router } from '@angular/router';
import { LoginRequest } from '../../features/auth/models/loginRequest.model';
import { LoginResponse } from '../../features/auth/models/loginResponse.model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private LOGIN_URLs = 'http://localhost:8000/api/usuarios/login/';
  private REFRESH_URL = 'http://localhost:8000/api/usuarios/token/refresh/';
  private tokenKey = 'authToken';
  private refreshKey = 'refreshToken';

  private authStatusSubject = new BehaviorSubject<boolean>(this.hasToken());
  public authStatus$ = this.authStatusSubject.asObservable();

  constructor(private http: HttpClient, private router: Router) {}

  login(usuario: LoginRequest): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(this.LOGIN_URLs, usuario).pipe(
      tap(response => {
        if (response.access && response.refresh) {
          this.setToken(response.access);
          this.setRefreshToken(response.refresh);
          this.authStatusSubject.next(true);  // 🔥 Notifica que está autenticado
        } else {
          console.error("Error en la autenticación");
        }
      }),
      catchError(error => {
        console.error("Error en el login:", error);
        return throwError(() => new Error(error.message || "Error en el login"));
      })
    );
  }

  refreshToken(): Observable<string> {
    const refresh = localStorage.getItem(this.refreshKey);
    if (!refresh) {
      this.logOut();
      return throwError(() => new Error("No hay token de refresco"));
    }

    return this.http.post<{ access: string }>(this.REFRESH_URL, { refresh }).pipe(
      tap(response => {
        if (response.access) {
          this.setToken(response.access);  // 🔥 Guarda el nuevo token en localStorage
          console.log("Token renovado exitosamente");
        }
      }),
      catchError(error => {
        console.error("Error al refrescar el token:", error);
        this.logOut();  // 🔥 Si falla, forzar logout
        return throwError(() => new Error(error.message || "Error al renovar el token"));
      }),
      switchMap(response => {
        return new Observable<string>(observer => {
          observer.next(response.access);
          observer.complete();
        });
      })
    );
  }

  logOut(): void {
    localStorage.removeItem(this.tokenKey);
    localStorage.removeItem(this.refreshKey);  // 🔥 Elimina el refresh token
    this.authStatusSubject.next(false);  // 🔥 Notifica que está deslogueado
    this.router.navigate(['/login']);
  }

  private setToken(access: string): void {
    localStorage.setItem(this.tokenKey, access);
  }

  private setRefreshToken(refresh: string): void {
    localStorage.setItem(this.refreshKey, refresh);
  }

  public getToken(): string | null {
    return localStorage.getItem(this.tokenKey);
  }

  private hasToken(): boolean {
    return !!this.getToken();
  }
}
