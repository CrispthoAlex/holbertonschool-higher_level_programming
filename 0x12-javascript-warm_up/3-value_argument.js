#!/usr/bin/node
// Script that prints the first argument passed to it
// process.argv
// console.log(`${process.argv}`)

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
