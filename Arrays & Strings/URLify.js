function replaceString(strings) {
    strings = strings.trim();
    let newString = "";
    for (let i = 0; i < strings.length; i++) {
        if (strings[i] === " ") {
            newString += "%20";
        } else {
            newString += strings[i];
        }
    }
    return newString;
    
}

console.log(replaceString("Mr John Smith    "));