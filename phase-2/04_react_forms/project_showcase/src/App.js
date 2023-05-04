import { useState } from "react";

import Header from "./components/Header";
import ProjectForm from "./components/ProjectForm";
import ProjectList from "./components/ProjectList";
import ProjectFilter from "./components/ProjectFilter";
// import projects from './projects'

const App = () => {
  //! INVERSION DATA FLOW
  
  //! THERE IS NO WAY TO CHANGE darkModeOn WITHOUT USING setDarkModeOn
  const [darkModeOn, setDarkModeOn] = useState(false);
  const [userQuery, setUserQuery] = useState("");
  const [phaseSelected, setPhaseSelected] = useState("All");

  const handleClick = (e) => {
    //! If you need to reference the current value to determine the new one: THIS IS WRONG!
    // setDarkModeOn(!darkModeOn)
    //! The preferred way is:
    setDarkModeOn(currentValue => !currentValue)
  }

  const handleChange = (e) => {
    const value = e.target.value
    setUserQuery(value)
  }

  const handlePhaseClick = (e) => {
    const intValue = parseInt(e.target.textContent.slice(-1))
    e.target.textContent === "All" ? setPhaseSelected("All") : setPhaseSelected(intValue)
  }
  // # Deliverable 1: Configure a <button> in our App 
  // that will use json-server to fetch projects 
  // and store them in state

  // - Add an onClick event listener to the "Load Projects" 
  // button

  // - When the button is clicked, make a fetch 
  // request to "http://localhost:4000/projects"
  // and set the `projects` state to the value 
  // returned by the response

  return (
    <div className={darkModeOn ? "App" : "App light"}>
      <Header handleClick={handleClick} darkModeOn={darkModeOn}/>
      <ProjectForm />
      <ProjectFilter handleClick={handlePhaseClick} handleChange={handleChange} />
      <ProjectList userQuery={userQuery} phaseSelected={phaseSelected} />
    </div>
  );
};

export default App;
