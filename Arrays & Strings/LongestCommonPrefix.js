// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

function longestCommonPrefix(strs) {
    for (let i = 0; i < strs.length; i++) {
        if (strs[i] === "") {
            return "";
        }
    }
    let prefix = "";
    let firstWord = strs[0];
    for (let i = 0; i < firstWord.length; i++) {
        for (let j = 1; j < strs.length; j++) {
            // console.log(firstWord[i], strs[j][i]);
            if (firstWord[i] !== strs[j][i]) {
                return prefix;
            }
        }
        prefix += firstWord[i];
    }
    return prefix;
}

console.log(longestCommonPrefix(["flower","flow","flight"]));