#!/usr/bin/node

const fs = require('fs');

const filepath = process.argv[2];

// read the file
fs.readFile(filePath, 'utf8', (err, data) => {
    // handle error casses
    if (err) {
        console.error(err);
        return;
      }
      console.log(data);
});
