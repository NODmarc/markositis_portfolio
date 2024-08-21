let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

function reverseArray(array) {
    let new_array = []
    for (let i = array.length - 1; i >= 0; i--) {
        new_array.push(i);
    }
    return new_array;
}


function reverseArrayInPlace(array) {
    for (let i = array.length - 1; i >= 0; i--) {
        array.push(array[i]);
    }
    array.splice(0, array.length/2);
    return array;
}

console.log(reverseArrayInPlace(nums))
