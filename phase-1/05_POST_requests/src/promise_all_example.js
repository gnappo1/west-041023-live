let storeFetch = fetch('http://localhost:3000/stores/1')
  .then((res) => res.json())

let booksFetch = fetch("http://localhost:3000/books")
  .then((res) => res.json())

// load all the books and render them
Promise.all([storeFetch, booksFetch])
  .then((bookStore, books) => {
    renderHeader(bookStore)
    renderFooter(bookStore)

    books.forEach(book => renderBook(book))
  })
  .catch(err => {
    console.error(err);
    makeError('Make sure to start json-server!')
  });

function makeError(message) {
  const main = document.querySelector('main');
  const errorDiv = document.createElement('div');
  errorDiv.className = "error";
  errorDiv.textContent = message;
  main.prepend(errorDiv);
  window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
      errorDiv.remove();
    }
  })
}
