import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { MindService } from './shared/mind.service';

import { MindComponent } from './controllers/mind/mind.component';

@NgModule({
  declarations: [
    AppComponent,
    MindComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    MindService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
