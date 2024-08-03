#!/usr/bin/node
/* computes the number of tasks completed by user id. */
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (err, rs, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const tasksList = JSON.parse(body);
  const tasks = {};

  tasksList.forEach(task => {
    if (task.completed) {
      if (!tasks[task.userId]) tasks[task.userId] = 1;
      else tasks[task.userId]++;
    }
  });
  console.log(tasks);
});
