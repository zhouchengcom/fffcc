/*
 * Minio Cloud Storage (C) 2016 Minio, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import React from 'react'
import ReactDropzone from 'react-dropzone'


export default class Dropzone extends React.Component {
  onDrop(files) {
      console.log(files)
  }

  render() {
    const style = {
      height: '100%',
      borderWidth: '0',
      // borderStyle: 'dashed',
      // borderColor: '#fff',
      width: '100%'
      
    }
    const activeStyle = {
      borderWidth: '2px',
      borderColor: '#777'
    }
    const rejectStyle = {
      backgroundColor: '#ffdddd'
    }

    return (
      <ReactDropzone 
      style={style}
        activeStyle={activeStyle}
        rejectStyle={rejectStyle}
        // disableClick={true}
        onDrop={this.onDrop.bind(this)}>
        {this.props.children}
      </ReactDropzone>
    )
  }
}


