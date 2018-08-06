import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import { FilePond, File, registerPlugin } from "react-filepond";

import "./css/welcome.css";

import "./css/main.css";
import upload_logo from "./svg/upload.svg";
import Dropzone from "./Dropzone";
// Our app
class Main extends Component {
  constructor(props) {
    super(props);

    this.state = {
      files: []
    };
  }

  render() {
    return (
      <div className="main">
        <div id="page-one" className="effect--fadeIn">
          <div className="title">私密、安全的文件分享服务</div>
          <div className="description">
            <div>
              通过安全、私密且受加密的链接发送文件，链接到期后文件将从网上彻底抹除。
            </div>
            <a
              href="https://testpilot.firefox.com/experiments/send"
              className="link"
            >
              详细了解
            </a>
          </div>
          <Dropzone>
            <div className="uploadArea">
              {/* <Dropzone> */}
              <img src={upload_logo} title="上传" />
              <div className="uploadArea__msg">把文件拖到到此处开始上传</div>
              <span className="uploadArea__sizeMsg">
                为保证运行稳定，建议文件大小不超过 1GB
              </span>
              <label
                title="选择一个要上传的文件"
                for="file-upload"
                className="btn btn--file"
              >
                选择一个要上传的文件
              </label>
              {/* </Dropzone> */}
            </div>
          </Dropzone>
        </div>
      </div>
    );
  }
}

export default Main;
