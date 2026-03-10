import { Routes } from '@angular/router';
import {PageComponent} from './page/page';
import {OrdersComponent}from './orders/orders';
import {BagComponent} from './bag/bag';
import {AccountComponent} from './account/account';
import {WomensComponent} from './womens/womens';
export const routes: Routes = [
    {path:'', component:PageComponent},
    {path:'orders',component:OrdersComponent},
    {path:'bag',component:BagComponent},
      {path:'account',component:AccountComponent},
      {path:'womens',component:WomensComponent},
    {path:'**',redirectTo:''}
];
