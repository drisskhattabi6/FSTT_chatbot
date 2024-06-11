import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChoosemodelComponent } from './choosemodel.component';

describe('ChoosemodelComponent', () => {
  let component: ChoosemodelComponent;
  let fixture: ComponentFixture<ChoosemodelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ChoosemodelComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ChoosemodelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
