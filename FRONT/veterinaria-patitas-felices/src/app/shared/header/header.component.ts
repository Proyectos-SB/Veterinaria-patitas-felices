import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { LoginService } from '../../features/auth/services/login.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {
    showMenu = false;
    estaAutenticado = false;
  constructor(private loginService: LoginService) {
     
    this.loginService.isLogginOn$.subscribe({
      next: (data) => {
        this.estaAutenticado = data;
      },
      error: (error) => {
        console.error('No se pudo autenticar:', error);
        this.estaAutenticado = false;
      }
    });
  }
  logOut() {
    Swal.fire({
      title: "¿Estás Seguro?",
      text: "¿seguro que quieres irte =( ?",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Si"
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire({
          title: "Adiós!",
          text: "Te esperamos!",
          icon: "success"
        });
        setTimeout(() => {
          this.loginService.logOut();
        }, 2000);
      }
    });
  }
}

