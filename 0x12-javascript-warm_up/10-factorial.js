#!/usr/bin/node
// script that computes and prints a factorial
function factorial (a) {
  if (a === 0 || isNaN(a)) {
    return 1;
  }
  return a * factorial(a - 1);
}
const num = parseInt(process.argv[2]);
console.log(factorial(num));
