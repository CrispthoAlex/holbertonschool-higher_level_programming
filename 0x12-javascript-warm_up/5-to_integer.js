#!/usr/bin/node
// Script that prints a string if the first argument is integer
// process.argv
// console.log(`${process.argv}`)
const num = parseInt(process.argv[2]);
if (num) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
