//people shouldnt ask why I did this in JS :>
const {faker} = require("@faker-js/faker");
const fs = require('fs');

suffixes = ['exe', 'png', 'jpg', 'jpeg', 'mp4', 'mp3', 'avi', 'xml', 'css', 'html', 'js', 'py', 'json', 'csv', 'xlsx', 'pptx', 'docx', 'txt', 'pdf']
filenames = []
for(let i = 0; i < 100; i++){
    filenames.push(faker.word.noun() + "." + suffixes[Math.floor(Math.random() * suffixes.length)])
}
fs.writeFile('files.txt', filenames.join("\n"), { flag: 'w+' }, err => {console.log(err)});