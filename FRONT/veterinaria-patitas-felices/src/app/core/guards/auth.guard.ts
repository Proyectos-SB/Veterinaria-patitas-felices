import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { map, take } from 'rxjs/operators';
import { Observable } from 'rxjs';

  export const authGuard: CanActivateFn = (route, state): => {
    const authService = inject(AuthService);
    const router = inject(Router);
  
    return authService.authStatus$.pipe(
      take(1), // Tomamos el último valor y completamos
      map(isAuthenticated => {
        if (isAuthenticated) {
          return true;
        } else {
          router.navigate(['/login']);
          return false;
        }
      })
    );
  };
