import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Router } from '@angular/router';
@Component({
  selector: 'app-page',
  imports: [RouterOutlet],
  templateUrl: './page.html',
  styleUrl: './page.css',
})
export class PageComponent {

  constructor(private router: Router){}
  womens(){
    this.router.navigate(['/womens']);
  }
}
