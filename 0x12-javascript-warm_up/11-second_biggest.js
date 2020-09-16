#!/usr/bin/node
// script  that searches the second biggest integer in the list of arguments
const arrArg = process.argv;
const numElem = arrArg.length;
if (numElem <= 3) {
  console.log('0');
} else {
  const arrSort = arrArg.sort((a, b) => a - b); // Arrow function expressions
  console.log(arrSort[numElem - 2]);
}
