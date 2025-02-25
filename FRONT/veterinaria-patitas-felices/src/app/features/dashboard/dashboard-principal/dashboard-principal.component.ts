import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UsuarioService,} from '../../../core/services/usuario.service';
import { UsuarioInterface } from '../../auth/models/usuarioInterface.model';
@Component({
  selector: 'app-dashboard-principal',
  standalone: true,
  imports: [],
  templateUrl: './dashboard-principal.component.html',
  styleUrl: './dashboard-principal.component.css'
})
export class DashboardPrincipalComponent {
  usuario!: UsuarioInterface;
  constructor(private usuarioService: UsuarioService, private router: Router) {}
  
  ngOnInit(): void {
    this.usuarioService.getUsuario().subscribe((userData) => {
      this.usuario = userData;
    });
  }
  verPerfil(): void {
    this.router.navigate(['/me/']);
  }
  editarPerfil(): void {
    this.router.navigate(['/me/editar']);
  }

  registrarMascota(): void {
    this.router.navigate(['/mascotas/registrar']);
  }

  verMascotas(): void {
    this.router.navigate(['/mascotas']);
  }

  verHistorialCompras(): void {
    this.router.navigate(['/pedidos/historial']);
  }
}

