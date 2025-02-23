import { Routes } from '@angular/router';
import { LandingComponent } from './pages/landing/landing.component';
import { RegistroComponent } from './features/auth/registro/registro.component';

export const routes: Routes = [
    {path: "index", component: LandingComponent},
    {path: "registro", component: RegistroComponent},
    {path:"", redirectTo:"/index", pathMatch:"full"},
    
    

    
];
