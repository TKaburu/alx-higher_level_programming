#!/usr/bin/node

function fact (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
const argv1 = Number(process.argv[2]);

if (!isNaN(argv1)) {
  console.log(fact(argv1));
} else {
  console.log(1);
}
