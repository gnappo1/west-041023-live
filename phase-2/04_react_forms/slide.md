---
presentation:
  width: 1500
  height: 1000
  controls: false
---

<!-- slide -->

<h2><strong> React Forms 📝 </strong></h2>

<!-- slide -->

<h2><strong> ✅ Objectives </strong></h2>

- Explain why we use controlled forms (vs uncontrolled forms)

- Implement a controlled form

- Use form data to update state in a parent component

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> What is a controlled input </strong></h2>

<br>

In React, rather than looking into the DOM to get the form's input field values when the form is submitted, we use state to monitor the user's input as they type, so that our component state is always in sync with the DOM.

<center><img src="https://res.cloudinary.com/dnocv6uwb/image/upload/v1646072384/controlled-forms_j69gpu.svg" alt="controlled input diagram" height="500" width="1000"></center>

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> Making an input controlled </strong></h2>

<br>

To keep track of each input's value, you need:

1. State for the input that will manage the input's value

2. An `onChange` listener attached to the input to monitor users behavior and update state as the user interacts with the field

3. A `value` attribute on the input that corresponds to a key in state

And for the form itself, you need an `onSubmit` listener on the form to finally submit data.

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> 🛠️ ProjectForm setup </strong></h2>

<br>

1. For each input element in the form, create a new state variable:

<br>

```js
const [name, setName] = useState("");
const [about, setAbout] = useState("");
const [phase, setPhase] = useState("");
const [link, setLink] = useState("");
const [image, setImage] = useState("");
```

<br>

❗ Most common approach (and cleanest) is to create a state object with key/value pairs associated with each form field:

```js
const [formData, setFormData] = useState({
  name: "",
  about: "",
  phase: "",
  link: "",
  image: "",
});
```

<!-- slide style="text-align: left;" -->

2. Add an onChange handler for each input field using a helper function:

<br>
<br>

Example:

```js
<input type="text" id="about" onChange={handleOnChange} />
```

<br>

🤯 If using individual pieces of state for form fields, a separate helper function will be created for each corresponding field.

Example:

```js
<input type="text" id="about" onChange={handleAbout} />
```

<br>

```js
<input type="text" id="phase" onChange={handlePhase} />
```

<!-- slide style="text-align: left;" -->

3. Connect the `value` attribute of each input field to the corresponding state variable:

<br>
<br>

Example:

```js
<input
  type="text"
  id="about"
  onChange={handleOnChange}
  value={formData.about}
/>
```

<br>
<br>

❗<strong>Note:</strong> The reason `formData.name` is being used is because the state variable is an object named `formData`. To access the value of a key within the object, dot notation is used.

<!-- slide style="text-align: left;" -->

4. Adding a `name` attribute to the input fields:

<br>
<br>

```js
<input
  type="text"
  id="about"
  onChange={handleOnChange}
  value={formData.about}
  name="about"
/>
```

<br>
<br>

❗ <strong>IMPORTANT: </strong> The `name` attribute needs to match with the key created in the state object in order to update the value. If the key in the state object is 'about' then the `name` attribute for the corresponding input field should be `about` as well

<!-- slide style="text-align: left;" -->

5. Updating the state when the onChange occurs (aka when the user begins typing or changing parts of the form):

<br>
<br>

```js
const handleOnChange = (e) => {
  // e.target will return an object, the element that triggered the event with properties
  // including name and value. Object destructuring is used to extract that values from e.target

  // This is the same as doing:
  // const name = e.target.name
  // const value = e.target.value

  const { name, value } = e.target;

  // The setter function is then invoked and a new object will  be created with the 
  // contents of the previous formData spread and the new key/value added to avoid overwriting the 
  // previous form field values

  setFormData((formData) => ({ ...formData, [name]: value }));
};
```

<!-- slide style="text-align: left;" -->

6. On the `<form>` element, add an `onSubmit` listener with a `handleSubmit` helper function that will run when the form is submitted:

<br>
<br>

```js
<form className="form" autoComplete="off" onSubmit={handleSubmit}></form>
```

<br>

```js
const handleSubmit = (e) => {
  e.preventDefault();
};
```

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> 🔑 After the form has been submitted </strong></h2>

<br>

The state of `projects` is defined inside of the parent component `App` and the behavior occurs in the child component `ProjectForm`. When the new project is submitted, `projects` will need to be updated to include it.

<!-- slide style="text-align: left;" -->

Here is where the process of inverse data flow will need to occur:

<br>

1. Create a helper function in `App` component called `onAddProject` that will update the `projects` state:

<br>

```js
const onAddProject = (newProject) => {
  setProjects([...projects, newProject]);
};
```

<br>

`projects` is an array so to update the state, a new array will be created with the elements of the original `projects` array spread and the new project passed to `onAddProject` added as a new element

<br>

Pass `onAddProject` as a prop to `ProjectFrom` from within `App` component:

```js
<ProjectForm onAddProject={onAddProject} />
```

<!-- slide style="text-align: left;" -->

Inside the `ProjectForm` component, destructure `onAddProject` from the props and invoke it from within the `handleSubmit` function, passing it the formData object:

<br>

```js
const handleSubmit = (e) => {
  e.preventDefault();
  onAddProject(formData);

  // after we have delivered the formData to the App component and updated state
  // clear the form by setting the values back to empty strings:

  setFormData({
    name: "",
    about: "",
    phase: "",
    link: "",
    image: "",
  });
};
```

<!-- slide style="text-align: left;" -->

<h2 style="text-align: center;"><strong> 💡 Conclusion </strong></h2>

<br>

State is a very integral part of the way that React applications operate and DOM manipulation to occur. React prefers using state to update the forms and keep track of the form fields values, making them controlled inputs. What our user sees in the input fields reflects the value of the state associated with that field. 

