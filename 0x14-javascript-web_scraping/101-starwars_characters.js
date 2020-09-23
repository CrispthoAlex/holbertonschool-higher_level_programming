#!/usr/bin/node
// script that prints all characters of a Star Wars movie
// in the same order of the list characters in the /films/ response
const movId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movId;
const request = require('request');

// https://javascript.info/async-await
request(url, async (error, response, body) => {
  if (error) console.log(error);
  else {
    const listChar = JSON.parse(body).characters;
    for (const elem of listChar) {
      console.log(await getName(elem));
    }
  }
});

// https://javascript.info/promise-basics
function getName (apiPerson) {
  const promise = new Promise((resolve, reject) => {
    request(apiPerson, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body).name);
    });
  });
  return promise;
}
