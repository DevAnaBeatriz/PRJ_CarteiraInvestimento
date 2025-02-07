import { Routes, RouterModule } from '@angular/router';
import { RentabilidadeComponent } from './components/rentabilidade/rentabilidade.component';

export const routes: Routes = [
  { path: '', component: RentabilidadeComponent }
];

export const appRouting = RouterModule.forRoot(routes);
