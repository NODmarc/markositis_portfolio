function range(start, end, step) {
    let ans = [];
    if (step == null) {
      for (let i = start; i <= end; i++) {
        ans.push(i);
    }
    return ans;  
    } else if (step > 0) {
        for (let i = start; i <= end; i = step + i) {
            ans.push(i);
        }
        return ans;  
    } else {
        for (let i = start; i >= end; i = step + i) {
            ans.push(i);
        }
        return ans;
    }
    
}

function sum(array) {
    let result = 0
    for (let i = 0; i < array.length; i++) {
        result += array[i]
    }
    return result
}

console.log(range(5, 2, -1))
console.log(sum(range(5, 2, -1)))