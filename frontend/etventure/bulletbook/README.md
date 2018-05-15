# Bulletbook

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 6.0.0.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Either use Materialize 0.100.2 or update angular2-materialize to use 1.x (as it is now, just change node_modules/angular2-materialize/dist/index.js as shown below) because "window.Materialize" was renamed to "window.M".

if (!("Materialize" in window)) {
  if (!("M" in window)) {
    throw new Error("Couldn't find Materialize object on window. It is created by the materialize-css library. Please import materialize-css before importing angular2-materialize.");
  } else {
    window["Materialize"] = window["M"];
  }
}

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).
