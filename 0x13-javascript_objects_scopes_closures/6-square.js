#!/usr/bin/node
/* Write a class Square that defines a square and inherits from Rectangle of
   4-rectangle.js
*/
// set the exports object to a function or a new object
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let ch = c;
    if (ch === undefined) { ch = 'X'; }
    for (let i = 0; i < this.width; i++) console.log(ch.repeat(this.width));
  }
};
