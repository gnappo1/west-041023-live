# Events
## SWBAT
- [ ] Explain the importance of event handling in modern web applications
- [ ] Explain how callback functions are used with event listeners
- [ ] Observe how to add a form to a webpage using HTML and JavaScript
- [ ] Observe how onSubmit events are used to receive information from Users via forms
- [ ] Explain the purpose of .preventDefault() method
- [ ] Use MDN to discover and implement JavaScript events

## Deliverables 

- Demo a simple event:
    - Add an eventListener to an element and log the event object. Do something simple as an example before integrating events into the application. (Such as a click that console.logs)
- Demo click event and remove 
    - In renderBookCard, add an event listener to the Delete button.
    - Add a callback that removes the li. You can do this through the li itself or the event.target.parentElement
- Demo Forms and Submit
    - Select the form with the id of ‘book-form’.
    - Add a submit eventListener.
    - Pass the eventListener a callback that handles the form.
    - The callback takes the event as a parameter.
    - It should prevent the form's default behavior.
    - It should build a book object using the event object through the name attribute (e.target.title.value), the id attribute (note the ids are in kabab case so you’ll need to select the id with bracket notation (e.target[form-title].value) or index of the input (e.target[0].value)
    - Call renderBook and pass it the new book object.
- Demo DOMContentLoaded
    - Add a DOMContentLoaded eventListener to the document and wrap the code within the callback function
- Bonus
	- Create a new store object with the same properties as BookStore.
	- Add a button that toggles the store information to a different store.
	- Add eventListener for a click that toggles the store info in the header and footer to the new store object.


## Events
When the user interacts with the DOM, it fires events that trigger an effect in our JavaScript code that can do something. Such as updating the DOM or adding content to the database. 

To pick up events, our code must 'listen' for the event. The `addEventListener` method will do just that. It takes 2 arguments, the first is the event it's listening for, and the second is the function that will run once the event is triggered.

```js
div.addEventListener('click', () => console.log('hi'))

// When events are triggered, the event object is passed as an argument
// to the event handler function (the callback passed as the second arg to addEventListener)
div.addEventListener('click', (e) => console.log(e))

```

There are many event types: [Events](https://developer.mozilla.org/en-US/docs/Web/Events)


## Forms
Forms can have a variety of user inputs users can interact with.
The submit event can be used to retrieve the value of those inputs. 

When a form submits, it will, by default, try to send a request and refresh the page. To prevent that, we need to call e.preventDefault(). Afterward, the event can be used to grab the form values through the target attribute.

```html
<form>
  <input type="text" name='favColor'/>
  <input type="submit" />
</form>
```

```js
form.addEventListener('submit',(e)=> {
  e.preventDefault
  //Here we are using the name property from the form to target the specific input.
  console.log(e.target.faveColor.value)
})
```