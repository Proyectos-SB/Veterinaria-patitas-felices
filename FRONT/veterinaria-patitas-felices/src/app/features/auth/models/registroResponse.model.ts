import { Usuario } from "./usuario.model";
export interface RegistroResponse {
    message: string;
    cliente: Usuario;
  }