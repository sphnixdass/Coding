var Gpio = require('onoff').Gpio; //require onoff to control GPIO
var Pin1 = new Gpio(24, 'out'); //declare GPIO4 an output
var Pin2 = new Gpio(23, 'out'); //declare GPIO4 an output
var fs = require('fs'); //require filesystem to read html files
var url = require('url');

var http = require('http').createServer(function handler(req, res) { //create server

  var path = url.parse(req.url).pathname;
  console.log("css", path);
  switch (path){
    case '/':
  fs.readFile(__dirname + '/index.html', function (err, data) { //read html file
    if (err) {
      res.writeHead(500);
      return res.end('Error loading socket.io.html');
    }

    res.writeHead(200);
    res.end(data);
  });
  break;

  case '/socket.io.js':
  fs.readFile(__dirname + path, function (err, data) { //read html file
    if (err) {
      res.writeHead(500);
      return res.end('Error loading socket.io.html');
    }

    res.writeHead(200);
    res.end(data);
  });
  break;

  case '/bootstrap.min.css':
  fs.readFile(__dirname + path, function (err, data) { //read html file
    if (err) {
      res.writeHead(500);
      return res.end('Error loading socket.io.html');
    }

    res.writeHead(200);
    res.end(data);
  });
  break;

  case '/jquery-3.2.1.slim.min.js':
  fs.readFile(__dirname + path, function (err, data) { //read html file
    if (err) {
      res.writeHead(500);
      return res.end('Error loading socket.io.html');
    }

    res.writeHead(200);
    res.end(data);
  });
  break;

  case '/popper.min.js':
  fs.readFile(__dirname + path, function (err, data) { //read html file
    if (err) {
      res.writeHead(500);
      return res.end('Error loading socket.io.html');
    }

    res.writeHead(200);
    res.end(data);
  });
  break;

  case '/bootstrap.min.js':
  fs.readFile(__dirname + path, function (err, data) { //read html file
    if (err) {
      res.writeHead(500);
      return res.end('Error loading socket.io.html');
    }

    res.writeHead(200);
    res.end(data);
  });
  break;





  }
  

});

var io = require('socket.io')(http) //require socket.io module and pass the http object

http.listen(3010); //listen to port 8080

io.sockets.on('connection', function (socket) {// WebSocket Connection
  var buttonState = 0; //variable to store button state

  socket.on('forward', function (data) { //get button state from client
    console.log("forward pressed")
      Pin1.writeSync(0); //turn LED on or off
      Pin2.writeSync(1);
   
  });

  socket.on('state', function (data) { //get button state from client
    Pin1.writeSync(0); //turn LED on or off
    Pin2.writeSync(0);
 
  });

  socket.on('backward', function (data) { //get button state from client
    Pin1.writeSync(1); //turn LED on or off
    Pin2.writeSync(0);
 
  });


});
