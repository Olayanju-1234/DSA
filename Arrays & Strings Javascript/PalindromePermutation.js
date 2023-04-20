// permutation of a palindrome
// Given a string, write a function to check if it is a permutation of a palindrome.

function palindromePermutation(str) {
    let charMap = {};
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        if (charMap[str[i]]) {
            charMap[str[i]]++;
        } else {
            charMap[str[i]] = 1;
        }
    }
    for (let key in charMap) {
        if (charMap[key] % 2 !== 0) {
            count++;
        }
    }
    return count <= 1;
}

console.log(palindromePermutation("tact coa"));
