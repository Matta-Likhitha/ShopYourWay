import { Injectable } from '@angular/core';
import { BehaviorSubject, tap } from 'rxjs';
import { HttpClient } from '@angular/common/http';

// ── Matches backend schemas.py
export interface Product {
  id: number;
  name: string;
  brand: string;
  price: number;
  image_url: string;
  stock: number;
  category: string;
}

export interface BagItem {
  id: number;
  product: Product;
  quantity: number;
  added_at: Date;
}

export interface OrderItem {
  product: Product;
  quantity: number;
  price: number;
}

export interface Order {
  id: number;
  status: string;
  delivered: boolean;
  total_price: number;
  created_at: Date;
  items: OrderItem[];
}

@Injectable({
  providedIn: 'root'
})
export class OrderService {
  private readonly API = 'http://localhost:8000';
  private userId = 1; // ← replace with real user id after adding login

  // ── Streams (same as before, just fed from API now)
  private _bagItems = new BehaviorSubject<BagItem[]>([]);
  bagItems$ = this._bagItems.asObservable();

  private _orders = new BehaviorSubject<Order[]>([]);
  orders$ = this._orders.asObservable();

  // Add this to order.service.ts
private _products = new BehaviorSubject<Product[]>([]);
products$ = this._products.asObservable();

  constructor(private http: HttpClient) {
    // Load from API instead of localStorage on startup
    this.loadBag();
    this.loadOrders();
  }

  // ── Bag ─────────────────────────────────────────

  loadBag() {
    this.http.get<BagItem[]>(`${this.API}/bag/${this.userId}`)
      .subscribe(items => this._bagItems.next(items));
  }

  // womens.ts calls this — accepts full product object
  addToBag(product: Product) {
    this.http.post(`${this.API}/bag/${this.userId}`, {
      product_id: product.id,
      quantity: 1
    })
    .pipe(tap(() => this.loadBag()))  // refresh bag after adding
    .subscribe();
  }

  clearBag() {
    this.http.delete(`${this.API}/bag/${this.userId}`)
      .pipe(tap(() => this._bagItems.next([])))
      .subscribe();
  }

  // ── Orders ───────────────────────────────────────

  loadOrders() {
    this.http.get<Order[]>(`${this.API}/orders/${this.userId}`)
      .subscribe(orders => this._orders.next(orders));
  }

  placeOrder() {
    const currentBag = this._bagItems.value;
    if (currentBag.length === 0) return;

    this.http.post(`${this.API}/orders/${this.userId}`, {})
      .pipe(tap(() => {
        this.loadOrders();  // refresh orders page
        this.loadBag();     // refresh bag (it gets cleared by backend)
      }))
      .subscribe();
  }
  loadWomensProducts() {
  // ✅ Check sessionStorage first (survives navigation, not refresh)
  const cached = sessionStorage.getItem('womensProducts');
  if (cached) {
    this._products.next(JSON.parse(cached));
    return;
  }

  // ✅ If not cached, fetch from API and cache it
  this.http.get<Product[]>(`${this.API}/products/womens`)
    .subscribe(data => {
      this._products.next(data);
      sessionStorage.setItem('womensProducts', JSON.stringify(data)); // cache it
    });
}

  // ── Sorting (still done on frontend, same as before)
  sortOrders(compareFn: (a: Order, b: Order) => number) {
    const sorted = [...this._orders.value].sort(compareFn);
    this._orders.next(sorted);
  }
}