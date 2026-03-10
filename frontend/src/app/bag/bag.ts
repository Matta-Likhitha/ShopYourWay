import { Component ,OnInit} from '@angular/core';
import { BagItem, OrderService } from '../order.service';
import { CommonModule } from '@angular/common';
import { Route, Router } from '@angular/router';
import { RouterModule } from '@angular/router';
import { Observable } from 'rxjs';
@Component({
  selector: 'app-bag',
  imports: [CommonModule,RouterModule],
  templateUrl: './bag.html',
  styleUrl: './bag.css',
})
export class BagComponent implements OnInit{
 
  bagItems$!: Observable<BagItem[]>;
 constructor(public orderService: OrderService, private router:Router) {}
 ngOnInit() {
    // 2. Link the local observable to the service's observable
    this.bagItems$ = this.orderService.bagItems$;
  }
  placeOrder() {
    this.orderService.placeOrder();
  }
home(){
  this.router.navigate(['/']);
}
clearBag(){
  this.orderService.clearBag();

}
}
