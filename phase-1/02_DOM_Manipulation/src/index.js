//BookStore has been moved to data.js 
console.log(bookStore);

function formatPrice(price) {
  return '$' + Number.parseFloat(price).toFixed(2);
}

// CRUD
    // Retrieve
        // Accessing An Existing Element on the Page
        //! querySelector() -> can target by id, class, position, etc
        //! getElementById() -> only targets elements that have an id
        // TODO Create a function that sets the text content of the header to the bookstore name.
        function setHeader(name) {
            const h1 = document.querySelector("div#header div h1")
            h1.innerText = bookStore.name
        }
        setHeader()
        // TODO Create a function that grabs all the divs from the footer. Render the bookstore name, address, and hours
        function changeFooter() {
            const divName = document.getElementById("store")
            divName.innerText = bookStore.name
            const divAddress = document.getElementById("address")
            divAddress.innerText = bookStore.address
            const divNumber = document.getElementById("number")
            divNumber.innerText = bookStore.number
        }
        changeFooter()
        //TODO Think of a way to refactor and DRY out the previous function (think of forEach)

        // Accessing Existing ElementS on the Page
        //! querySelectorAll() -> can target by id, class, position, etc
        document.querySelectorAll("footer div") // returns a NodeList, you can use forEach on it but no other iterators
        //! getElementsByClassName() -> only targets elements that have an id
        document.getElementsByClassName("red") // returns an HTMLCollection, you cannot use forEach or any other iterators
        //! getElementsByTagName() -> can select all elements that are of a specific html tag type (e.g. <p>)
        document.getElementsByClassName("p") // returns an HTMLCollection, you cannot use forEach or any other iterators
        //* TO TRANSFORM A HTMLCollection OR NodeList into an Array use Array.from(collectionToTransformHere)

    // Create
        // Creating a new Node and Add it to the DOM
        //! document.createElement() -> takes a string representing the element to create (e.g. document.createElement("p"))
        //! append -> can append multiple elements at the same type (string, number, node, etc)
        //! appendChild -> more restictive, only one Node can be appended at the time
        //TODO Create a new Node with some random text and append it to the DOM
        function addParagraph() {
            const p = document.createElement("p") // I just created a new orphan node
            p.innerText = "Something random!"
            p.id = "random"
            document.querySelector("main").appendChild(p)
            document.querySelector("main").append(p, "a string here", 7)
        }
        addParagraph()

    // Update
        // Update Existing Content by Targeting the Node and then using:
        //! innerText -> is also aware of style and will not return the text of hidden elements, whereas textContent will.
        //! textContent -> gets the content of all elements, including <script> and <style> elements
        //! innerHTML -> includes the HTML markup and deserves a special WARNING
        function changeHeader() {
            const h1 = document.querySelector("div#header div h1")
            h1.innerText = "A new name"
        }
        changeHeader()
        //TODO Showcase the difference between innerText, textContent, innerHTML, outerHTML
        console.log("InnerHTML: ", explanation.innerHTML)
        console.log("OuterHTML: ", explanation.outerHTML)
        console.log("InnerText: ", explanation.innerText)
        console.log("TextContent: ", explanation.textContent)
        //! Differences:
        //* Note that while textContent gets the content of all elements, including <script> and <style> elements, the mostly equivalent IE-specific property, innerText, does not.
        //* innerText is also aware of style and will not return the text of hidden elements, whereas textContent will.
        //* As innerText is aware of CSS styling, it will trigger a reflow, whereas textContent will not.
        //* InnerHTML will include the entire HTML code inside the element selected
        //* InnerHTML will include the entire HTML code inside the element selected and include the element itself

    // Destroy
        // Remove a Node from the page
        //! remove() -> removes a node from the page
        // TODO Remove an element of your choice from the DOM
        function removeEl(){
            const h1 = document.querySelector("div#header div h1")
            h1.remove()
        }
        // removeEl()
        
// 💡 Exercise After Break

    // create a function called renderBook(book)
    // it will take a book object as an argument
    // and create the html struture for rendering 
    // that book and insert it into our webpage!

    // function renderBook(book) {
    // should create an li element that looks something like this:
    // <li class="list-li">
    //   <h3>Eloquent JavaScript : A Modern Introduction to Programming</h3>
    //   <p>Marjin Haverbeke</p>
    //   <p>$10.00</p>
    //   <img src="https://images-na.ssl-images-amazon.com/images/I/51IKycqTPUL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg" alt="Eloquent JavaScript cover"/>
    //   <button>Delete</button>
    // </li>

  function renderBook(book){
    const li = document.createElement("li")
    li.className = "list-li"
    const h3 = document.createElement("h3")
    h3.innerText = book.title
    const p1 = document.createElement("p1")
    p1.innerText = book.author
    const p2 = document.createElement("p2")
    p2.innerText = formatPrice(price)
    const img = document.createElement("img")
    img.src = book.imageUrl
    img.alt = book.title + 'cover'
    const btn = document.createElement("btn")
    button.innerText = "Delete"
    li.append(h3, p1, p2, img, btn)
  }