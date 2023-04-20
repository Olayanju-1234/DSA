// String compression

function stringCompression(string) {
    // string must be letters only
    if (string.match(/[^a-z]/i)) {
        return 'String must be letters only';
    }

    let compressed = '';
    let count = 0;
    for (let i = 0; i < string.length; i++) {
        count++;
        if (string[i] !== string[i + 1]) {
            compressed += string[i] + count;
            count = 0;
        }
    }
    return compressed.length < string.length ? compressed : string;
}

console.log(stringCompression('aabcc23cccaaa'));
console.log(stringCompression('abc'));
console.log(stringCompression('aabbcc'));