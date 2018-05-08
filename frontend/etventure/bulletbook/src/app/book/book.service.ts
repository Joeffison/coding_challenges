import { Injectable } from '@angular/core';
import { Book } from './book';
import { Store } from '@ngrx/store';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class BookService {
  public lastId: number = 0;
  public books: Book[] = [];
  public faves: string[] = ["9781435139435", "9780785126560", "9780091850425", "9781604507102"];

  constructor(private _store: Store<any>, private _http: HttpClient) {
    _store.select('books').subscribe(books => {
      this.books = books;
    });

    this.addByISBN(this.faves);
  }

  public addByISBN(isbn: string[]) {
    let query = isbn.map(item => "isbn:" + item.replace("-","")).join("+OR+");

    return this._http.get("https://www.googleapis.com/books/v1/volumes?q=" + query)
      .subscribe((data: any) => this.addBooks(data.items));
  }

  public addBooks(books: any[]): void {
    console.log(books);
    books.map(item => this.addBook({title: item.volumeInfo.title, complete: true} as Book));
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
