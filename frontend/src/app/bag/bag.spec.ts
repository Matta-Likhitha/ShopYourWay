import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BagComponent } from './bag';

describe('Bag', () => {
  let component: BagComponent;
  let fixture: ComponentFixture<BagComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BagComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BagComponent);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
