#!/usr/bin/node
/* Prints the number of movies where the character “Wedge Antilles” is present. */
const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

request(apiUrl, function (err, rs, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;
  films.forEach(film => {
    if (film.characters.includes(characterUrl)) {
      count++;
    }
  });
  console.log(count);
});
