
import { Component, OnInit } from '@angular/core';
import { ArticuloService } from '../services/articulo.service';
import { RouterLink } from '@angular/router';
import { Articulo } from './model/articulo.model';
import { Categoria } from './model/articulo.model';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-articulos',
  standalone: true,
  imports: [ReactiveFormsModule,CommonModule],
  templateUrl: './articulos.component.html',
  styleUrls: ['./articulos.component.css']
})
export class ArticulosComponent implements OnInit {
  articuloList: Articulo[] = [];
  selectedCategoria: string = ''; // Ahora es un string para coincidir con getCategoryId()

  constructor(private articuloService: ArticuloService) {}

  ngOnInit(): void {
    this.updateCategory(this.selectedCategoria);
  }

  updateCategory(categoria: string): void {
    this.selectedCategoria = categoria;
    this.articuloService.obtenerArticulos().subscribe(
      (articulos: Articulo[]) => {
        this.articuloList = articulos.filter(
          articulo => articulo.categoria.id === this.getCategoryId(this.selectedCategoria)?.id
        );
        
      },
      (error) => {
        console.error('Error al obtener los artículos', error);
      }
    );
  }

  getCategoryId(category: string): Categoria | null {
    const categorias: Categoria[] = [
      { id: 1, nombre: 'accesorios' },
      { id: 2, nombre: 'alimentos' }
    ];
    return categorias.find(cat => cat.nombre.toLowerCase() === category.toLowerCase()) || null;
  }
  
  
}
