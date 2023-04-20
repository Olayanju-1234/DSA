var isPalindrome = function(x) {
    let reversed = '';
  
    for (let i = x.length - 1; i >= 0; i--) {
      reversed += x[i];
    }

    return reversed === x;
  };


console.log(isPalindrome("121"));