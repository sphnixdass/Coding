const express = require('express');
const { exec } = require('child_process');
var http = require('http'),
    fileSystem = require('fs'),
    path = require('path'),
    util = require('util');

const app = express();
const port = 4000;
let temptext = "hi dass";

app.get('/', (req, res) => {

    const execSync = require('child_process').execSync;
    const stdout = execSync('cat *.js file | wc -l');
    console.log(`stdout: ${stdout}`);


    var result = require('child_process').execSync('ping www.google.com -c 2').toString()
    console.log('result', result);
    var result2 = require('child_process').execSync('ls').toString()
    console.log('result2', result2);

    //handler();

    res.send(result2);
    // console.log('sss', handler());    
})

app.get('/pdf', (req, res) => {
    var filePath = '0071752129.pdf';
    res.writeHead(200, {
        'Content-Type': 'application/pdf',
    });
    var rs = require('fs').createReadStream(filePath);
    rs.pipe(res);
    
})

app.get('/image', (req, res) => {


    //http://localhost:4000/image?pagenumber=5&filename=0071752129.pdf
    var url = require('url');
    var url_parts = url.parse(req.url, true);
    var pagenumber = url_parts.query.pagenumber;
    var filename = url_parts.query.filename;
    console.log('pagenumber', pagenumber, filename);

    const execSync = require('child_process').execSync;
    console.log('gs -sDEVICE=jpeg -dNOPAUSE -dBATCH -sOutputFile=temp.jpeg -dFirstPage=' + pagenumber + ' -dLastPage=' + pagenumber + ' -r300x300 -f "' + filename + '"');
    const stdout = execSync('gs -sDEVICE=jpeg -dNOPAUSE -dBATCH -sOutputFile=temp.jpeg -c "{1 exch sub}{1 exch sub}{1 exch sub}{1 exch sub} setcolortransfer" -dFirstPage=' + pagenumber + ' -dLastPage=' + pagenumber + ' -r300x300 -f "' + filename + '"');
    console.log(`stdout: ${stdout}`);
    res.writeHead(200, {
        'Content-Type': 'image/jpeg',
    });
    var rs = require('fs').createReadStream('temp.jpeg');
    rs.pipe(res);
    //gs -sDEVICE=jpeg -dNOPAUSE -dBATCH -sOutputFile=temp.jpeg -dFirstPage=4 -dLastPage=4 -r200x200 -f 0071752129.pdf

})

app.get('/bellTone', (req, res) => {
    //console.log('req', req);
    var url = require('url');
    var url_parts = url.parse(req.url, true);
    var pagenumber = url_parts.query.pagenumber;
    var filename = url_parts.query.filename;
    console.log('pagenumber', pagenumber, filename);

    const execSync = require('child_process').execSync;
    console.log('python3 DassPDFreadder.py ' + pagenumber + ' "' + filename + '"');
    const stdout = execSync('python3 DassPDFreadder.py ' + pagenumber + ' "' + filename + '"');
     console.log(`stdout: ${stdout}`);

    var filePath = 'file.mp3';
    res.writeHead(200, {
        'Content-Type': 'audio/mp3',
    });
    var rs = require('fs').createReadStream(filePath);
    rs.pipe(res);
}
)


app.post('/PdfPageLoad', function (req, res) {
    res.send('Got a POST request')
})


app.listen(port, () => console.log('server listening on prot ', port))

