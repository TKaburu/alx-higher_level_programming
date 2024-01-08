#!/usr/bin/node

// console.log('My number: ' prosess.argv[2])

const argv1 = Number(process.argv[2]);

if (!isNaN(argv1)) {
  console.log('My number: ' + Math.floor(process.argv[2]));
} else {
  console.log('Not a number');
}
