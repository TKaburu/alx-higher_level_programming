#!/usr/bin/node

const argv1 = Number(process.argv[2]);

if (!isNaN(argv1)) {
  for (let x = 0; x < argv1; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
