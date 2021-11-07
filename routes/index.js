var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/image/:img', function(req, res, next){
  res.sendFile('/home/danny/express/public/images/'+req.params["img"]+'.JPG');
});

router.get('/getLocations/', function(req, res, next) {
  var mysql = require('mysql')
  var connection = mysql.createConnection({
    host: 'localhost',
    user: 'danny3',
    password: 'password',
    database: 'vision',
    insecureAuth: true
  })

  connection.connect()

  connection.query('SELECT Latitude, Longitude, ImageID FROM PoleImages;', function (err, rows, fields) {
    if (err) throw err
    res.send(rows)
  })

connection.end()
});


module.exports = router;