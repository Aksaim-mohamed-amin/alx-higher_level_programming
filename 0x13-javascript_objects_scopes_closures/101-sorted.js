#!/usr/bin/node

/**
 * Imports a dictionary of occurrences by user id
 * and computes a dictionary of user ids by occurrence.
 */
const dict = require('./101-data').dict;
const occurrencesDict = {};
for (const userId in dict) {
  const occurrence = dict[userId];

  if (!occurrencesDict[occurrence]) {
    occurrencesDict[occurrence] = [userId];
  } else {
    occurrencesDict[occurrence].push(userId);
  }
}
console.log(occurrencesDict);
