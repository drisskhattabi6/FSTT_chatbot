import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { ChoosemodelComponent } from './choosemodel/choosemodel.component';
export const routes: Routes = [
  { path: '', component: ChoosemodelComponent },
  { path: 'chat', component: HomeComponent },
  { path: 'about', component: AboutComponent }
];
