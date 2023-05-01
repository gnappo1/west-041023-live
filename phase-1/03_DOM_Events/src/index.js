//! Suggestions When Working With the DOM

//TODO 1. Set global selector variables at the top of the file for everyone to use
//TODO 2. Attach event listeners to the correct DOM nodes
//TODO 3. Decide if creating the callback anonymously in-place OR pass a function reference (promotes reusability)
//TODO 4. Does the callback have access to all the data it needs or should it receive parameters?

////////////////////////////////////////////////////////////////
// Yesterday's Code
////////////////////////////////////////////////////////////////

console.log(bookStore);

function formatPrice(price) {
  return '$' + Number.parseFloat(price).toFixed(2);
}
function setHeader() {
    const h1 = document.querySelector("#store-name")
    h1.innerText = bookStore.name
}
function changeFooter() {
    const divName = document.getElementById("store")
    divName.innerText = bookStore.name
    const divAddress = document.getElementById("address")
    divAddress.innerText = bookStore.address
    const divNumber = document.getElementById("number")
    divNumber.innerText = bookStore.number
}
function addParagraph() {
    const p = document.createElement("p") // I just created a new orphan node
    p.innerText = "Something random!"
    p.id = "random"
    document.querySelector("main").appendChild(p)
    document.querySelector("main").append(p, "a string here", 7)
}
function removeEl(){
    const h1 = document.querySelector("div#header div h1")
    h1.remove()
}
function changeHeader() {
    const h1 = document.querySelector("div#header div h1")
    h1.innerText = "A new name"
}
function renderBook(book) {
    const li = document.createElement("li")
    li.className = "list-li"
    const h3 = document.createElement("h3")
    h3.innerText = book.title
    const pAuthor = document.createElement("p")
    pAuthor.innerText = book.author
    const pPrice = document.createElement("p")
    pPrice.innerText = formatPrice(book.price)
    const img = document.createElement("img")
    img.src = book.imageUrl
    img.alt = book.title
    const button = document.createElement("button")
    button.innerText = "Delete"
    li.append(h3, pAuthor, pPrice, img, button)
    // figure out where
    // target that place with querySelector/getElementById
    const ulList = document.getElementById("book-list")
    // append
    ulList.appendChild(li)
}
function renderBookAsHTML(book) {
    const ulList = document.getElementById("book-list")
    ulList.innerHTML += `
    <li class="list-li">
        <h3>${book.title}</h3>
        <p>${book.author}</p>
        <p>${formatPrice(book.price)}</p>
        <img src=${book.imageUrl} alt=${book.title}/>
        <button>Delete</button>
    </li>
    `
}

setHeader()
changeFooter()
bookStore.inventory.forEach(bookObj => renderBookAsHTML(bookObj))
// bookStore.inventory.forEach(renderBook) this line leverages JS magic BUT IT'S IDENTICAL TO THE ONE ABOVE

////////////////////////////////////////////////////////////////
// Today's Code
// Event Listeners/Handlers (Behavior => Data => Display)
////////////////////////////////////////////////////////////////
//! Generic Syntax For Attaching Event Listeners

// domNodeElement.addEventListener(theEventInStringformat, callbackFunctionThatDesidesWhatToDo)
const toggleBtn = document.querySelector("#toggleForm")
const form = document.querySelector("#book-form")

//! Pattern 1: create the function somewhere to promote reusability
//! then pass the function as a callback to addEventListener
// const handleClick = e => {
//     // debugger
//     const isVisible = form.classList.toggle("collapsed")
//     if (isVisible) {
//         toggleBtn.innerText = "Add Book"
//     } else {
//         toggleBtn.innerText = "Hide Form"
//     }
    
// }
// toggleBtn.addEventListener("click", handleClick) //! DO NOT TYPE () after the function name or it would not be a callBACK anymore. It would be invoked immediately and not when the event actually triggers.

//! Pattern 2: create the callback function in-place, make it anonymous, and IF YOU WANT use an arrow function for readability.
toggleBtn.addEventListener("click", () => {
    //! If the event object is not needed, you can omit it like above
    // debugger
    //! classList returns an array-like structure that shows all the classnames available on the element specified
    const isVisible = form.classList.toggle("collapsed")
    //! toggle returns a boolean based on whether the classname is actually present on the element or not
    if (isVisible) {
        toggleBtn.innerText = "Add Book"
    } else {
        toggleBtn.innerText = "Hide Form"
    }
})

form.addEventListener("submit", e => {
    e.preventDefault() // prevent the submit event from refreshing the page
    //! You can extract the value of inputs inside a form using . notation and the input's name/id properties if in camel-case notation
    //! You can extract the value of inputs inside a form using [] notation and the input's name/id properties independently of the notation
    const title = e.target.title.value
    const author = e.target.author.value
    const price = e.target.price.value
    const imageUrl = e.target.imageUrl.value
    const inventory = e.target.inventory.value
    //! Package the data into an object because the renderBook functions expect an object as argument
    const bookObj = {
        title,
        author,
        imageUrl,
        price,
        inventory
    }
    bookStore.inventory.push(bookObj) //* desperate attempt to persist the book across page rerendering! The correct way will be showcased next week!
    renderBookAsHTML(bookObj) //* put new book on the page
    e.target.reset() //* empty each input in the form
    form.classList.toggle("collapsed") //* toggle visibility

})

window.addEventListener('keydown', e => {
    if (e.key === "Escape") {
        
        //! form.classList.add("collapsed") could be enough but let's use a conditional statement OR ternary expression to make sure 
        !form.classList.contains("collapsed") ? form.classList.add("collapsed") : null

        //! the above is equivalent to
        // if (!form.classList.contains("collapsed")) {
        //     form.classList.add("collapsed")
        // }
    }
})