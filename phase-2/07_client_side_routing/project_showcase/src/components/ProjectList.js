import ProjectListItem from "./ProjectListItem";


const ProjectList = ({userQuery, phaseSelected, projects, handleSetProjectId, handleProjectDelete, handleNewProject}) => {


  
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
  
  const projectListItems = queryFilteredProjects.map((project) => <ProjectListItem key={project.id} handleProjectDelete={handleProjectDelete} handleNewProject={handleNewProject}  handleSetProjectId={handleSetProjectId} {...project} />);


  return (
    <section>
      <h2>Projects</h2>
      <ul className="cards">{projectListItems}</ul>
    </section>
  );
};

export default ProjectList;
