---
presentation:
  width: 1500
  height: 1000
  controls: false
---

<!-- slide -->

<h2><strong> Side Effects and Data Fetching 💻 </strong></h2>

<!-- slide -->

<h2><strong> ✅ Objectives </strong></h2>

- Use the useEffect hook to fetch data

- Understand Component side effects

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> What to know before discussing side effects? </strong></h2>

<br>

React components are 'pure functions'. This means that given an input (such as a prop), the return is 100% predictable

<br>

```js
const Greeting = ({ name }) => {
  return <h1> Hello, {name} </h1>;
};

export default Greeting;
```

<br>

Any time Greeting is called, and provided a new prop, we will always be able to predict the output, regardless of the prop value

<br>

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> What is a side effect? </strong></h2>

<br>

"We perform a side effect when we need to reach outside of our React components to do something. Performing a side effect, however, will not give us a predictable result."

https://www.freecodecamp.org/news/react-useeffect-absolute-beginners/

<br>

The term 'side effect' not only applies to React but to all functional programming.

<br>

“A side effect is anything that affects something outside the scope of the function being executed ” - Michael W. Brady

<br>

💡 These are operations that will still affect our component but can't specifically happen during the rendering

<br>

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> Examples of React component side effects </strong></h2>

<br>

- Fetching Data from a server

- Interacting with a browsers API like the `document` or `window`

- Utilizing interval timers such as `setInterval` or `setTimeout`

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> 🛠️ useEffect() hook </strong></h2>

<br>

- `useEffect()` runs both upon the first render and then with every re-render after but only based on the rules set inside the dependency array

<br>

- Takes in two arguments:

  - A callback function defining the logic to be executed as a side effect(the 'effect')

  - A dependency array that defines when the side effect should occur. This argument is optional and does not always need to be provided

<br>

- `useEffect()` is essentially telling React that the component needs to do something else AFTER the component has rendered

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> 1️⃣ useEffect() hook without a dependency array  </strong></h2>

<br>

```js
useEffect(() => {
  // Some effect to occur
});
```

<br>

- In this example, only 1 argument is passed to useEffect

- The dependency array which is the optional second argument is left out

- That means that upon every render and re-render, this side effect will also execute

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> 2️⃣ useEffect() hook with an empty dependency array  </strong></h2>

<br>

```js
useEffect(() => {
  // Some effect to occur
}, []);
```

<br>

- In this example, the dependency array is passed as the second argument

- The dependency array is empty with no provided value

- That means that the side effect will only run one time, upon the initial render of the component and no more after that. Even if the component is re-rendered

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> 3️⃣ useEffect() hook with a value provided to the dependency array  </strong></h2>

<br>

```js
useEffect(() => {
  // Some effect to occur
}, [data]);
```

<br>

- In this example, the dependency array is passed a piece of data. This data can be either a prop or a state variable

- That means that the side effect will run once upon the components initial render and then only re-run when the value of the provided data changes

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> Fixing App component with useEffect</strong></h2>

<br>

🛑 Current problem: To load all the projects into the Project showcase application, a user must click on the 'load projects' button

<br>

👍 Solution: Perform a side effect that will fetch the projects from the API and set the `projects` state to the response from the request

<br>

```js
useEffect(() => {
  fetch("http://localhost:4000/projects")
    .then((res) => res.json())
    .then((projects) => setProjects(projects));
}, []);
```

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> 🔺 Common Mistakes with useEffect </strong></h2>

<br>

❗ Why are we not including `projects` like:

What happens here?

<br>

```js
useEffect(() => {
  fetch("http://localhost:4000/projects")
    .then((res) => res.json())
    .then((projects) => setProjects(projects));
}, [projects]);
```

<br>

❓or here?

```js
useEffect(() => {
  fetch("http://localhost:4000/projects")
    .then((res) => res.json())
    .then((projects) => setProjects(projects));
};
```

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> Cleaning up 🧹 </strong></h2>

<br>

- There will be some code that is necessary to clean up after the component is no longer being mounted on the DOM. AKA turning off our side effects

- Why? To avoid 'memory leaks' which means using memory for data that is no longer necessary

- Examples: Timeouts, subscriptions, event listeners

- Happens on a couple of occasions:

  - When the component initially mounts, it will run the cleanup function before the effect function inside `useEffect()`

  - After a re-render but before the effect function runs again: if there is any cleanup defined, it will run this first

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> Cleanup example </strong></h2>

<br>

```js
const Timer = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    let timer = setTimeout(() => {
      setCount((count) => count + 1);
    }, 1000);

    return () => clearTimeout(timer);
  }, []);

  return <h1>I've rendered {count} times!</h1>;
};
```

<br>

When the component unmounts from the DOM or mounts for the first time, it is ensured that the timeout has been cleared

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> 💡 Conclusion </strong></h2>

<br>

Side effects are essential parts of a components functionality but not necessarily an action that needs to parttake in the rendering of the component. These are 'effects' that are going to happen after the component has rendered to the DOM. We can utilize the built in React hook `useEffect()` to indicate what actions we would like to run after our component has rendered. There are a few ways to set rules on when these effects should occur by using the dependency array which is the optional second argument provided to the `useEffect()` hook.

<br>
