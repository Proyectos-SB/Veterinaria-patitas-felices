import { TestBed } from '@angular/core/testing';

import { AplicacionVacunaService } from './aplicacion-vacuna.service';

describe('AplicacionVacunaService', () => {
  let service: AplicacionVacunaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AplicacionVacunaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
