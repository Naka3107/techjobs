import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { PerfilResponse } from '../models/perfil-response';


@Injectable({ providedIn: 'root'})
export class PerfilService {
  private http = inject(HttpClient);
  private apiUrl = 'http://localhost:5000';

  getPerfil() {
    return this.http.get<PerfilResponse>(`${this.apiUrl}/perfil`);
  }

  actualizarPerfil(datos: PerfilResponse, rol: string, tecnologiasNuevas: string[]) {
    const datosFiltrados: any = {
      nombre: datos.nombre,
      ciudad: datos.ciudad,
      pais: datos.pais
    };

    if (rol === 'programador') {
      datosFiltrados.experiencia = datos.experiencia;
      datosFiltrados.tecnologias = tecnologiasNuevas;
    } else if (rol === 'empresa') {
      datosFiltrados.pagina_web = datos.pagina_web;
    }

    return this.http.put(`${this.apiUrl}/perfil`, datosFiltrados);
  }
}
