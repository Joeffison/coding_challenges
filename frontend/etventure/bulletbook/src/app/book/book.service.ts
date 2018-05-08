import { Injectable } from '@angular/core';
import { Book } from './book';
import { Store } from '@ngrx/store';

@Injectable()
export class BookService {
  public lastId: number = 0;
  public books: Book[] = [];

  constructor(private _store: Store<any>) {
    _store.select('books').subscribe(books => {
      this.books = books;
    });
  }

  public addBook(book: Book): void {
    this._store.dispatch({
      type: 'ADD_BOOK',
      payload: {
        id: ++this.lastId,
        title: book.title,
        complete: book.complete
      }
    });
  }

  public deleteBookById(itemId: number): void {
    this._store.dispatch({
      type: 'REMOVE_BOOK',
      payload: { id: itemId }
    });
  }

  public toggleBookComplete(itemId: number): void {
    this._store.dispatch({
      type: 'TOGGLE_COMPLETE',
      payload: { id: itemId }
    });
  }

  public getCompletedItems(): Book[] {
    return this.books.filter(item => item.complete === true);
  }

  public getIncompletedItems(): Book[] {
    return this.books.filter(item => item.complete === false);
  }
}
