#!/usr/bin/node

const fs = require('fs');

const file = process.argv[2];

fs.readFile(file, 'utf-8', (error, data) => {
  error ? console.error(error) : console.log(data);
});
