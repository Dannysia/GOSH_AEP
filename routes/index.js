var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/image/:img', function(req, res, next){
  res.sendFile('/home/danny/express/public/images/'+req.params["img"]+'.JPG');
});

module.exports = router;