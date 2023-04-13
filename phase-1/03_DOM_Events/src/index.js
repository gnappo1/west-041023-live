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
// Event Listeners/Handlers (Behavior => Data => Display)
////////////////////////////////////////////////////////////////
