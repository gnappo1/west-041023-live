import {useState} from 'react'
import { useHistory } from 'react-router-dom';
// import { uuid } from 'uuidv4';

const ProjectForm = ({handleNewProject}) => {

  // const [name, setName] = useState("");
  // const [about, setAbout] = useState("");
  // const [phase, setPhase] = useState("");
  // const [link, setLink] = useState("");
  // const [image, setImage] = useState("");

  const [newProject, setNewProject] = useState({
    name: "",
    about: "",
    phase: "",
    link: "",
    image: ""
  });
  const history = useHistory()

  const validateData = () =>  [newProject.name, newProject.about, newProject.link, newProject.image, newProject.phase].some(el => el.trim() === '' )

  const handleChange = ({target: {id, value}}) => {
    
    setNewProject({
      ...newProject,
      [id]: value
    })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (validateData()) {
      alert("Please fill out the entire form!")
    } else {
      // the new project object has to make it to the page
      // const newProject = {name, about, phase, link, image}
      // the new project has to make it to the json-server
      fetch('http://localhost:4000/projects', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(newProject)
      })
      .then(resp => {
        if (resp.status === 201) {
          resp.json()
          .then(projectFromDb => handleNewProject(projectFromDb))
          .then(() => history.push("/projects"))
        } else {
          alert("Something went wrong, try again!")
        }
      })
      .catch(err => console.error(err))
      
      // [setName, setAbout, setImage, setLink, setPhase].forEach(fn => fn(""))
      // setName("")
      // setAbout("")
      // setImage("")
      // setLink("")
      // setPhase("")
  }
  }

  return (
    <section>
      <form className="form" autoComplete="off" onSubmit={handleSubmit}>
        <h3>Add New Project</h3>

        <label htmlFor="name">Name</label>
        <input type="text" id="name" name="name" onChange={handleChange} value={newProject.name} required/>

        <label htmlFor="about">About</label>
        <textarea id="about" name="about" onChange={handleChange} value={newProject.about} required/>

        <label htmlFor="phase">Phase</label>
        <select name="phase" id="phase" onChange={handleChange} value={newProject.phase} required>
          <option>Select One</option>
          <option value="1">Phase 1</option>
          <option value="2">Phase 2</option>
          <option value="3">Phase 3</option>
          <option value="4">Phase 4</option>
          <option value="5">Phase 5</option>
        </select>

        <label htmlFor="link">Project Homepage</label>
        <input type="text" id="link" name="link" onChange={handleChange} value={newProject.link} required/>

        <label htmlFor="image">Screenshot</label>
        <input type="text" id="image" name="image" onChange={handleChange} value={newProject.image} required/>

        <button type="submit">Add Project</button>
      </form>
    </section>
  );
};

export default ProjectForm;