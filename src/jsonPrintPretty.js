function readJson(path) {
  try {
    const fs = require("fs");
    return JSON.parse(fs.readFileSync(path));
  } catch (err){
    return undefined;
  }
}
  

let jsonContent = readJson(process.argv[2]);
console.table(jsonContent)