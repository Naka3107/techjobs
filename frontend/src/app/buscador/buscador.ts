import { Component, inject, signal } from '@angular/core';
import { Resultado } from '../models/resultado';
import { DecimalPipe } from '@angular/common';
import { OfertaService } from '../services/oferta.service';

@Component({
  selector: 'app-buscador',
  imports: [DecimalPipe],
  templateUrl: './buscador.html',
  styleUrl: './buscador.scss',
})
export class Buscador {
  resultados = signal<Resultado[]>([]);
  nombre = signal<string>('');
  salarioMinimo = signal<number>(0);
  estado = signal<'idle' | 'ok' | 'error'>('idle');

  private service = inject(OfertaService);

  buscar() {
    if(!this.nombre()) {
      alert('Por favor, introduce el nombre del programador.');
      return;
    }
    if(!this.salarioMinimo() || this.salarioMinimo() < 0) {
      alert('Por favor, introduce un salario mínimo válido.');
      return;
    }
    this.service.getCompatibles(this.nombre(), this.salarioMinimo()).subscribe({
      next: data => {
        this.resultados.set(data);
        if (data.length === 0) {
          this.estado.set('error');
          alert('No se han encontrado ofertas compatibles con los criterios de búsqueda.');
          return;
        }
        this.estado.set('ok');
      },
      error: err => {
        if (err.status === 404) {
          this.estado.set('error');
          alert('No se ha encontrado al programador especificado.');
        }
      }
    });
  }
}
