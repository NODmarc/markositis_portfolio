"use strict";


// let someNumber = Math.floor(Math.random() * 10) + 1
// while(someNumber !== 10) {
//     console.log(`Your number is ${someNumber}`)
//     someNumber = Math.floor(Math.random() * 10) + 1
//     if (someNumber === 10) {
//         console.log("Win!")
//     }
// }


// Start(1) -> output: [0]
// Start(2) -> 0, 1 -> output: [0, 1] 
            //f0, f0 + 1
// Start(3) -> 0, 1, 0 + 1 -> output: [0, 1, 1]
            // f0, f0 + f1, f0 + f0 + f1
// Start(4) -> 0, 1, 0 + 1, 1 + (0 + 1) -> output: [0, 1, 1, 2]
// Start(5) -> 0, 1, 0 + 1, 1 + (0 + 1), 0 + 1 + (1 + (0 + 1)) -> output: [0, 1, 1, 2, 3]
            // f0, f1, f0 + f1, f1 + (f0 + f1), f0 + f1 + (f1 + (f0 + f1))
// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
// 0, 1, 0+1, 1+0+1, 1+0+1+0+1, 1+0+1+1+0+1+0+1, 1+0+1+0+1+1+0+1+1+0+1+0+1  
            

const f0 = 0
const f1 = 1
const sum_01 = f0 + f1

// function fibonachi(n) {
//     if (n === 1) {
//         output.push(f0)
//     } else if (n === 2) {
//         output.push(f0, f0 + 1)
//     } else {
//         output.push(f0)
//         output.push(f1)
//         for(let n = 1; n < 10; n++) {
//             let sum1 = f0 + f1 + n 
//             let result = sum1
//             output.push(result)
//         }
//     }
// }

// fibonachi(10)
// console.log(output)

function fibonacciGenerator (n) {

    let output = []

    if (n === 1) {
        output[f0]
    } else if (n === 2) {
        output[f0, f0 + 1]
    } else {
        output = [0, 1]
        for (let i = 2; i < n; i++) {
            output.push(output[output.length - 2] + output[output.length - 1]) 
        }
    }
    return output
}

let result = fibonacciGenerator(100)
console.log(result)