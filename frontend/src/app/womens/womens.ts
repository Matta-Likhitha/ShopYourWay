import { Component, OnInit } from '@angular/core';
import { CommonModule, CurrencyPipe } from '@angular/common';
import { RouterModule } from '@angular/router';
import { OrderService, Product } from '../order.service';

@Component({
  selector: 'app-womens',
  imports: [CommonModule, RouterModule, CurrencyPipe],
  templateUrl: './womens.html',
  styleUrl: './womens.css',
})
export class WomensComponent implements OnInit {
  showMessage: boolean = false;
  products: Product[] = [];

  constructor(private orderService: OrderService) {} // ✅ removed HttpClient, not needed here

  ngOnInit() {
    this.orderService.loadWomensProducts(); // ✅ fetch from API via service

    this.orderService.products$.subscribe(data => {
      this.products = data; // ✅ update local array when data arrives
    });
  }

  addToBag(product: Product) {
    this.orderService.addToBag(product);
    this.showMessage = true;
    setTimeout(() => this.showMessage = false, 3000);
  }
}