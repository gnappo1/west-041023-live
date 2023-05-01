# Functions
## SWBAT
- [ ] Describe what functions are and their central importance in JS
- [ ] Review syntax differences between regular functions and arrow functions
- [ ]Explain the difference between:
    - [ ] Block scope
    - [ ] Function scope
    - [ ] Global scope
- [ ] Understand what it means that a function are first- class -objects
- [ ] Explain what a higher-order function is
- [ ] Grasp the relationship betweenDescribe what a callback and higher-order functions is


<p align="center">
    <img src="../../assets/functions.jpeg" width="250" height="250">
</p>


## Deliverables 

Easley's Technical Books has asked us to build them an inventory management tool for their employees. 

Today we will work on functions that may help us accomplish some tasks related to displaying data on the application. 


The variable inventory is an array of book objects in index.js. Inventory[0] is the following book.
```
        {
            id:1,
            title: 'Eloquent JavaScript: A Modern Introduction to Programming',
            author: 'Marjin Haverbeke',
            price: 10.00,
            reviews: [{userID: 1, content:'Good book, but not great for new coders'}],
            inventory: 10,
            imageUrl: 'https://images-na.ssl-images-amazon.com/images/I/51IKycqTPUL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg',
            
        }
```

- Demo Function Decoration: 
    - Declare a function that takes a book as a parameter and returns the book's price formatted to look like currency. Given inventory[0] the return should be '$10.00"
    
- Demo Function Expressions: 
    - Create a function Expression that takes a book as a parameter and returns a string consisting of the title and author of the book. Given inventory[0] the return should be 'Title: Eloquent JavaScript: A Modern Introduction to Programming by Marjin Haverbeke'
- Demo arrow functions pt1: 
    - Create an arrow function that takes a book as a parameter and returns a string noting a book is on sale. Given inventory[0] the return should be 'Eloquent JavaScript: A Modern Introduction to Programming by Marjin Haverbeke is on sale!'
-  Demo arrow functions pt2: 
    - Create an arrow function that takes a discount and a book as parameters. Return the book price divided by the discount. Given inventory[0] and 2 the return should be 5.00
- Demo Scope: 
    - Create a variable in the global scope and set it to a book's title. 
    - Create a function that takes title, price, author, and imageUrl as parameters. 
    - Create a variable in function scope and set it to an empty object. 
    - Assign the object the properties of title, price, and author with their values set to their corresponding parameters. Add a key of inventory and set it to 0, and a key of reviews set to an empty array. 
    - Create a conditional statement that checks whether the imageUrl has a value. If it has a value, give the object the property of imageUrl with its value set to the parameter. Else create a variable with the value of 'placeHolderImage.jpg' within block scope and give the object property of imageUrl set to the variable in block scope. (Note: we can give the parameter a default value here, but this section's purpose is to demo scope.)

    - Return book object 
    - Invoke the function with arguments and pass it to inventory.push so the return value is added to the inventory array.
    - Show the different levels of scope using console.logs or debuggers. Where do we have access to variables declared in global scope? Where do we have access to variables declared in function scope? Where do we have access to variables declared at the block level? What does local scope mean?
- Demo Callbacks
    - Create a function that takes a callback function and an array
    - Inside the function create a variable and set it to an empty array.
    - Loop through the array property. Within the block, invoke the callback function and pass it to the array element as an argument.
    - The return value of the callback should be pushed to the new array variable.
    - Return the new array variable. 
    - Test the function by passing the inventory array and one of our previous functions as its callback. (The function must take a single book as a parameter)
- Bonus
    - Demo .map as a practical example of callbacks. 



## Functions
Functions are like a little program. They consist of a set of statements/tasks and return a value or undefined. 

```
// This is a function delcoration 
// This function is returning the string of 'hi'
function sayHi() {
    return 'hi'
}
//This is a function reference but it doesn't actually run the function. 
sayhi

// To run or call or invoke (all the same thing). Write the functions name and add a pair of ()
sayHi()

// This functions console.logs the string of 'hello' but returns undefined because it does not have the return keyword.

function sayHello(){
    console.log('hello')
}

sayHello()

// logging and returning are not the same thing. A return value becomes the value of an invoked function, while a console.log only logs something to the console. 

```

Functions can take unique localized variables called parameters. When the function is invoked, it's passed an argument that becomes the parameter's value.

```

function squareNumb(num){
    //num is the parameter, it is scoped to the inside of the function
    return num*num
}
// 2 is the argument. The value of num in the above function becomes 2.
squareNumb(2)


// functions can take multiple parameters.
function addTwo(num1, numb2){
    return num1 + num2
}
addTwo(5,10)

```

Arrow functions are another way to declare functions with some added benefits.

```
// An arrow function can avoid {} if it's return done on a single line or with () 
// An arrow function with a single paramater doesn't need the () around the paramater. 
const faveFood = food =>  `My fave food is ${food}`
const faveFood = food => (
     `My fave food is ${food}`
)
faveFood('cookies')

```

Arrow functions also have the added benefit of passing context, but we won't be covering that today. 

## Callbacks and HigherOrder Functions 

Functions in JavaScript are treated like any other variable. When functions are treated like this, we refer to them as First class. One of the most significant benefits of this is that functions in JavaScript can be passed as arguments to other functions.

```
// A function that returns a function is called a Higher-Order Function.

const outsideFunction = () => {
    return () => {
        //inside function
    }
}

//A function that is taken as an argument is a callback 

const opening => (openingVideo, credits){
    return openingVideo(credits)
}

const taskingHistory(){
    //... video functionality here
}

const crashCourse(){
    //... video functionality here
}

opening(crashCourse, 'Hank Green')

```