export class Usuario {
    id?: number;
    first_name: string = "";
    last_name: string = "";
    email: string = "";
    dni: number | null = null;
    direccion: string = "";
    telefono: string = "";
    password: string = "";
    is_cliente: boolean = true; // Siempre es cliente al registrarse
}