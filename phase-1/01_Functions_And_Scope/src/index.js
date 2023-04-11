//Data 
const inventory = [
    {
      id: 1,
      title: 'Eloquent JavaScript: A Modern Introduction to Programming',
      author: 'Marjin Haverbeke',
      price: 10.00,
      reviews: [{userID: 1, content:'Good book, but not great for new coders'}],
      inventory: 10,
      imageUrl: 'https://images-na.ssl-images-amazon.com/images/I/51IKycqTPUL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg'
    },
    {
      id: 2,
      title: 'JavaScript & JQuery: Interactive Front-End Web Development',
      author: 'Jon Duckett',
      price: 45.75,
      reviews: [{userID: 15, content:'good way to learn JQuery'}],
      inventory: 2,
      imageUrl: 'https://images-na.ssl-images-amazon.com/images/I/31SRWF+LkKL._SX398_BO1,204,203,200_.jpg'
    },
    {
      id: 3,
      title: 'JavaScript: The Good Parts',
      author: 'Douglas Crockford',
      price: 36.00,
      reviews: [{userID: 25, content:'I disagree with everything in this book'}, {userID: 250, content:'Only JS book anyone needs'}],
      inventory: 8,
      imageUrl: 'https://images-na.ssl-images-amazon.com/images/I/5131OWtQRaL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg'
    },
    {
      id: 4,
      title: 'JavaScript: The Definitive Guide',
      author: 'David Flanagan',
      price: 25.50,
      reviews: [{userID: 44, content:'Great intro to js book'}, {userID: 350, content:'It really is the Definitive guide'}],
      inventory: 0,
      imageUrl: "https://images-na.ssl-images-amazon.com/images/I/51wijnc-Y8L._SX379_BO1,204,203,200_.jpg"
    },
    {
      id: 5,
      title: 'You Don’t Know JS',
      author: 'Kyle Simpson',
      price: 6.00,
      reviews: [{userID: 76, content:'You can find this for free online, no need to pay for it!'}],
      inventory: 7,
      imageUrl: 'https://images-na.ssl-images-amazon.com/images/I/41T5H8u7fUL._SX331_BO1,204,203,200_.jpg'
    }, 
    {
      id: 6,
      title: 'Learn Enough JavaScript to Be Dangerous',
      author: 'Michael Hartl',
      price: 24.00,
      reviews: [{userID: 50, content:'pretty good'}],
      inventory: 5,
      imageUrl: 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQyf6xSyTHc7a8mx17ikh6GeTohc88Hn0UgkN-RNF-h4iOwVlkW'
    },
    {
      id: 7,
      title: 'Cracking the Coding Interview',
      author: 'Gayle Laakmann McDowell',
      price: 49.95,
      reviews: [{userID: 99, content:'One of the most helpful books for taking on the tech interview'}, {userID: 20, content: 'Great but I just wish it was in JavaScript instead of Java' }],
      inventory: 20,
      imageUrl: 'https://images-na.ssl-images-amazon.com/images/I/41oYsXjLvZL._SY344_BO1,204,203,200_.jpg'
    }
  ]
  
  // ✅ Function ideas:
  /*
  - helloWorld
  - formatPrice(price)
  - blurb(book)
  */
  
  // Start here!
  
  
  // ✅ create a formatPrice(price) function that accepts a price (number) as an argument and returns the price formatted as a string.
  // formatPrice(10) => '$10.00'
  
  
  // ✅ create a blurb() function that accepts a book as an argument and returns a string in the following format:
  // 'Eloquent JavaScript: A Modern Introduction to Programming by Marjin Haverbeke is on sale for $10.00'
  
  // 💡 Difference between Block scope, Function scope, and Global scope
  const globalVariable = "I am global"
  
  function scopey() {
    var a = "first Value";
    let b = "first Value";
    const c = "first Value";
    d = "first Value";
  
    if (true) {
      var a = "second Value";
      let b = "second Value";
      const c = "second Value";
      d = "second Value";
    }
  
    // what will each statement log to the console?
    console.log("a (var) is,", a);
    console.log("b (let) is,", b);
    console.log("c (const) is,", c);
    console.log("d (evil) is,", d);
  }
  
  // 💡 Arrow functions vs regular functions
  
  // ✅ create an arrow function version of the formatPrice function

  
  // After Break
  
  // 💡 Practice using callbacks for iteration
  
  // ✅ Create an array of the prices of all of the books
  
  // ✅ Create an array of simplified book objects

  // ✅ Create an array of strings from the inventory in the following format:
  // 'Eloquent JavaScript: A Modern Introduction to Programming by Marjin Haverbeke is on sale for $10.00'
  
  // 💡 When do I use forEach vs map?