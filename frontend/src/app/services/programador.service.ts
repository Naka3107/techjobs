import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Programador } from '../models/programador';
import { ProgramadorResponse } from '../models/programador-response';

@Injectable({
  providedIn: 'root',
})
export class ProgramadorService {
  private http = inject(HttpClient);
  private apiUrl = 'http://localhost:5000';

  getProgramadores() {
    return this.http.get<Programador[]>(`${this.apiUrl}/programadores`);
  }

  getProgramadoresCompatibles(ofertaId: number, experienciaMinima?: number, ciudad?: string) {
    let params = new HttpParams();
    if(ofertaId) params = params.set('oferta_id', ofertaId);
    if(experienciaMinima) params = params.set('experiencia', experienciaMinima);
    if(ciudad) params = params.set('ciudad', ciudad);
    return this.http.get<ProgramadorResponse[]>(`${this.apiUrl}/programadores/compatibles`, { params });
  }
}
