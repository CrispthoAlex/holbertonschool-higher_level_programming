#!/usr/bin/node
// script that imports an array and computes a new array
const list = require('./100-data.js').list;
const compuArr = list.map((num, index) => num * index);
console.log(list);
console.log(compuArr);
