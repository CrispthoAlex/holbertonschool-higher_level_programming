#!/usr/bin/node
// Write a script that reads and prints the content of a file
const file = process.argv[2];
const fs = require('fs');

if (file) {
  // Asynchronous version of fs.readFile. Returns the contents of the filename
  fs.readFile(file, 'utf8', (err, data) => {
    if (err) {
      console.log(err)
    } else console.log(data);
  });
}
