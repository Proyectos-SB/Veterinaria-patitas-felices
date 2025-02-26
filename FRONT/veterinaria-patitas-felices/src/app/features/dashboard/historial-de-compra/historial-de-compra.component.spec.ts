import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HistorialDeCompraComponent } from './historial-de-compra.component';

describe('HistorialDeCompraComponent', () => {
  let component: HistorialDeCompraComponent;
  let fixture: ComponentFixture<HistorialDeCompraComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HistorialDeCompraComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HistorialDeCompraComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
