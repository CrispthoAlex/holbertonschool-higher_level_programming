#!/usr/bin/node
// script that computes the number of tasks completed by user id.
const url = process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const listTasks = JSON.parse(body);
    const dictTask = {};
    for (const task of listTasks) {
      const keyId = task.userId;
      if (task.completed) {
        if (dictTask[keyId]) { dictTask[keyId] += 1; } else { dictTask[keyId] = 1; }
      }
    }
    console.log(dictTask);
  }
});
