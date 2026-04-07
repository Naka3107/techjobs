import { Component, input, signal } from '@angular/core';
import { DecimalPipe } from '@angular/common';
import { ProgramadorResponse } from '../models/programador-response';

@Component({
  selector: 'app-programador-card',
  imports: [DecimalPipe],
  templateUrl: './programador-card.html',
  styleUrl: './programador-card.scss'
})
export class ProgramadorCard {
  programador = input.required<ProgramadorResponse>();
  modo = input<'lista' | 'tarjeta'>('tarjeta');
  abierta = signal(false);

  toggle() {
    this.abierta.set(!this.abierta());
  }
}