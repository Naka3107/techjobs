import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProgramadorCard } from './programador-card';

describe('ProgramadorCard', () => {
  let component: ProgramadorCard;
  let fixture: ComponentFixture<ProgramadorCard>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProgramadorCard],
    }).compileComponents();

    fixture = TestBed.createComponent(ProgramadorCard);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
