#!/usr/bin/node

exports.esrever = function (list) {
  let newList = ''; let i = 0;

  while (i < list.length / 2) {
    newList = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = newList;
    i++;
  }
  return list;
};
