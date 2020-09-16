#!/usr/bin/node
// Script that prints 3 lines
// process.argv
// console.log(`${process.argv}`)

if (process.argv.length === 2) { console.log('No argument'); } else if (process.argv.length === 3) { console.log('Argument found'); } else if (process.argv.length > 3) { console.log('Arguments found'); }
