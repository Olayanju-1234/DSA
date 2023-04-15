function oneAway(string, modified) {
    // replace
    if (string.length === modified.length) {
        return checkReplace(string, modified);
    } 
    // insert
    else if (string.length + 1 === modified.length) {
        return checkInsert(string, modified);
    } 
    // remove
    else if (string.length - 1 === modified.length) {
        return checkInsert(modified, string);
    }
    return false;


}

// check replace function
function checkReplace(string, modified) {
    let foundDifference = false;
    for (let i = 0; i < string.length; i++) {
        if (string[i] !== modified[i]) {
            if (foundDifference) {
                return false;
            }
            foundDifference = true;
        }
    }
    return true;
}

// check insert/remove function
function checkInsert(string, modified) {
    let index1 = 0;
    let index2 = 0;
    while (index2 < modified.length && index1 < string.length) {
        if (string[index1] !== modified[index2]) {
            if (index1 !== index2) {
                return false;
            }
            index2++;
        } else {
            index1++;
            index2++;
        }
    }
    return true;
}

console.log(oneAway("pale", "ple"));
console.log(oneAway("pales", "pale"));
console.log(oneAway("pale", "bale"));
console.log(oneAway("pale", "bake"));
