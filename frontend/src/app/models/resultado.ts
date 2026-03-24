export interface Resultado {}
import { Oferta } from './oferta';

export interface Resultado {
  oferta: Oferta;
  coincidencias: string[];
}