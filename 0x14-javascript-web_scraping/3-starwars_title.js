#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + id, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
