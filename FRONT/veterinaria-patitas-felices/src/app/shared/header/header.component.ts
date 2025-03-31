import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { AuthService } from '../../core/services/auth.service';
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

  constructor(private authService: AuthService) {
    this.authService.authStatus$.subscribe({
      next: (data) => {
        console.log(data);
        this.estaAutenticado = data;
      },
      error: (error) => {
        console.error('No se pudo autenticar:', error);
      }
    });
  }
  ngOnInit(): void {
    this.authService.authStatus$.subscribe(status => {
      this.estaAutenticado = status;
    });
  }
  logOut(){
    Swal.fire({
      title: "¿Estás Seguro?",
      text: "¿Seguro que quieres irte =( ?",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Si"
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire({
          title: "¡Adiós!",
          text: "Te esperamos!",
          icon: "success"
        });
        
          this.authService.logOut();
      
      }
    });
  }
}