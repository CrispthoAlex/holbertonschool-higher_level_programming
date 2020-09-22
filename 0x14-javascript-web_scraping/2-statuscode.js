#!/usr/bin/node
// Write a script that display the status code of a GET request.
const url = process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
