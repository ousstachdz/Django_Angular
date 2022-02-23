import { Component } from '@angular/core';
import { ServiceService } from './services/message/service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';

  msg:any ;
  constructor(private service:ServiceService){}

  ngOnInit():void{
    this.showMessage()
  }

  showMessage(){
    this.service.getMessage().subscribe(data=>{
      this.msg = data;
      this.msg = this.msg.message
    })
  }


}
