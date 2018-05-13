import {Component, OnInit, Input, Output, EventEmitter} from '@angular/core';
import {Book} from "../book/book";

@Component({
  selector: 'app-book-card',
  templateUrl: './book-card.component.html',
  styleUrls: ['./book-card.component.css']
})
export class BookCardComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  @Input() book: Book;
  @Output() toggle = new EventEmitter<any>();
  @Output() remove = new EventEmitter<any>();

  public toggleItem(book: Book): void {
    this.toggle.emit(book);
  }

  public removeItem(book: Book): void {
    this.remove.emit(book);
  }

}
