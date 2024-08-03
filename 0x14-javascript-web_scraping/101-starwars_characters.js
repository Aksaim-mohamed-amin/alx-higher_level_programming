#!/usr/bin/node
/* Prints all characters of a Star Wars movie */
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';

request(apiUrl, function (err, rs, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const characters = JSON.parse(body).characters;
  characters.forEach(charcterUrl => {
    request(charcterUrl, function (err, rs, body) {
      if (err) console.error('Error:', err);
      else console.log(JSON.parse(body).name);
    });
  });
});
