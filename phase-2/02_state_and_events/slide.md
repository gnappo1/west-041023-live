---
presentation:
  width: 1500
  height: 1000
  controls: false
---

<!-- slide -->

<h1> State & Events </h1>

<!-- slide -->

<h2><strong> ✅ Objectives </strong></h2>

- Add event handlers to elements in React

- Use the useState hook to create state variables

- Create event handler callbacks that manipulate state

- Trigger re-renders by setting state

- Distinguish between props and state

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong>Handling events in vanilla JS</strong></h2>

<br>

In vanilla JS, our steps for handling events looked like this:

<br>

```js
// 1. find a piece of DOM:
const pizza = document.getElementById("pizza");
// 2. Add an event listener to that piece
pizza.addEventListener;
// 3. Give type and callback to the event listener:
pizza.addEventListener("click", () => {
  console.log("It's Pizza Time!");
});
```

<br>

In React, we don't have to do step 1, we can skip directly to step 2 by adding event handlers directly to our JSX. We still must supply the event handler with a callback.

<!-- slide style="text-align: left;"-->

<h2 style="text-align: center;"><strong> Handling events in React </strong> </h2>

<br>

```js
const Counter = () => {
  return <button onClick={() => console.log("clicked!")}>Click Me</button>;
};
```

<br>

<strong>NOTE:</strong> Events can only be attached to DOM elements, we can't attach event listeners to our components

<br>

We can also create a helper function for the callback

<br>

```js
const Counter = () => {
  function handleClick(event) {
    console.log(event);
  }

  return <button onClick={handleClick}>Click Me</button>;
};
```

<br>

This is helpful in the case where we need to introduce additional event handling logic. We can do so without cluttering our JSX.

<!-- slide style="text-align: left;"-->

<h2 style="text-align:center;"><strong>✅ Toggle Dark Mode Button</strong></h2>

<br>

Inside the `Header` component, there is a button with textContent of `Dark Mode`

<br>

```js
<button>Dark Mode</button>
```

<br>

Attach an `onClick` event to the button:

<br>

```js
<button onClick={() => console.log("clicked")}>Dark Mode</button>
```

<br>

We can also also refactor using a helper function:

```js

 const handleClick = () => console.log('clicked')

<button onClick={handeClick}>Dark Mode</button>
```

<br>

💡 We need to now figure out how to properly set new text for the button and perform DOM manipulation to reflect the change. That is where `state` will come in.

<!-- slide style="text-align: left;"-->

<h2 style="text-align: center;"><strong>Why is state important?</strong></h2>

<br>

🏹 State is used for data that needs to be dynamic. Where props are passed down from parents to children and are static, values stored in state are meant to change, especially as the user interacts with the DOM.

<br>

🏹 This is a key component of declarative programming in React: we tie our components to our state by integrating values in state into logic (e.g. conditional rendering). This way, changes in state eventually cause changes to the DOM.

<br>

🏹 To work with state in a function component, we use the `useState` hook

<!-- slide style="text-align: left;"-->

<h2 style="text-align: center;"> The useState hook </h2>

<br>

`useState` will return an array of two elements:

- state variable: returns the current value for the state

- setterFunc: a function that will update the value of the state when invoked

<br>

React recommends using [array destructuring]:

```js
const [stateVariable, setterFunc] = useState(someVal);
```

<!-- slide style="text-align: left;"-->

<h2 style="text-align: center;"> Adding state to Header component </h2>

<br>
<br>

```js
const [isDarkMode, setIsDarkMode] = useState(true);
```

<br>

This creates a variable `isDarkMode` that will return `true` initially until it gets updated to a new value

<!-- slide style="text-align: left;"-->

<h2 style="text-align: center;"> Updating State </h2>

<br>

To update a state variable, we use its setter function:

<br>

```js
const handleClick = () => setIsDarkMode(!isDarkMode);
```

<br>
<br>

🛑 Calling the setter function does two things:

1. It updates the state variable to some new value

2. It causes our component to re-render and update the DOM

<br>

Now when we click the button, the state will toggle to the negated version of itself due to the `!` operator.

<!-- slide style="text-align: left;"-->

<h2 style="text-align: center;"> Filter by project name in ProjectList component </h2>

<br>

Currently, we are creating a `ProjectListItem` component for each project inside of the `projects` array:

```js
const projectListItems = projects.map((project) => (
  <ProjectListItem key={project.id} {...project} />
));
```

<br>

We need to make this dynamic by implementing a filter feature that returns the projects based on the users entry in the `search input`

```js
<input type="text" placeholder="Search..." />
```

<br>

<!-- slide style="text-align: left;"-->

<h3 style="text-align: center;"> Filter by project name in ProjectList component steps: </h3>

<br>

1. Initialize state to track the `searchQuery`:

```js
const [searchQuery, setSearchQuery] = useState("");
```

<br>

2. Add on `onChange` event to the input element:

```js
<input onChange={handleSearch} type="text" placeholder="Search..." />
```

<br>

3. Update the state in the `handleSearch` helper function:

```js
const handleSearch = (e) => setSearchQuery(e.target.value);
```

<!-- slide style="text-align: left;"-->

<h3 style="text-align: center;"> Filter by project name in ProjectList component steps contd: </h3>

<br>

<br>

4. Filter the `projects` array to return the search results based on the `searchQuery` value:

```js
const searchResults = projects.filter((project) =>
  project.name.toLowerCase().includes(searchQuery.toLowerCase())
);
```

<br>

5. Update `projectListItems` to use `searchResults`:

```js
const projectListItems = searchResults.map((project) => (
  <ProjectListItem key={project.id} {...project} />
));
```

<br>

<strong>Note:</strong> If the searchQuery is an empty string, the `filter()` will return all the project items

<!-- slide style="text-align: left;"-->

<h2 style="text-align: center;"> 💡 Conclusion </h2>

<br>

Events and state are both important and can work together to allow the DOM to reflect a users interactions and activities by:

1. Attaching events to parts of our JSX

2. Updating the state based on the goal of the event

3. State change forces a re-render that will cause DOM manipulation and reflect the changes on the interface

<br>
<br>

<h4 style="text-align: center;"><strong> user behavior -> update state -> React updates DOM </strong></h4>

<br>
