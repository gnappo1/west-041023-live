import ProjectListItem from "./ProjectListItem";
import { useState } from 'react'

const ProjectList = ({ projects }) => {
  const [userQuery, setUserQuery] = useState("");
  const [phaseSelected, setPhaseSelected] = useState("All");

  const handleChange = (e) => {
    const value = e.target.value
    setUserQuery(value)
  }

  const handleClick = (e) => {
    const intValue = parseInt(e.target.textContent.slice(-1))
    e.target.textContent === "All" ? setPhaseSelected("All") : setPhaseSelected(intValue)
  }
  
  //TODO Showcase the different ways we could have handled the double filtering

  //! Make 2 subsequent filter calls in TWO separate variables
  // const queryFilteredProjects = projects
  // .filter(project => project.name.toLowerCase().includes(userQuery.toLowerCase()) || project.about.toLowerCase().includes(userQuery.toLowerCase()))
  
  // const phaseFilteredProjects = queryFilteredProjects.filter(project => phaseSelected === "All" || project.phase === phaseSelected)
  
  //! Make 2 subsequent filter calls in ONE variable
  // const queryFilteredProjects = projects
  // .filter(project => project.name.toLowerCase().includes(userQuery.toLowerCase()) || project.about.toLowerCase().includes(userQuery.toLowerCase()))
  // .filter(project => phaseSelected === "All" || project.phase === phaseSelected)
  

  //! Make ONE filter call where you combine the conditions with logical operators
  // const queryFilteredProjects = projects.filter(project => (project.name.toLowerCase().includes(userQuery.toLowerCase()) || project.about.toLowerCase().includes(userQuery.toLowerCase())) && (phaseSelected === "All" || project.phase === phaseSelected))

  //! Refactor it to look neat using a couple of helper functions
  const filterBy = (project, prop) => project[prop].toLowerCase().includes(userQuery.toLowerCase())

  const phaseSelection = (project) => phaseSelected === "All" || project.phase === phaseSelected

  const queryFilteredProjects = projects.filter(project => (filterBy(project, "name") || filterBy(project, 'about')) && phaseSelection(project))
  
  const projectListItems = queryFilteredProjects.map((project) => <ProjectListItem key={project.id} {...project} />);


  return (
    <section>
      <h2>Projects</h2>

      <div className="filter">
        <button onClick={handleClick}>All</button>
        <button onClick={handleClick}>Phase 5</button>
        <button onClick={handleClick}>Phase 4</button>
        <button onClick={handleClick}>Phase 3</button>
        <button onClick={handleClick}>Phase 2</button>
        <button onClick={handleClick}>Phase 1</button>
      </div>
      <input type="text" onChange={handleChange} placeholder="Search project by name..."/>

      <ul className="cards">{projectListItems}</ul>
    </section>
  );
};

export default ProjectList;
