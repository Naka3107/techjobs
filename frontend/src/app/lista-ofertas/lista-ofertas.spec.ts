import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaOfertas } from './lista-ofertas';

describe('ListaOfertas', () => {
  let component: ListaOfertas;
  let fixture: ComponentFixture<ListaOfertas>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListaOfertas],
    }).compileComponents();

    fixture = TestBed.createComponent(ListaOfertas);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
