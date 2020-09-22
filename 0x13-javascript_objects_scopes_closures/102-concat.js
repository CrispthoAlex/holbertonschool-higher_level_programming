#!/usr/bin/node
// Write a script that concats 2 files
const fileA = process.argv[2]
const fileB = process.argv[3]
const fileC = process.argv[4];
const fs = require('fs');

if (fileA && fileB && fileC) {
  // Synchronous version of fs.readFile. Returns the contents of the filename
  const txtA = fs.readFileSync(fileA);
  const txtB = fs.readFileSync(fileB);
  const txtC = txtA + txtB;

  /* Asynchronously writes data to a file, replacing the file if it
     already exists. data can be a string or a buffer
  */
  fs.writeFileSync(fileC, txtC);
}
