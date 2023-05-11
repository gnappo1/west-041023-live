import { useState, useEffect } from 'react'
import { useParams, useHistory } from 'react-router-dom'

const initialState = {
    name: "",
    about: "",
    phase: "",
    link: "",
    image: ""
}

const EditProjectForm = ({handleUpdateProject}) => {
    const [formData, setFormData] = useState(initialState)
    const {id} = useParams()
    const history = useHistory()
    useEffect(() => {
        fetch(`http://localhost:4000/projects/${id}`)
        .then(resp => resp.json())
        .then(data => setFormData(data))
    }, [id])

    const {name, about, phase, link, image} = formData

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        //! Figure out what new data looks like and maybe package it into one object => formData
        //! Fire the PATCH/PUT
        fetch(`http://localhost:4000/projects/${id}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        //! in case of success:
        .then(resp => resp.json())
        .then(updatedProjectFromJSON => {
            //TODO 1. Update our state
            handleUpdateProject(updatedProjectFromJSON)
            //TODO 2. Empty the form
            setFormData(initialState)
            //TODO 3. Let App know that we're not in editing mode anymore

        })
        .then(() => history.push(`/projects/${id}`))
    }

    return (
    <section>
      <form className="form" autoComplete="off" onSubmit={handleSubmit}>
        <h3>Update Existing Project</h3>

        <label htmlFor="name">Name</label>
        <input type="text" id="name" name="name" onChange={handleChange} value={name} required/>

        <label htmlFor="about">About</label>
        <textarea id="about" name="about" onChange={handleChange} value={about} required/>

        <label htmlFor="phase">Phase</label>
        <select name="phase" id="phase" onChange={handleChange} value={phase} required>
          <option>Select One</option>
          <option value="1">Phase 1</option>
          <option value="2">Phase 2</option>
          <option value="3">Phase 3</option>
          <option value="4">Phase 4</option>
          <option value="5">Phase 5</option>
        </select>

        <label htmlFor="link">Project Homepage</label>
        <input type="text" id="link" name="link" onChange={handleChange} value={link} required/>

        <label htmlFor="image">Screenshot</label>
        <input type="text" id="image" name="image" onChange={handleChange} value={image} required/>

        <button type="submit">Update Project</button>
      </form>
    </section>

    )
}

export default EditProjectForm