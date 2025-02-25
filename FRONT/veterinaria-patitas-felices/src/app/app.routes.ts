import { Routes } from '@angular/router';
import { LandingComponent } from './pages/landing/landing.component';
import { RegistroComponent } from './features/auth/registro/registro.component';
import { LoginComponent } from './features/auth/login/login.component';
import { DashboardPrincipalComponent } from './features/dashboard/dashboard-principal/dashboard-principal.component';
import { authGuard } from './core/guards/auth.guard';

export const routes: Routes = [
    {path: "index", component: LandingComponent},
    {path: "registro", component: RegistroComponent},
    {path: "login", component: LoginComponent},
    {path:"dashboard", component: DashboardPrincipalComponent,canActivate: [authGuard]},
    {path:"", redirectTo:"/index", pathMatch:"full"},
    
    

    
];
