import { Injectable } from '@angular/core';
import { Book } from './book';
import { Store } from '@ngrx/store';
import { HttpClient } from '@angular/common/http';
import { map } from "rxjs/operators";

@Injectable()
export class BookService {
  private MAX_REQUEST_SIZE: number = 3;

  public lastId: number = 0;
  public books: Book[] = [];
  public faves: string[] = [
    "9781435139435", // 1435139437 Oscar Wilde - The Picture of Dorian Gray and Other Works (Sterling)
    "9780674057920", // 0674057929 Oscar Wilde - The Picture of Dorian Gray - An Annotated, Uncensored Edition (Harvard University Press)
    "9780785126560", // 0785126562 Oscar Wilde - The Picture of Dorian Gray (Marvel Illustrated)
    "9780141442464", // 0141442468 Oscar Wilde - The Picture of Dorian Gray (A Penguin Classics Hardcover)
    "9781604244625", // 1604244623 Oscar Wilde - De Profundis (Book Jungle)
    "9781853266102", // 1853266108 Oscar Wilde - Teleny (The Reverse of the Medal) (Wordsworth Classic Erotica)
    "9780241251805", // 024125180X Oscar Wilde - Only Dull People Are Brilliant at Breakfast (Penguin Little Black Classics)

    // incomplete JSON
    "9780497253103", // 0497253100 Oscar Wilde - The Picture of Dorian Gray (Webster's Thesaurus Edition)

    // not on Google Books yet
    "9783895080982", // 3895080985 Oscar Wilde - The Picture of Dorian Gray (Konemann Classics)
    "9780955816932", // 0955816939 Oscar Wilde - The Picture of Dorian Gray (Eye Classics)
    "9781593081751", // 1593081758 Oscar Wilde - The Picture of Dorian Gray (Barnes & Noble Classics)
    "9788579714153", // 857971415X Oscar Wilde - O Retrato De Dorian Gray (Abril)
    "9780091850425", // 0091850428 Oscar Wilde - The Epigrams of Oscar Wilde (Bracken Books)
    "9781858911427", // 1858911427 Oscar Wilde - The Epigrams of Oscar Wilde (Bracken Books)
    "9781604507102", // 1604507101 Oscar Wilde - De Profundis & The Ballad of Reading Gaol (Serenity Publishers)
    "9788580442694", // 8580442699 Oscar Wilde - O Fantasma de Canterville (Leya)

    // Not Oscar Wilde's
    "9781107020580", // 1107020581 Sarah Turing - Alan M. Turing: Centenary Edition
    "9781476708690", // 147670869X Walter Isaacson - The Innovators: How a Group of Hackers, Geniuses, and Geeks Created the Digital Revolution (Simon & Schuster)
    "9781451648539", // 1451648537 Walter Isaacson - Steve Jobs
    "9788535906509", // 8535906509 Fernando Pessoa - Poesia Completa de Alberto Caeiro (Companhia de Bolso)

    // Not Oscar Wilde's and not on Google Books yet
    "9780385512077", // 0385512074 Thomas Kelley - The Ten Faces of Innovation: Ideo's Strategies for Beating the Devil's Advocate & Driving Creativity Throughout Your Organization (Broadway Business)
    "9788535919431", // 8535919430 Fernando Pessoa - Livro do Desassossego (Companhia das Letras)
    "9788526017788", // 8526017780 Cecília Meireles - Antologia Poética (Global)
  ];

  constructor(private _store: Store<any>, private _http: HttpClient) {
    let books$ = _store.select('books');
    books$
      .pipe(
        map((data) => {
          data.sort((a, b) => a.rating > b.rating ? -1 : 1);
          return data;
        })
      ).subscribe(books => {
        this.books = books;
      });

    for (let i = 0; i < this.faves.length; i += this.MAX_REQUEST_SIZE) {
      this.addByISBN(this.faves.slice(i, i + this.MAX_REQUEST_SIZE));
    }
  }

  // Google Books API

  public addByISBN(isbn: string[]) {
    let query = isbn.map(item => "isbn:" + item.replace("-","")).join("+OR+");

    return this._http.get("https://www.googleapis.com/books/v1/volumes?q=" + query)
      .subscribe((data: any) => this.addBooks(data.items));
  }

  private addBooks(books: any[]): void {
    if(!books) return;

    books
      .filter(item => this.validGoogleBookObject(item))
      .map(item => this.addBook({
        title: item.volumeInfo.title,

        isbn10: item.volumeInfo.industryIdentifiers[0].type === "ISBN_10" ?
          item.volumeInfo.industryIdentifiers[0].identifier : item.volumeInfo.industryIdentifiers[1].identifier,

        isbn13: item.volumeInfo.industryIdentifiers[0].type === "ISBN_10" ?
          item.volumeInfo.industryIdentifiers[1].identifier : item.volumeInfo.industryIdentifiers[0].identifier,

        thumbnail: item.volumeInfo.imageLinks.thumbnail,
        rating: this.ratingFor(item.volumeInfo.industryIdentifiers[0].type === "ISBN_10" ?
          item.volumeInfo.industryIdentifiers[1].identifier : item.volumeInfo.industryIdentifiers[0].identifier),
        complete: true
      } as Book));
  }

  private validGoogleBookObject(book: any): boolean{
    return book.volumeInfo && book.volumeInfo.imageLinks && book.volumeInfo.imageLinks.thumbnail &&
      book.volumeInfo.title && book.volumeInfo.industryIdentifiers && book.volumeInfo.industryIdentifiers.length > 1;
  }

  private ratingFor(isbn: string) {
    let bookIndex = this.faves.indexOf(isbn);

    if(bookIndex < 0) {
      return 0;
    }

    return 5 - (bookIndex * 0.01);
  }

  // CRUD

  public addBook(book: Book): void {
    book.id = ++this.lastId;

    this._store.dispatch({
      type: 'ADD_BOOK',
      payload: book
    });
  }

  public deleteBookById(itemId: number): void {
    this._store.dispatch({
      type: 'REMOVE_BOOK',
      payload: { id: itemId }
    });
  }

  public rateBook(itemId: number, rating: number): void {
    this._store.dispatch({
      type: 'RATE',
      payload: { id: itemId, rating: rating }
    });
  }

  public toggleBookComplete(itemId: number): void {
    this._store.dispatch({
      type: 'TOGGLE_COMPLETE',
      payload: { id: itemId }
    });
  }

  public getItems(): Book[] {
    return this.books;
  }

  public getCompletedItems(): Book[] {
    return this.books.filter(item => item.complete === true);
  }

  public getIncompletedItems(): Book[] {
    return this.books.filter(item => item.complete === false);
  }
}
