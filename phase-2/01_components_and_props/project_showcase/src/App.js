// Create an App component that:
// Returns the Header, ProjectForm and ProjectList components

// Provides the array of projects to ProjectList as props
import Header from "./components/Header";
import ProjectForm from "./components/ProjectForm";
import ProjectList from "./components/ProjectList";
import projects from "./projects"

const App = () => {
  // JS LAND HERE

// const name = "TEST"
// const newName = `My name is ${name}`

  return (
    <div>
      <Header person={{name: "Matteo", lastname: "Piccini"}}/>
      <ProjectForm />
      <ProjectList projects={projects}/>
    </div>
  );
}

export default App;