import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { map } from 'rxjs/operators';

export const authenticatedGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService);
  const router = inject(Router);

  return authService.authStatus$.pipe(
    map(isAuth => {
      if (isAuth) {
        router.navigate(['/dashboard']); // Redirige si ya está autenticado
        return false;
      }
      return true; // Permite acceso si NO está autenticado
    })
  );
};

