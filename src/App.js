import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import { FilePond, File, registerPlugin } from "react-filepond";

import "./css/welcome.css"

import "./css/header.css"
// Register the image preview plugin

import send_logo from './svg/send_logo.svg';
import Main from "./Main"
// Our app
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      files: []
    };
  }

  render() {
    return (
      <div className="App">
        <header className="header">
          <div className="logo">
            <a href="/" className="logo__link">
              <img src={send_logo} alt="Send" />
              <h1 className="logo__title">Send</h1>
            </a>
            <div className="logo__subtitle">
              <a
                href="https://testpilot.firefox.com"
                className="logo__subtitle-link"
              >
                Firefox Test Pilot
              </a>
              <div>Web 实验</div>
            </div>
          </div>
          
        </header>

        <Main/>
      </div>
    );
  }
}

export default App;
