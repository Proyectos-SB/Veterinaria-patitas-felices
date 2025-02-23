import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { RegistroService } from '../services/registro.service';
import { Usuario } from '../models/usuario.model';

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
      repitePassword: ['', [Validators.required]], /*recordar ver el cambio a verde*/
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
     /* this.registroService.registrarUsuario(usuario).subscribe( data => {
        alert('Registro exitoso, ahora puedes iniciar sesión.')
        this.router.navigate(['/login']);
      }, error => {
        alert('Error en el registro, intenta nuevamente.');
      });*/
    } else {
      this.formRegister.markAllAsTouched();
    }
  }

  get firstName() { return this.formRegister.get('first_name'); }
  get lastName() { return this.formRegister.get('last_name'); }
  get email() { return this.formRegister.get('email'); }
  get direccion() { return this.formRegister.get('direccion'); }
  get telefono() { return this.formRegister.get('telefono'); }
  get password() { return this.formRegister.get('password'); }
  get repitePassword() { return this.formRegister.get('repitePassword'); }
}
