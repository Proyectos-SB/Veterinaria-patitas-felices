import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LoginRequest } from '../../features/auth/models/loginRequest.model';
import { catchError, Observable, tap ,throwError,BehaviorSubject} from 'rxjs';
import { Router } from '@angular/router';
import { LoginResponse } from '../../features/auth/models/loginResponse.model';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private LOGIN_URLs = 'http://localhost:8000/api/usuarios/login/';
  private tokenKey = 'authToken';
  private authStatusSubject = new BehaviorSubject<boolean>(this.hasToken());
  public authStatus$ = this.authStatusSubject.asObservable();
     
  constructor(private http: HttpClient,private router: Router) {}

  login(usuario: LoginRequest): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(this.LOGIN_URLs, usuario).pipe(
      tap(response => {
        if (response) {
          console.log(response.access);
          console.log(response.refresh);
          console.log('El Logeo fue un éxito');
          this.setToken(response.access);
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


  private setToken(access: string): void {
  localStorage.setItem(this.tokenKey, access);
}
  private getToken(): string | null {
    return localStorage.getItem(this.tokenKey); 
  }
  getAuthHeaders(): { headers: HttpHeaders } {
    const token = this.getToken();
    return {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      })
    };
  }
  private hasToken(): boolean {
    return !!this.getToken();
  }
  
  // Devuelve el estado de autenticación como Observable
  isAuthenticated(): Observable<boolean> {
    return this.authStatus$;
  }
  logOut(): void {
    localStorage.removeItem(this.tokenKey);
    this.router.navigate(['/login']);
  } 
}
