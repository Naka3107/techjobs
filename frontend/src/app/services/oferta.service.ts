import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { inject } from '@angular/core';
import { Oferta } from '../models/oferta';
import { Programador } from '../models/programador';
import { Resultado } from '../models/resultado';

@Injectable({
  providedIn: 'root',
})
export class OfertaService {
  private readonly http = inject(HttpClient);
  private apiUrl = 'http://localhost:5000';

  getOfertas() {
    return this.http.get<Oferta[]>(`${this.apiUrl}/ofertas`);
  }

  getProgramadores() {
    return this.http.get<Programador[]>(`${this.apiUrl}/programadores`);
  }

  getCompatibles(nombre: string, salarioMinimo: number) {
    return this.http.get<Resultado[]>(`${this.apiUrl}/ofertas/compatibles/${nombre}/${salarioMinimo}`)
  }
}
