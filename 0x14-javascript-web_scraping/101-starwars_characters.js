#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const movId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movId;
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const list = getName(body);
    for (const elem of list) {
      request(elem, (error, response, body1) => {
        if (error) { console.log(error); } else { console.log(JSON.parse(body1).name); }
      });
    }
  }
});

function getName (body) {
  const listChar = JSON.parse(body).characters;
  const returnList = [];
  for (const apiPerson of listChar) {
    request(apiPerson, (error, response, body1) => {
      if (error) { console.log(error); } else { returnList.push(JSON.parse(body1).name); }
    });
  }
  return listChar;
}
