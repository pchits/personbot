import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MindComponent } from './controllers/mind/mind.component';

const routes: Routes = [
  { path: '', component: MindComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
