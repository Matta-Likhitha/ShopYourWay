import { Component } from '@angular/core';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CurrencyPipe,DatePipe } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Order,OrderService } from '../order.service';

@Component({
  selector: 'app-orders',
  imports: [FormsModule,CurrencyPipe,DatePipe,CommonModule],
  templateUrl: './orders.html',
  styleUrl: './orders.css',
})
export class OrdersComponent {
    constructor(public orderService: OrderService) {}
userName = 'Likhitha';
searchText = '';
onSearch() {
    console.log('Search:', this.searchText);
  }

  onFilter(type: string) {
    console.log('Filter clicked:', type);
  }
  
  // Logic to handle sorting
 onSortChange(event: any) {
  const value = event.target.value;
  if (value === 'asc') {
    this.orderService.sortOrders((a: Order, b: Order) =>
      new Date(a.created_at).getTime() - new Date(b.created_at).getTime()
    );
  } else if (value === 'desc') {
    this.orderService.sortOrders((a: Order, b: Order) =>
      new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
    );
  }
}
  
}
