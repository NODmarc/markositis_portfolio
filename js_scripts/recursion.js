function isEven(pam) {
    if (pam == 0) {
        return console.log('even');
    } else if (pam == 1) {
        return console.log('odd');
    } else {
        return isEven(pam - 2)
    }
 }

console.log(isEven(0))
