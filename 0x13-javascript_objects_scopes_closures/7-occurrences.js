#!/usr/bin/node
// Function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let elem;
  let num = 0;
  for (elem of list) {
    if (elem === searchElement) {
      num += 1;
    }
  }
  return num;
};
