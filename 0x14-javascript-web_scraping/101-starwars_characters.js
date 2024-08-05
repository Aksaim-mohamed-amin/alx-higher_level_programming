#!/usr/bin/node
/* Prints all characters of a Star Wars movie */
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';

const printName = function (charsList, i) {
  if (charsList.length <= i) return;

  request(charsList[i], function (err, rs, body) {
    if (err) console.error('Error:', err);
    else {
      console.log(JSON.parse(body).name);
      printName(charsList, ++i);
    }
  });
};

request(apiUrl, function (err, rs, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const charsList = JSON.parse(body).characters;
  printName(charsList, 0);
});
