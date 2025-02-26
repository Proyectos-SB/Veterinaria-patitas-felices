import { Component, OnInit } from '@angular/core';
import { MascotaService, Mascota } from './services/mascota.service';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators,} from '@angular/forms';
import { CommonModule, NgIf } from '@angular/common';

@Component({
  selector: 'app-mascota',
  
  standalone: true,
  imports: [FormsModule,NgIf,CommonModule, ReactiveFormsModule], 
  templateUrl: './mascota.component.html',
  styleUrls: ['./mascota.component.css']
})
export class MascotaComponent implements OnInit {
  mascotas: Mascota[] = [];
  mascotaForm: FormGroup;
  editMode = false;
  mascotaIdEdit?: number;

  constructor(private mascotaService: MascotaService, private fb: FormBuilder) {
    this.mascotaForm = this.fb.group({
      nombre: ['', Validators.required],
      raza: ['', Validators.required],
      edad: ['', [Validators.required, Validators.min(0)]],
      sexo: ['', Validators.required],
      tipo: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    this.obtenerMascotas();
  }

  obtenerMascotas(): void {
    this.mascotaService.getMascotas().subscribe((data) => {
      this.mascotas = data;
    });
  }

  guardarMascota(): void {
    if (this.mascotaForm.invalid) return;

    const mascota: Mascota = this.mascotaForm.value;

    if (this.editMode && this.mascotaIdEdit) {
      // Editar mascota existente
      this.mascotaService.updateMascota(this.mascotaIdEdit, mascota).subscribe(() => {
        this.obtenerMascotas();
        this.resetForm();
      });
    } else {
      // Crear nueva mascota
      this.mascotaService.createMascota(mascota).subscribe(() => {
        this.obtenerMascotas();
        this.resetForm();
      });
    }
  }

  editarMascota(mascota: Mascota): void {
    this.mascotaForm.patchValue(mascota);
    this.mascotaIdEdit = mascota.id;
    this.editMode = true;
  }

  resetForm(): void {
    this.mascotaForm.reset();
    this.editMode = false;
    this.mascotaIdEdit = undefined;
  }
}
