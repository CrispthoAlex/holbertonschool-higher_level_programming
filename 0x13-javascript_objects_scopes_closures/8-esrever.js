#!/usr/bin/node
// Function that returns the number of occurrences in a list
exports.esrever = function (list) {
  const len = list.length;
  let num = 0;
  const newlist = [];

  for (let i = len - 1; i >= 0; i--) {
    newlist[i] = list[num];
    num += 1;
  }
  return newlist;
};
