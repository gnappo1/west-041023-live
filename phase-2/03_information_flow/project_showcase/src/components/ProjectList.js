import ProjectListItem from "./ProjectListItem";
import { useState } from 'react'

const ProjectList = ({userQuery, phaseSelected}) => {
  const [projects, setProjects] = useState([]);

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

  const handleFetchTraditional = async () => {
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
      <button onClick={handleFetchTraditional}>Load Projects</button>
      <h2>Projects</h2>
      <ul className="cards">{projectListItems}</ul>
    </section>
  );
};

export default ProjectList;
