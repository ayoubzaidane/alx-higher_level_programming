#!/usr/bin/node
const argument = process.argv[2];
const parsedNumber = parseInt(argument);

if (!isNaN(parsedNumber)) {
  console.log(`My number: ${parsedNumber}`);
} else {
  console.log('Not a number');
}
