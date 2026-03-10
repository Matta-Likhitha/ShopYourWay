import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
interface Order {
  id: number;
  date: Date;
  amount: number;
}
@Component({
  selector: 'app-root',
  imports: [RouterOutlet,FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  userName = 'Likhitha';
searchText = '';
  protected readonly title = signal('Frontend');
  constructor(private router: Router) {}
orders(){
  this.router.navigate(['/orders']);
}
bag(){
  this.router.navigate(['/bag']);
}
account(){
  this.router.navigate(['/account']);
}
home(){
  this.router.navigate(['/']);
}
}
