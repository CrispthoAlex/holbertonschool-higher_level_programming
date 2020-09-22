#!/usr/bin/node
// Write a script that concats 2 files
const fileC = process.argv[4];
const fs = require('fs');

// Synchronous version of fs.readFile. Returns the contents of the filename
const txtA = fs.readFileSync(`./${process.argv[2]}`, 'utf8');
const txtB = fs.readFileSync(`./${process.argv[3]}`, 'utf8');
const txtC = txtA + txtB;

/* Asynchronously writes data to a file, replacing the file if it
   already exists. data can be a string or a buffer
*/
fs.writeFile(fileC, txtC, (err) => {
  if (err) throw err; console.log(err);
});
