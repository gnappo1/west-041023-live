"use strict" // use to enforce a stricter set of rules and best-practices

// JS Fundamentals Part 1

// Single Line Comments 
/*
    Multi Line Comments
*/
// Toggle comments using cmd + ? (mac) OR cntr + ? (pc)
// ! Special type of comment!

// Console Logging
console.log("Hello") // print to browser's console some values

// Debugging
//debugger // place it in your code to freeze execution and take a look at existing values

// Variables
    // var DO NOT USE: re-declare: YES, re-assign: YES
    var test = "I should not be used!"
    // implicit global  DO NOT USE (the variable has never been declared before and you forgot to type let/const)
    // re-declare: YES, re-assign: YES
    implicitGlobal = "test"
    // let: re-declare: NO, re-assign: YES
    let name = "Matteo"
    // const: re-declare: NO, re-assign: NO
    const age = 9


// Data Types
// String: ', ", `
    console.log(`Hello, ${name}`) // string interpolation
    console.log('Hello, ' + name) // string concatenation

// Number
    const age2 = 12
    const price = 12.99

// Bigint
    // Numbers out of the +-2^53 - 1

// Boolean
    // Falsey Values
    false
    0
    ""
    null
    undefined
    NaN
    -0
    0n

// Null
    // Indicates the absence of a value

// Undefined
    // Indicates that a value has not been assigned yet

// Symbol
    // Useful data type to optimize memory usage, and used to set up keys on objects

// Object (Structural Type)
  // Array (unshift, slice, push, splice, pop, shift, length)
    let temps = [1, 2, 3, 4]
    console.log(temps[-1])

  // Object (Object.keys(), Object.values(), Object.entries(), Object.assign(), Object.freeze(),)
    let obj = {name: "Matteo", age: 21}
    console.log(obj['name']) // Matteo
    console.log(obj['random']) // undefined

// Conditional Statements
    if (true) {
      alert("WOW!") 
    } else if (7 != 9) {
        alert("Ciao!")
    } else {
        alert("I alert for any other case!")
    }

// Ternary Expression
    // return name === "Matteo" ?  "yes" : "NO"

// Loops
    // for
    for (let i = 0; i < temps.length; i++) {
        console.log(temps[i])
    }

    //while
    let i = 0
    while (i < temps.length) {
        console.log(temps[i])
        // i++
    }

