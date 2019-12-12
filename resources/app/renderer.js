// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.
const fs = require('fs');
const os = require('os');
const { dialog } = require('electron').remote
const ipc = require('electron').ipcRenderer;
var child_process = require('child_process');
pythonPathParameter = ''
imageContainer = document.getElementById('imageContainer');

const fileSelectButton = document.getElementById('SelectFiles');
fileSelectButton.addEventListener('click', function(){
    dialog.showOpenDialog({
        properties: ['openFile', 'multiSelections',]
      }).then(result => {
        console.log(result.canceled)
        pythonPathParameter = result.filePaths[0]
        console.log(result.filePaths)
        console.log(result)
      }).catch(err => {
        console.log(err)
      })
})
counter = 0
const runButton = document.getElementById('Run');
runButton.addEventListener('click', function(){
  counter += 1
  CacheBreaker = "background-image: url('../../test.png" + counter + "');" + 'background-size: contain; background-repeat: no-repeat; background-position: center;'
  file = 'resources\\app\\dist\\quality\\quality.exe ' + pythonPathParameter;
  child_process.execSync(file);
  newFileName = 'test.png' + counter
  fs.renameSync('test.png', newFileName)
  imageContainer.style.cssText = CacheBreaker
//   imageContainer.classList.remove('image');
//   imageContainer.classList.add('image');
  console.log('done')
})
