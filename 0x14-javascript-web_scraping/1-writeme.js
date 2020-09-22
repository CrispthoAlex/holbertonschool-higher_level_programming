#!/usr/bin/node
// script that writes a string to a file
const fileTowrite = process.argv[2];
const text = process.argv[3];
const fs = require('fs');

if (fileTowrite) {
  fs.writeFileSync(fileTowrite, text, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    } else console.log(data);
  });
}
