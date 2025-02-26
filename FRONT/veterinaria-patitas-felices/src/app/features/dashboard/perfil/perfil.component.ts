import { Component, NgModule } from '@angular/core';
import { UsuarioService } from '../../../core/services/usuario.service';
import { UsuarioInterface } from '../../auth/models/usuarioInterface.model';
import { NgIf } from '@angular/common';
import { FormsModule, NgModel } from '@angular/forms';

@Component({
  selector: 'app-perfil',
  standalone: true,
  imports: [NgIf,FormsModule  ],
  templateUrl: './perfil.component.html',
  styleUrl: './perfil.component.css'
})
export class PerfilComponent {
  usuario!: UsuarioInterface;

  modoEdicion = false;

  constructor(private usuarioService: UsuarioService) {}

  ngOnInit(): void {
    this.cargarUsuario();
  }

  cargarUsuario(): void {
    this.usuarioService.getUsuario().subscribe(
      (data) => {
        this.usuario = data;
      },
      (error) => {
        console.error('Error al cargar usuario:', error);
      }
    );
  }

  toggleEditar(): void {
    this.modoEdicion = !this.modoEdicion;
  }

  guardarCambios(): void {
    this.usuarioService.updateUsuario(this.usuario).subscribe(
      (response) => {
        console.log('Usuario actualizado con éxito');
        this.modoEdicion = false;
      },
      (error) => {
        console.error('Error al actualizar usuario:', error);
      }
    );
  }
}
