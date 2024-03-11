#!/usr/bin/node

const args = process.argv.slice(2).map(Number); // Convert command-line arguments to numbers

if (args.length < 2) {
  console.log(0);
} else {
  // Remove duplicates and sort the numbers in descending order
  const sortedUniqueNumbers = Array.from(new Set(args)).sort((a, b) => b - a);

  // Print the second biggest integer
  console.log(sortedUniqueNumbers[1]);
}
