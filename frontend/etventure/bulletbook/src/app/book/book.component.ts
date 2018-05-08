import { Component, OnInit } from '@angular/core';
import { Book } from './book';
import { BookService } from './book.service';

@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.css'],
  providers: [BookService]
})
export class BookComponent implements OnInit {

  ngOnInit() {
  }

  newItem: Book = new Book();

  constructor(private bookService: BookService) {}

  public addItem(): void {
    this.bookService.addBook(this.newItem);
    this.newItem = new Book();
  }

  public toggleBookComplete({ id }): void {
    this.bookService.toggleBookComplete(id);
  }

  public removeBook({ id }): void {
    this.bookService.deleteBookById(id);
  }

  public allBooks(): number {
    return this.incompleteBooks.length + this.completeBooks.length;
  }
  public get incompleteBooks(): Array<Book> {
    return this.bookService.getIncompletedItems();
  }

  public get completeBooks(): Array<Book> {
    return this.bookService.getCompletedItems();
  }

}
