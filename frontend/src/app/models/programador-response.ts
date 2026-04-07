import { Programador } from "./programador";

export interface ProgramadorResponse {
    programador: Programador;
    compatibilidad: {
        porcentaje: number;
        desglose: {
            tecnologias_coincidentes: string[];
            tecnologias_faltantes: string[];
            experiencia_cumple: boolean;
            ciudad_cumple: boolean;
            pais_cumple: boolean;
        }
    }
}