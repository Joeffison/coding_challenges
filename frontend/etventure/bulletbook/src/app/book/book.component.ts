import { Component, OnInit } from '@angular/core';
import { Book } from './book';
import { BookService } from './book.service';
import { Observable, of, timer } from "rxjs";
import { switchMap, repeat, tap } from "rxjs/operators";
import { Subscription } from "rxjs/internal/Subscription";

@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.css'],
  providers: [BookService]
})
export class BookComponent implements OnInit {
  private randomRank$: Observable<any>;
  private randomRankingSubscription: Subscription;

  ngOnInit() {
    this.randomRank$ = of(1).pipe(
      switchMap(() => timer(this._randomTime())),
      tap(() => {
        this.books.map(book => {
          book.rating = this._getRandom(0, 5);
          this.rateBook(book);
          return book;
        });
      }),
      repeat()
    );
  }

  newItem: string = "";
  constructor(private bookService: BookService) {}

  public addItem(): void {
    if(this.newItem){
      this.bookService.addByISBN([this.newItem]);
      this.newItem = "";
    }
  }

  public toggleBook({ id }): void {
    this.bookService.toggleBookComplete(id);
  }

  public rateBook(book: Book): void {
    this.bookService.rateBook(book.id, book.rating);
  }

  public removeBook({ id }): void {
    this.bookService.deleteBookById(id);
  }

  public allBooks(): number {
    return this.books.length;
  }

  public get books(): Book[] {
    return this.bookService.getItems();
  }

  public get isRandomRanking(): boolean {
    return this.randomRankingSubscription !== undefined;
  }

  public randomRank(): void {
    if(this.isRandomRanking) {
      this.randomRankingSubscription.unsubscribe();
      this.randomRankingSubscription = undefined;
    } else {
      this.randomRankingSubscription = this.randomRank$.subscribe();
    }
  }

  private _randomTime() {
    return ~~(Math.random() * 3000) + 500;
  }

  private _getRandom(min: number, max: number) {
    return Math.random() * (max - min) + min;
  }

}
