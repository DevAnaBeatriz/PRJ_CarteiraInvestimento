import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { DecimalPipe, KeyValuePipe, NgClass, CommonModule } from '@angular/common';

interface Ativo {
  'Valor Investido (R$)': number;
  'Preço Inicial (R$)': number;
  'Preço Final (R$)': number;
  'Rentabilidade (%)': number;
}

@Component({
  selector: 'app-rentabilidade',
  templateUrl: './rentabilidade.component.html',
  standalone: true, // ✅ Definindo como standalone
  imports: [
    CommonModule,  // ✅ Adicionando CommonModule para resolver *ngIf e *ngFor
    KeyValuePipe,
    DecimalPipe,
    NgClass
  ],
  styleUrls: ['./rentabilidade.component.css']
})
export class RentabilidadeComponent implements OnInit {
  rentabilidade: { detalhes: { [key: string]: Ativo } } = { detalhes: {} };

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.apiService.getRentabilidade().subscribe(
      (data: any) => {
        this.rentabilidade = data;
      },
      error => {
        console.error('Erro ao buscar rentabilidade:', error);
      }
    );
  }
}
