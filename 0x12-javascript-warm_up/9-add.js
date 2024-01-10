#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

// convert arguments to numbers
const argv1 = Number(process.argv[2]);
const argv2 = Number(process.argv[3]);

// check if conversion to numbers failed
if (!isNaN(argv1) && !isNaN(argv2)) {
  add(argv1, argv2);
} else {
  console.log(NaN);
}
