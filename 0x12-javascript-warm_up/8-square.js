#!/usr/bin/node
// Script that prints x times C is fun
const myVar = 'X';
const times = process.argv[2];

if (parseInt(times)) {
  for (let i = 0; i < times; i++) console.log(myVar.repeat(times));
} else console.log('Missing size');
