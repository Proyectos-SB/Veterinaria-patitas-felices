import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { RegistroService } from '../services/registro.service';
import { Usuario } from '../models/usuario.model';
import Swal from 'sweetalert2';
import { RegistroResponse } from '../models/registroResponse.model';


@Component({
  selector: 'app-registro',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './registro.component.html',
  styleUrl: './registro.component.css',
})
export class RegistroComponent {
  formRegister!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private registroService: RegistroService,
    private router: Router,
  ) {
    this.formRegister = this.formBuilder.group({
      
      first_name: ['',[
                  Validators.required,
                  Validators.minLength(3),
                  Validators.pattern(/^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$/)]],

      last_name: ['',[Validators.required,
                 Validators.minLength(3),
                 Validators.pattern(/^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$/)
                 ]],
      username: ['',[Validators.required,
                  Validators.minLength(3),
                  Validators.maxLength(10)
                  ]],           
      email:    ['',[
                Validators.required,
                Validators.email]
              ],
      direccion: ['', [Validators.required]
              ],
      telefono: ['', [Validators.required, Validators.pattern(/^\d{10}$/)]],
      password: ['',[
                    Validators.required,
                    Validators.minLength(8), 
                    Validators.maxLength(16), 
                    Validators.pattern(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)/)]],
      repitePassword: ['', [Validators.required]], 
      is_cliente: [true]
    }, { validator: this.passwordMatchValidator });
  }

  passwordMatchValidator(form: FormGroup) {
    return form.get('password')?.value === form.get('repitePassword')?.value ? null : { mismatch: true };
  }

  onEnviar(event: Event) {
    event.preventDefault();
    if (this.formRegister.valid) {
      const usuario: Usuario = this.formRegister.value;
      this.registroService.registrarUsuario(usuario).subscribe({
        next: (response: RegistroResponse) => {
          if(response.message){
            Swal.fire({
              title: '¡Bienvenido!',
              text: 'Te has registrado exitosamente!',
              icon: 'success',
              confirmButtonText: 'Aceptar',
            });
            setTimeout(() => {
              this.router.navigateByUrl("/login");
            }, 3000);
          }
        },
        error: (error) => {
          Swal.fire({
            title: 'Error al registrar',
            text: 'Ha ocurrido un error. Intente nuevamente.',
            icon: 'error',
            confirmButtonText: 'Aceptar',
          });
          console.error('Error en el registro:', error);
        }
      });
    } else {
      this.formRegister.markAllAsTouched();
    }
  }

  get firstName() { return this.formRegister.get('first_name'); }
  get lastName() { return this.formRegister.get('last_name'); }
  get email() { return this.formRegister.get('email'); }
  get userName(){ return this.formRegister.get('username'); }
  get direccion() { return this.formRegister.get('direccion'); }
  get telefono() { return this.formRegister.get('telefono'); }
  get password() { return this.formRegister.get('password'); }
  get repitePassword() { return this.formRegister.get('repitePassword'); }
}
