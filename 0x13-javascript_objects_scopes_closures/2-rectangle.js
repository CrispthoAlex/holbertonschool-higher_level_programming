#!/usr/bin/node
/* Write an empty class Rectangle that defines a rectangle
   The constructor must take 2 arguments w and h
   Initialize the instance attribute width with the value of w
   Initialize the instance attribute height with the value of h
   If w or h is equal to 0 or not a positive integer, create an empty object
*/
// set the exports object to a function or a new object
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || w === undefined) || (h <= 0 || h === undefined)) {
      return this;
    }
    this.width = w;
    this.height = h;
  }
};
