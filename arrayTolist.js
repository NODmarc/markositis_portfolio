function arrayToList(...value) {
    let list = {
        value: value[0],
        rest: {
            value: value[1],
            rest: {
                value: value[2],
                rest: null
            }
        }
    }
    return list;
}

function listToArray(list) {
    let array = [];
    let currentNode = list;
    while (currentNode !== null) {
        array.push(currentNode.value);
        currentNode = currentNode.rest;
    }
    return array;
}
console.log(arrayToList(1, 2, 3))
console.log(listToArray(arrayToList(1, 2, 3)))