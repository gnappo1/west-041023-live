# JS Fundamentals Pt. 1

## SWBAT
- Use comments appropriately
- Use console.log, debugger, and node to test and debug JavaScript
- Define all JavaScript data types
- Implement JavaScript conditionals
- Implement `for` and `while` loops
- Perform CRUD operations on Arrays
- Perform CRUD operations on Objects

### Debugging Tools
- Comments   
```js
// Comments begin can with a double backslash. They are used to leave notes in the code that will be ignored when the program is executed. 
```
- Console.log
```js
// A method outputs a message to the web console
console.log('welcome to phase-1 JavaScript);
```
- Debugger 
```js
// A statement that adds a breakpoint to your code. A breakpoint pauses your code in the middle of execution
debugger;
```
- Node
```js
//Typing node in your terminal opens a REPL (Read-Eval-Print Loop). This allows you a small environment to test out tiny bits of code.
node
```

## JavaScript Types
- Strings 🧵
```js
// Used for characters 

'rose is cute'
"rose is cute"
`rose is cute`
```
- Number 🔢
```js
// Integers, Floats(Real numbers)
// The maximum safe integer in JavaScript (2^53 - 1).
// NaN(Not a number) has the datatype of number 😓 
42
42.01
Infinity
-Infinity
NaN
```

- BigInt
```js
// Numbers that are too large for number
Number.MAX_SAFE_INTEGER
// 9007199254740991
BigInt(9007199254740991)
// 9007199254740991n
```
- Booleans ✅ 🚫
```js
// Logic, true or false values 
true 
false
```
- Undefined 
```js
//values assigned to variables that have been declared but not assigned a value
let a 
// undefined 

```
- Null
```js
// Represents an absence of a value
```
- Symbols 
```js
// These are Not emoji
//  Symbols are often used to add unique property keys to an object
// 
```
Falsy values
```js
!!0
//false
!!""
//false
!!null
//false
!!undefined 
//false
!!NaN
//false
```
Truthy values 
```js
!!{}
// true
!![]
// true
!!42
// true
!!"rose"
//true
!!Infinity
//true
!!true
//true
```

## Variables 
```js
// Never use var
var cat = 'rose'

// variables defined with const can't be reassigned 
const bestCat = 'rose'

// variables defined with lets can be reassigned 

let someCat = 'tom'
someCat = 'rose'

```

## Conditionals 
```js
// The if statement executes if a condition is truthy

if(true) {
    console.log('rose is cute')
};

// if...else will execute the first block if the condition is true, else it will execute the second blog

if(cat == 'rose'){
    console.log('rose is cute!')
} else {
    console.log(`${cat} is cute`)
};

// else if can have multiple conditions

if(weather == 'sunny'){
    console.log('go for a walk')
} else if (weather == 'raining') {
    console.log('stay inside and read')
} else if (weather == 'snow') {
    console.log('make hot coco')
} else {
    console.log('¯\_(ツ)_/¯')
}

```

## Arrays (Object Data Type)
Arrays are list-like objects with indexes and elements. 
Each element has a specific index starting from 0. 
```js
// Arrays can be defined with []
// It can start empty or with elements pre-populated
const arr = [];
const arr = [1,2,3];


//Accessing arrays
//bracket notation
arr[0]

//Adding items to arrays
arr.push(4)
arr.unshift(0)
arr.splice(1, 0,, 6)

//Removing items from arrays
arr.pop()
arr.shift()
arr.splice(2,2);

//Does not mutate the original array
arr.slice(2);

//Make a copy of the array
arr2 = [...arr]
arr3 = [...arr, 7]

```

## Looping Through Arrays
```js
// a for loop is a classic loop for looping through every index of an array
for(let i = 0; 0 < arr.length; i++){
    console.log(arr[i])
}

// a for each loop loops through every element in the array without needing 'let i = 0; 0 < arr.length; i++'
for(element of arr){
    console.log(element)
}
```

## Object (Object Data Type)
Object is a data type that's used to store other data. Arrays are a type of object. A typical Object has key-value pairs. Much like an Array has indexes that contain values, Objects have keys (also known as properties) that hold value. 

```js
//Creating objects
//Objects can start as an empty pair of {} or with default data
const obj = {username: 'matteo', faveFood: {food:'pasta', serving: 150}}

//New properties can be added using dot notation or bracket notation 
obj.favToys = ['banana-plush', 'feather stick']
obj['age'] = 10

//Bracket notation allows variables to be passed in for keys
let owner = 'the boss'
obj[owner]

// {username: 'rose', faveToys:['banana-plush', 'feather stick'], age:10, owner:'ix'}

//Accessing properties 
//Properties can be access through dot or bracket notation
obj.username //rose
obj['owner'] // ix

//Accessing nested properties
obj.favToys[1] // 'feather stick'
obj.favFood.food // 'nulo'

//Updating properties 
obj.age = 11

//Delete object property  
delete obj.age 

```
## Looping Through Objects
```js
// a for loop is a classic loop for looping through every key/value of an object
for(let i = 0; i < Object.values(obj).length; i++){
 console.log(Object.values(obj)[i])
}

// a for of loop loops through every element in the array without needing 'let i = 0; 0 < arr.length; i++'
for(element of Object.values(obj)){
    console.log(element)
}
```