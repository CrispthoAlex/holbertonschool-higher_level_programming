#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number
// matches a given integer
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');

if (file) {
  request(url, (error, response, body) => {
    if (error) console.log(error);
    else {
      fs.writeFileSync(file, body, 'utf8', (err) => {
        if (err) console.log(err);
      });
    }
  });
}
