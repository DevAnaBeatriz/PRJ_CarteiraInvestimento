import { Component } from '@angular/core';
import { RentabilidadeComponent } from './components/rentabilidade/rentabilidade.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [
    RentabilidadeComponent
  ]
})
export class AppComponent {}
