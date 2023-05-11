import {useState, useRef, useContext, useReducer} from 'react'
// import { uuid } from 'uuidv4';
import {useHistory} from 'react-router-dom'
import { ProjectContext } from "../context/projectContext";

const initialState = {
  name: "",
  about: "",
  phase: "",
  link: "",
  image: ""
}

const reducer = (state, {key, value}) => {
  return {
    ...state,
    [key]: value
  }
}

const ProjectForm = () => {
  const {handleNewProject} = useContext(ProjectContext);
  const [state, dispatch] = useReducer(reducer, initialState)
  const history = useHistory()
  const image = useRef(null)
  const validateData = () =>  Object.values(state).some(element => element.trim() === "")

  const handleSubmit = (e) => {
    e.preventDefault()
    if (validateData()) {
      alert("Please fill out the entire form!")
    } else {
      // the new project object has to make it to the page
      // const state = {name, about, phase, link, image}
      // the new project has to make it to the json-server
 
      const formdata = new FormData(e.target)
      formdata.append('file', image.current.files[0])
      const files = Array.from(e.target['upload'].files)

      fetch('http://localhost:4000/projects', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(state)
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
  const handleChange = (e) => {
    dispatch({key: e.target.name, value: e.target.value})
  }
  return (
    <section>
      <form className="form" autoComplete="off" onSubmit={handleSubmit}>
        <h3>Add New Project</h3>

        <label htmlFor="name">Name</label>
        <input type="text" id="name" name="name" onChange={handleChange} value={state.name} required/>

        <label htmlFor="about">About</label>
        <textarea id="about" name="about" onChange={handleChange} value={state.about} required/>

        <label htmlFor="phase">Phase</label>
        <select name="phase" id="phase" onChange={handleChange} value={state.phase} required>
          <option>Select One</option>
          <option value="1">Phase 1</option>
          <option value="2">Phase 2</option>
          <option value="3">Phase 3</option>
          <option value="4">Phase 4</option>
          <option value="5">Phase 5</option>
        </select>

        <label htmlFor="link">Project Homepage</label>
        <input type="text" id="link" name="link" onChange={handleChange} value={state.link} required/>

        <label htmlFor="image">Screenshot</label>
        <input type="text" id="image" name="image" onChange={handleChange} value={state.image} required/>
        
        <label htmlFor="image">Image File</label>
        <input type="file" id="upload" name="upload" ref={image} required/>

        <button type="submit">Add Project</button>
      </form>
    </section>
  );
};

export default ProjectForm;
