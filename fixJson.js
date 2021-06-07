const { json } = require('express');
const fs = require('fs');
const dJSON = require('dirty-json');
const r = dJSON.parse("{ test: 'this is a test'}")
console.log(JSON.stringify(r));
 


fs.readFile('test.txt', 'utf8' , (err, data) => {
    if (err) {
      console.error(err)
      return
    }
    else{
        let new_data = dJSON.parse(data)
        console.log(JSON.stringify(new_data))
    }
  })