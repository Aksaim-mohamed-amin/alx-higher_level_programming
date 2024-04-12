#!/usr/bin/node

/**
 * Concats 2 files.
 */

const fs = require('fs');
const [, , fileA, fileB, fileC] = process.argv;

fs.readFile(fileA, 'utf8', function (errA, dataA) {

  fs.readFile(fileB, 'utf8', function(errB, dataB) {

    const content = dataA + dataB;

    fs.writeFile(fileC, content, 'utf8', function(errWrite) {
      
    });
  });
});
