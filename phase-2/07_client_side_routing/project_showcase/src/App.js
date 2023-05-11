// Deliverable 2: Use Switch and Route to set up initial routes so we can 
// conditionally render components based on URL

  // - Import the `Switch` component from the `react-router-dom` library 
  // and wrap the components designated for routing

  // - Import the `Route` component from the `react-router-dom` library 
  // and wrap each individual component designated for routing

  //   - Provide the `path` prop to the `Route` component to create a URL 
  // path associated with the component

  // - Demonstrate each route in the browser to confirm desired expectation 
  // is occuring

  // - Demonstrate the use of the `exact` prop passed to the `Route` 
  // component
  import { useState, useEffect } from "react";

  import Header from "./components/Header";
  import ProjectForm from "./components/ProjectForm";
  import Home from "./components/Home";
  import ProjectList from "./components/ProjectList";
  import ProjectFilter from "./components/ProjectFilter";
  import EditProjectForm from "./components/EditProjectForm";
  import Error from "./components/Error";
  import Test from "./components/Test";
  import ProjectDetail from "./components/ProjectDetail";
  import {Switch, Route} from 'react-router-dom'

  // import projects from './projects'
  
  const App = () => {
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

    return (
      <div className={darkModeOn ? "App" : "App light"}>
        <Header handleClick={handleClick} darkModeOn={darkModeOn}/>
        <Switch>
          <Route path="/projects/:id/edit">
            <EditProjectForm />
          </Route>
          <Route path="/projects/new">
            <ProjectForm />
          </Route>
          <Route path="/projects/:id">
            <ProjectDetail />
          </Route>
          <Route path="/projects">
            <ProjectFilter handleClick={handlePhaseClick} handleChange={handleChange} />
            <ProjectList userQuery={userQuery} phaseSelected={phaseSelected} />
          </Route>
          <Route exact path="/">
            <Home />
            <Test />
          </Route>
          <Route>
            <Error />
          </Route>
        </Switch>
      </div>
    );
  };
  
  export default App;
  