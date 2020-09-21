#!/usr/bin/node
/* Write a class Square that defines a square and inherits from Rectangle of
   4-rectangle.js
*/
// set the exports object to a function or a new object
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }

  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  rotate () {
    // const temp = this.width;
    // Swap variables: https://javascript.info/destructuring-assignment
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
