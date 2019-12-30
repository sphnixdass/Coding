import React from 'react';
import './PdfDisplay.css';
import { Grid } from '@material-ui/core';


class PdfDisplay extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      "page": 4,
      "ipaddress": "192.168.1.3",
      "filename": "0071752129.pdf",
      "playspeed": 1.5,
      "chkbox": true
    };


    // state = {};
    this.handlePrevious = this.handlePrevious.bind(this);
    this.handleNext = this.handleNext.bind(this);
    this.pageChange = this.pageChange.bind(this);
    this.speedchange = this.speedchange.bind(this);
    this.bookchange = this.bookchange.bind(this);
    this.handleChangeChk = this.handleChangeChk.bind(this);
  }


  handlePrevious() {
    const audioEl = document.getElementsByClassName("audio-element")[0]
    audioEl.pause();
    audioEl.currentTime = 0;
    audioEl.load();
    audioEl.playbackRate = this.state.playspeed;
    audioEl.play()
    const cuspage = document.getElementById("customerPagenumber");
    cuspage.value = this.state.page;
    this.setState({ page: this.state.page - 1 });
  }

  pageChange() {
    const cuspage = document.getElementById("customerPagenumber");

    this.setState({ page: parseInt(cuspage.value) });

    const audioEl = document.getElementsByClassName("audio-element")[0]
    audioEl.pause();
    audioEl.currentTime = 0;
    audioEl.load();
    audioEl.playbackRate = this.state.playspeed;
    audioEl.play()

  }
  handleNext() {
    console.log('next handle called');

    const cuspage = document.getElementById("customerPagenumber");
    cuspage.value = this.state.page;
    const audioEl = document.getElementsByClassName("audio-element")[0]
    audioEl.pause();
    audioEl.currentTime = 0;
    audioEl.load();
    audioEl.playbackRate = this.state.playspeed;
    audioEl.play()


    this.setState({ page: this.state.page + 1 });


  }

  speedchange(event){
    this.setState({ playspeed: event.target.value });
  }

  bookchange(event)
  {
    this.setState({ filename: event.target.value });
  }
  handleChangeChk(event)
  {
    this.setState({ chkbox: event.target.value });
  }
  componentDidMount() {


    const audioEl = document.getElementsByClassName("audio-element")[0]

    audioEl.addEventListener("ended", this.handleNext);

  }

  mainrender() {
    return (
      <>
        <button onClick={this.handlePrevious}>&lt;</button>
        <input style={{width: "30px"}} id="customerPagenumber"></input>
        {/* <TextField id="customerPagenumber" label="Outlined" variant="outlined" /> */}
        <button onClick={this.pageChange}>Get</button>

        <select id="speed" onChange={this.speedchange} value={this.state.playspeed}>
                  <option value="1">1</option>
                  <option value="1.2">1.2</option>
                  <option value="1.3">1.3</option>
                  <option value="1.4">1.4</option>
                  <option value="1.5">1.5</option>
                  <option value="1.6">1.6</option>
                  <option value="1.7">1.7</option>
                  <option value="1.8">1.8</option>
                  <option value="1.9">1.9</option>
                  <option value="2">2</option>
               </select>
               <input type="checkbox" defaultChecked={this.state.chkbox} onChange={this.handleChangeChk} ></input>
<button onClick={this.handleNext}>{this.state.page} + &gt;</button>
               <select id="ebook" onChange={this.bookchange} value={this.state.filename}>
                  <option value="/home/dass/ebooks/007159762X.pdf">Basic English</option>
                 <option value="/home/dass/ebooks/0071462937.pdf">Intermediate English Grammar for ESLLearners</option>
                  <option value="/home/dass/ebooks/0071492321.pdf">Just Enough ENGLISH GRAMMAR</option>
                  <option value="/home/dass/ebooks/0071497846.pdf">American Idioms Dictionary</option>
                  <option value="/home/dass/ebooks/0071752129.pdf">English Verb Tenses</option>
                  <option value="/home/dass/ebooks/0071763031.pdf">English Vocabulary for Beginning</option>
                  <option value="/home/dass/ebooks/0071791248.pdf">English Problem Solver</option>
                  <option value="/home/dass/ebooks/0071823026.pdf">Google Maps</option>
                  <option value="/home/dass/ebooks/0071840184.pdf">Essential ESL Dictionary</option>
                  <option value="/home/dass/ebooks/111890866X.pdf">PYTHON PROJECTS</option>
                  <option value="/home/dass/ebooks/0596804849.pdf">Ubuntu: Up and Running</option>
                  <option value="/home/dass/ebooks/1119028752.pdf">The Antivirus Hacker’s Handbook</option>
                  <option value="/home/dass/ebooks/1430248211.pdf">Learn Raspberry Pi with Linux</option>
                  <option value="/home/dass/ebooks/1449323073.pdf">Learning Node</option>
                  <option value="/home/dass/ebooks/1484225163.pdf">Python, PyGame and Raspberry Pi</option>
                  <option value="/home/dass/ebooks/1484228014.pdf">The Blender Python API</option>
                  <option value="/home/dass/ebooks/1491928999.pdf">Node.js for Embedded Systems</option>
                  <option value="/home/dass/ebooks/9780071492478.pdf">Linux: The Complete Reference</option>
                  <option value="/home/dass/ebooks/9781430258872.pdf">Smart Home Automation with Linux and Raspberry Pi</option>
                  <option value="/home/dass/ebooks/9781484201824.pdf">Mastering the Raspberry Pi</option>
                  <option value="/home/dass/ebooks/9781506149523.pdf">GRAMMAR REFERENCE FOR ESL STUDENTS</option>
                  <option value="/home/dass/ebooks/9781599664040.pdf">4000 Essential english words</option>
                  
               </select>



        
        <div>
       
          {this.state.chkbox?
          <audio controls="controls" className="audio-element">
            {console.log('audiorending', "http://" + this.state.ipaddress + ":4000/bellTone?pagenumber=" + parseInt(this.state.page) - 1 + "&filename=" + this.state.filename)}
            <source src={"http://" + this.state.ipaddress + ":4000/bellTone?pagenumber=" + (parseInt(this.state.page) - 1) + "&filename=" + this.state.filename}></source>
          </audio>:""}
        </div>
        <img width='100%' src={"http://" + this.state.ipaddress + ":4000/image?pagenumber=" + this.state.page + "&filename=" + this.state.filename}></img>
      </>
    )

  }

  render() {


    let mainrender = null;
    mainrender = this.mainrender();

    return (
      <div className="App">

        <Grid container spacing={1}>
          <Grid item xs={12}>
            {mainrender}
          </Grid>
        </Grid>
      </div>
    );
  }
}
export default PdfDisplay;