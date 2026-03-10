import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WomensComponent} from './womens';

describe('Womens', () => {
  let component: WomensComponent;
  let fixture: ComponentFixture<WomensComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [WomensComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WomensComponent);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
