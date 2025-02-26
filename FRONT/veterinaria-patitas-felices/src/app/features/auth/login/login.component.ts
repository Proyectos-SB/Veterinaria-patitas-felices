import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../../core/services/auth.service';
import { LoginRequest } from '../models/loginRequest.model';
import Swal from 'sweetalert2';
@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  form: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    this.form = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]]
    });
  }

  onEnviar(event: Event) {
    event.preventDefault();
    if (this.form.valid) {
      const { email, password } = this.form.value as LoginRequest;

      this.authService.login({ email, password }).subscribe({
        next: (response) => {
          if (response.access) {
            console.log("Login exitoso");
            //alert("Ingreso Correcto!");  // Cambiar el estado de autenticación
            Swal.fire({
              title: '��Bienvenido!',
              text: 'Has iniciado sesión correctamente.',
              icon:'success',
              confirmButtonText: 'Aceptar',
            });
            this.router.navigateByUrl("/index");
          };
        },
        error: (error) => {
          console.error("Error durante el login:", error);
          alert("ERROR: " + error.message);
        }
      });
    } else {
      this.form.markAllAsTouched();  // Marca todos los campos como tocados
    }
  }

  get Password() {
    return this.form.get('password');
  }

  get Email() {
    return this.form.get('email');
  }
}