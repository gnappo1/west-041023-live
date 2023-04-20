console.log("Hello World!")

//! Globals

const searchForm = document.querySelector("#search-form")
const results = document.querySelector("#results")
const showDetails = document.querySelector("#show-details")

//! Helper Functions

const handleClick = (e, show) => {
    // container
    const card = document.createElement("div")
    card.id = "show-details-card"
    // span for votes
    const spanVotes = document.createElement("div")
    spanVotes.id = "show-votes"
    spanVotes.textContent = `Rating: ${show.score.toFixed(2)}/5`
    // p for summary
    const p = document.createElement("p")
    p.id = "show-details-summary"
    p.innerHTML = show.show.summary

    // button for external link to more details
    const a = document.createElement("a")
    a.id = "show-more-details"
    a.href = show.show.url

    card.append(spanVotes, p, a)
    showDetails.innerHTML = ""
    showDetails.append(card)
}

const displayShow = (showObj) => {
    //* create the card container (div)
    const card = document.createElement("div")
    card.className = "card"
    //* create the header for the name (h2/h3)
    const h2 = document.createElement("h2")
    h2.className = "show-name"
    h2.textContent = showObj.show.name
    //* create an img pointing to one of the images
    const img = document.createElement("img")
    img.className = "show-img"
    img.src = showObj.show?.image?.medium || "https://i.pinimg.com/originals/e1/d4/8e/e1d48ec79bbc30fc35f124a4c7eed1f3.jpg"
    img.alt = `${showObj.show.name} deals with ${showObj.show.summary}`
    //* create a couple of spans for premiereDate and endedDate (if it did end)
    const spanPremiere = document.createElement("span")
    spanPremiere.className = "show-premiered"
    spanPremiere.textContent = showObj.show.premiered || "Not premiered yet!"

    const spanEnded = document.createElement("span")
    spanEnded.textContent = showObj.show.ended || "Still running!"
    spanEnded.className = "show-ended"
    //* add "more details" button
    const btn = document.createElement("button")
    btn.className = "more-details"
    btn.textContent = "More Details"
    btn.addEventListener("click", e => handleClick(e, showObj))

    const br1 = document.createElement("br")
    const br2 = document.createElement("br")
    const br3 = document.createElement("br")
    //* assemble them correctly
    card.append(h2, img, br1, spanPremiere, br2, spanEnded, br3, btn)
    //* put the card on the page
    results.append(card)
}

const handleSubmit = (e) => {
    e.preventDefault()
    //* Figure out what the user just typed AND ENCODE IT!!!!!
    const userInput = encodeURI(e.target['search'].value)
    //* finally, make this fetch call already!
    fetch(`https://api.tvmaze.com/search/shows?q=${userInput}`)
    .then(resp => resp.json())
    .then(showsArray => showsArray.forEach(show => displayShow(show)))
    e.target.reset()
}



//! Attach Listeners
searchForm.addEventListener("submit", handleSubmit)