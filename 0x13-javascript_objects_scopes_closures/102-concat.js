#!/usr/bin/node

/**
 * Concats 2 files.
 */

const fs = require('fs');
const [, , fileA, fileB, fileC] = process.argv;

fs.readFile(fileA, 'utf8', function (errA, dataA) {
  fs.readFile(fileB, 'utf8', function (errB, dataB) {
    fs.writeFile(fileC, dataA + dataB, 'utf8', function (errWrite) {});
  });
});
