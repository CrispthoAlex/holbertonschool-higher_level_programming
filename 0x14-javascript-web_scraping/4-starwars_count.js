#!/usr/bin/node
// script that prints the number of movies where the character Wedge Antilles is present.
const movId = 'https://swapi-api.hbtn.io/api/people/18/';
const url = process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const listFilms = JSON.parse(body).results;
    let count = 0;
    for (const elem of listFilms) {
      const persons = elem.characters;
      for (const person of persons) {
        if (person === movId) count += 1;
      }
    }
    console.log(count);
  }
});
