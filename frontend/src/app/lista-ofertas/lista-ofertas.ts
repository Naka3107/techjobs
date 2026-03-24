import { Component, OnInit, inject, signal, ViewChild, ElementRef } from '@angular/core';
import { Oferta } from '../models/oferta';
import { OfertaService } from '../services/oferta.service';
import { DecimalPipe } from '@angular/common';

@Component({
  selector: 'app-lista-ofertas',
  imports: [DecimalPipe],
  templateUrl: './lista-ofertas.html',
  styleUrl: './lista-ofertas.scss',
})
export class ListaOfertas implements OnInit {
  ofertas= signal<Oferta[]>([]);
  vista = signal<'lista' | 'tarjetas'>('lista');
  private service = inject(OfertaService);

  @ViewChild('carrusel') carruselRef!: ElementRef;

  scrollCarrusel(direccion: number) {
    const cardWidth = 300; // 280px tarjeta + 20px gap
    this.carruselRef.nativeElement.scrollBy({
      left: direccion * cardWidth,
      behavior: 'smooth'
    });
  }

  ngOnInit(): void {
  console.log('ngOnInit ejecutado');
  this.service.getOfertas().subscribe(data => {
    console.log('datos recibidos:', data);
    this.ofertas.set(data);
  });
  }
}
