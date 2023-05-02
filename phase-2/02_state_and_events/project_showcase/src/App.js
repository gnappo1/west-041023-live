import Header from "./components/Header";
import ProjectForm from "./components/ProjectForm";
import ProjectList from "./components/ProjectList";
import projects from "./projects";
import { useState } from 'react'

// . Add a click event to the 'Dark Mode' button inside the Header component:

// Define a function 'handleClick' that will toggle and update the isDarkMode state

// Attach a 'click' event to the button that invokes the callback function handleClick

const App = () => {
  //! INVERSION DATA FLOW
  
  //! THERE IS NO WAY TO CHANGE darkModeOn WITHOUT USING setDarkModeOn
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
