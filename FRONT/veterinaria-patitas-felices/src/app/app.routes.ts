import { Routes } from '@angular/router';
import { LandingComponent } from './pages/landing/landing.component';
import { RegistroComponent } from './features/auth/registro/registro.component';
import { LoginComponent } from './features/auth/login/login.component';
import { DashboardPrincipalComponent } from './features/dashboard/dashboard-principal/dashboard-principal.component';
import { authGuard } from './core/guards/auth.guard';
import { authenticatedGuard } from './core/guards/authenticated.guard';
import { PerfilComponent } from './features/dashboard/perfil/perfil.component';

export const routes: Routes = [
    {path: "index", component: LandingComponent},
    {path: "registro", component: RegistroComponent, canActivate: [authenticatedGuard]},
    {path: "login", component: LoginComponent, canActivate: [authenticatedGuard]},
    {path:"dashboard", component: DashboardPrincipalComponent,canActivate: [authGuard],canActivateChild:[authGuard]
        ,children:[
            {path:"perfil", component: PerfilComponent,},

            {path:"**", component: DashboardPrincipalComponent} //Si la ruta no coincide con ninguna de las anteriores, redireccionar al dashboard principal
    ]},
    {path:"", redirectTo:"/index", pathMatch:"full"},
    {path:"**", component: LandingComponent}
            
];
