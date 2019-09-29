var express = require('express');
var router = express.Router();
var sqlite3 = require('sqlite3').verbose()
var db = new sqlite3.Database(':memory:')

/* GET temps listing. */
router.get('/', function(req, res, next) {

  db.serialize(function () {
    db.run('CREATE TABLE lorem (info TEXT)')
    var stmt = db.prepare('INSERT INTO lorem VALUES (?)')

    for (var i = 0; i < 10; i++) {
      stmt.run('Ipsum ' + i)
    }

    stmt.finalize()

    db.each('SELECT rowid AS id, info FROM lorem', function (err, row) {
      console.log(row.id + ': ' + row.info)
    })
  })

  db.close()

  res.send('Did some db stuff');
});

module.exports = router;
