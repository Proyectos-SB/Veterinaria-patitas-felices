export interface Mascota {
    id: number;
    nombre: string;
    raza: string;
    edad: number;
    sexo: string;
    tipo?: { nombre: string };
  }