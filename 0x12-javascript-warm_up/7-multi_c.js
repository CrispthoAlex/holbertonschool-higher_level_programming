#!/usr/bin/node
// Script that prints x times C is fun
const myVar = 'C is fun';
const times = process.argv[2];

if (times) {
  for (let i = 0; i < times; i++) console.log(myVar);
} else console.log('Missing number of occurrences');
