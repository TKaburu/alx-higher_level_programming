#!/usr/bin/node

const argv1 = Number(process.argv[2]);

// check if converting to number was successful
if (!isNaN(argv1)) {
  console.log('My number: ' + Math.floor(process.argv[2]));
} else {
  console.log('Not a number');
}
