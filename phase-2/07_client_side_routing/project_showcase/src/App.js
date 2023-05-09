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
  import ProjectList from "./components/ProjectList";
  import ProjectFilter from "./components/ProjectFilter";
  import EditProjectForm from "./components/EditProjectForm";
  // import projects from './projects'
  
  const App = () => {
    //! INVERSION DATA FLOW
    
    //! THERE IS NO WAY TO CHANGE darkModeOn WITHOUT USING setDarkModeOn
    const [darkModeOn, setDarkModeOn] = useState(false);
    const [userQuery, setUserQuery] = useState("");
    const [phaseSelected, setPhaseSelected] = useState("All");
    const [projects, setProjects] = useState([]);
    const [projectId, setProjectId] = useState(null);
  
    const handleSetProjectId = (newProjectId) => {
      setProjectId(newProjectId)
    }
  
    const handleFetchAsync = async () => {
      try {
        const resp = await fetch(' http://localhost:4000/projects')
        if (resp.status === 200) {
          const projectList = await resp.json()
          setProjects(projectList)
        } else {
          throw new Error('Could not complete the request! Check request parameters please.')
        }
      } catch (error) {
        alert(error)
      }
    }
    
    const handleFetchTraditional = () => {
      fetch(' http://localhost:4000/projects')
      .then(resp => {
        resp.json().then(data => {
          if (resp.status === 200) {
            setProjects(data)
          } else {
            throw new Error('Could not complete the request! Check request parameters please.')
          }
        })
      })
      .catch(error =>  alert(error))
    }
  
    useEffect(() => {
      handleFetchTraditional()
    }, [])
  
  
    const handleClick = (e) => {
      //! If you need to reference the current value to determine the new one: THIS IS WRONG!
      // setDarkModeOn(!darkModeOn)
      //! The preferred way is:
      setDarkModeOn(currentValue => !currentValue)
    }
  
    const handleNewProject = (newProjectObj) => {
      setProjects(currentProjects => [...currentProjects, newProjectObj])
    }
  
    const handleChange = (e) => {
      const value = e.target.value
      setUserQuery(value)
    }
  
    const handlePhaseClick = (e) => {
      const intValue = parseInt(e.target.textContent.slice(-1))
      e.target.textContent === "All" ? setPhaseSelected("All") : setPhaseSelected(intValue)
    }
  
    const handleUpdateProject = (updatedProjectObj) => {
      setProjects(currentProjects => {
        // const newProjectsState = currentProjects.map(project => {
        //   if (project.id === updatedProjectObj.id ) {
        //     return updatedProjectObj
        //   } else {
        //     return project
        //   }
        // })
        return currentProjects.map(project => project.id === updatedProjectObj.id ? updatedProjectObj : project)
  
      })
    }
  
    const handleProjectDelete = (projectToDeleteId) => {
      setProjects(currentProjects => currentProjects.filter(project => project.id !== projectToDeleteId))
    }
  
    const resetEditingModeToNull = () => {
      setProjectId(null)
    }
  
    return (
      <div className={darkModeOn ? "App" : "App light"}>
        <Header handleClick={handleClick} darkModeOn={darkModeOn}/>
        {projectId ? <EditProjectForm resetEditingModeToNull={resetEditingModeToNull} projectId={projectId} handleUpdateProject={handleUpdateProject}/> : <ProjectForm handleNewProject={handleNewProject}/>}
        <ProjectFilter handleClick={handlePhaseClick} handleChange={handleChange} />
        <ProjectList handleProjectDelete={handleProjectDelete} handleSetProjectId={handleSetProjectId} projects={projects} userQuery={userQuery} handleNewProject={handleNewProject} phaseSelected={phaseSelected} />
      </div>
    );
  };
  
  export default App;
  