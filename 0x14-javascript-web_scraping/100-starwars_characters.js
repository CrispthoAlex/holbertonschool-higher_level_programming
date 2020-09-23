#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const movId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movId;
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const listChar = JSON.parse(body).characters;
    for (const apiPerson of listChar) {
      request(apiPerson, (error, response, body) => {
        if (error) { console.log(error); } else { console.log(JSON.parse(body).name); }
      });
    }
  }
});
