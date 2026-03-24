import { Routes } from '@angular/router';
import { Buscador } from './buscador/buscador';
import { ListaOfertas } from './lista-ofertas/lista-ofertas';
import { Bienvenida } from './bienvenida/bienvenida';

export const routes: Routes = [
    { path: '', component: Bienvenida },
    { path: 'ofertas', component: ListaOfertas },
    { path: 'buscador', component: Buscador },
];
