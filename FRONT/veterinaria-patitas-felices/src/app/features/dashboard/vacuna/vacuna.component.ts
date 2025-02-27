import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, NgModel, ReactiveFormsModule, Validators } from '@angular/forms';
import { MascotaService } from '../mascota/services/mascota.service';
import { VacunaService } from './services/vacuna.service';
import { AplicacionVacunaService } from './services/aplicacion-vacuna.service';
import { Router } from '@angular/router';
import { Mascota } from '../mascota/models/mascota.model';  // Asegúrate de que la importación sea correcta
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-vacuna',
  standalone: true, 
  imports: [CommonModule, ReactiveFormsModule,FormsModule],  // Añade ReactiveFormsModule para usar formularios
  templateUrl: './vacuna.component.html',
  styleUrls: ['./vacuna.component.css']
})
export class VacunaComponent implements OnInit {

  mascotas: Mascota[] = [];  // Lista de mascotas del usuario
  vacunas: any[] = []; // Lista de vacunas disponibles
  vacuna = { mascota: '', vacuna: '', fecha_aplicacion: '', proximo_refuerzo: '' };

  constructor(
    private mascotaService: MascotaService,
    private vacunaService: VacunaService,
    private aplicacionVacunaService: AplicacionVacunaService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.loadMascotas();
    this.loadVacunas();
  }

  // Cargar las mascotas del cliente
  loadMascotas() {
    this.mascotaService.getMascotas().subscribe(
      (response) => {
        this.mascotas = response;
      },
      (error) => {
        console.error('Error al cargar mascotas', error);
      }
    );
  }

  // Cargar las vacunas disponibles
  loadVacunas() {
    this.vacunaService.getVacunas().subscribe(
      (response) => {
        this.vacunas = response;
      },
      (error) => {
        console.error('Error al cargar vacunas', error);
      }
    );
  }

  // Enviar el formulario para aplicar la vacuna
  onSubmit() {
    this.aplicacionVacunaService.createAplicacionVacuna(this.vacuna).subscribe(
      (response) => {
        console.log('Vacuna aplicada correctamente:', response);
        this.router.navigate(['/mascotas']);
      },
      (error) => {
        console.error('Error al aplicar vacuna', error);
      }
    );
  }
}

