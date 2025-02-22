import { Component } from '@angular/core';
import { NgbCarouselModule } from '@ng-bootstrap/ng-bootstrap';
@Component({
  selector: 'app-landing',
  standalone: true,
  imports: [NgbCarouselModule],
  templateUrl: './landing.component.html',
  styleUrl: './landing.component.css'
})
export class LandingComponent {
  images = [
    'assets/banner/Banner1.jpg',
    'assets/banner/Banner2.jpg',
    'assets/banner/Banner3.png'
  ];
}
