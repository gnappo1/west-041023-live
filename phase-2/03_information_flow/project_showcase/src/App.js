
import Header from "./components/Header";
import ProjectForm from "./components/ProjectForm";
import ProjectList from "./components/ProjectList";
import projects from "./projects";
import { useState } from 'react'


// # Deliverable 1: Configure a <button> in our App 
// that will use json-server to fetch projects 
// and store them in state

// - Add an onClick event listener to the "Load Projects" 
// button

// - When the button is clicked, make a fetch 
// request to "http://localhost:4000/projects"
// and set the `projects` state to the value 
// returned by the response


const App = () => {
  
  const [darkModeOn, setDarkModeOn] = useState(false);

  const handleClick = (e) => {
    //! If you need to reference the current value to determine the new one: THIS IS WRONG!
    // setDarkModeOn(!darkModeOn)
    //! The preferred way is:
    setDarkModeOn(currentValue => !currentValue)
  }

  return (
    <div className={darkModeOn ? "App" : "App light"}>
      <Header handleClick={handleClick} darkModeOn={darkModeOn} />
      <ProjectForm />
      <ProjectList projects={projects} />
    </div>
  );
};

export default App;