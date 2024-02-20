#!/usr/bin/node

const fs = require('fs').promises;

const filepath = process.argv[2];

// The second argument is the string to write

const string = process.argv[3];

// write to file
fs.writeFile(filepath, string, 'utf8', (err, data) => {
    // handle error casses
    if (err) {
        console.error(err);
        return;
      }
      console.log(data);
});
