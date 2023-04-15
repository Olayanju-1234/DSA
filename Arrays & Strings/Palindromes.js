// Check if a string is permutation of another string

function isPermutation(str1, str2) {
    if (str1.length !== str2.length) {
        return false;
    }

    let str1Map = new Map();
    let str2Map = new Map();


    for (let i = 0; i < str1.length; i++) {
        if (str1Map.has(str1[i])) {
            str1Map.set(str1[i], 
            str1Map.get(str1[i]) + 1);
        } 
        else {
            str1Map.set(str1[i], 1);
        }
    }

    console.log(str1Map);
    

    for (let i = 0; i < str2.length; i++) {
        if (str2Map.has(str2[i])) {
            str2Map.set(str2[i], 
            str2Map.get(str2[i]) + 1);
        } 
        else {
            str2Map.set(str2[i], 1);
        }
    }

    console.log(str2Map);

    for (let [key, value] of str1Map) {
        if (str2Map.get(key) !== value) {
            return false;
        }
    }

    return true;
   

    
}

// function isPermutation(str1, str2) {
//     if (str1.length != str2.length) {
//         return false;
//     }

//     let sort1 = []
//     let sort2 = []

//     for (let i = 0; i < str1.length; i++) {
//         sort1.push(str1[i]);
//     }

//     for (let i = 0; i < str2.length; i++) {
//         sort2.push(str1[i]);
//     }

//     sort1.sort()
//     sort2.sort()

//     console.log(sort1, sort2);
    
//     return true;
    
// }

console.log(isPermutation('accc', 'ccac'));;
