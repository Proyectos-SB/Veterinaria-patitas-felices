import { inject } from '@angular/core';
import { HttpEvent, HttpHandlerFn, HttpInterceptorFn, HttpRequest } from '@angular/common/http';
import { catchError, Observable, switchMap, throwError } from 'rxjs';
import { AuthService } from '../services/auth.service';

export const authInterceptor: HttpInterceptorFn = (req: HttpRequest<unknown>, next: HttpHandlerFn): Observable<HttpEvent<unknown>> => {
  const authService = inject(AuthService);
  const token = authService.getToken();

  // 🔹 Si no hay token, pasa la petición sin modificar
  if (!token) {
    return next(req);
  }

  // 🔹 Clonar la solicitud y agregar el encabezado de autorización con el token actual
  const authReq = req.clone({
    setHeaders: { Authorization: `Bearer ${token}` }
  });

  return next(authReq).pipe(
    catchError(error => {
      if (error.status === 401) {  // 🔥 Si es un error 401, intenta refrescar el token
        return authService.refreshToken().pipe(
          switchMap(newToken => {
            // 🔥 Clonar la solicitud original con el nuevo token
            const newAuthReq = req.clone({
              setHeaders: { Authorization: `Bearer ${newToken}` }
            });
            return next(newAuthReq);
          }),
          catchError(err => {
            console.error("Error al refrescar el token:", err);
            authService.logOut();
            return throwError(() => new Error("Sesión expirada. Debes volver a iniciar sesión."));
          })
        );
      }
      return throwError(() => error);
    })
  );
};
