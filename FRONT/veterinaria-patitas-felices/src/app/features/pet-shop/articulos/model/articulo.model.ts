export interface Categoria {
    id: number;
    nombre: string;
  }   
export interface Articulo {
    id?: number;
    nombre: string;
    descripcion: string;
    precio: number;
    imagen: string;
    stock: number;
    categoria: Categoria;
  }