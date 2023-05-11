import { useState, useContext } from 'react'
import { FaPencilAlt, FaTrash } from "react-icons/fa";
import {Link, useLocation} from 'react-router-dom'
import { ProjectContext } from '../context/projectContext'


const ProjectListItem = ({ id, about, image, link, name, phase, claps=0, handleNewProject }) => {
  let [clapCount, setClapCount] = useState(claps)
  const {handleProjectDelete} = useContext(ProjectContext);
  const location = useLocation()

  const handleClick = () => {
    //! SUPER INCORRECT
    // ++clapCount
    // console.log(clapCount)
    //! NOT OPTIMAL
    // const newValue = clapCount + 1
    // setClapCount(newValue)
   
    //* CORRECT
    // setClapCount(currentClaps => currentClaps + 1)
    fetch(`http://localhost:4000/projects/${id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({claps: clapCount + 1})
    })
    .then(resp => {
      if (resp.status !== 200) {
        // setClapCount(currentClaps => currentClaps - 1)
        alert(resp.statusText)
      } else {
        resp.json().then(updatedObj => setClapCount(updatedObj.claps))
      }
    })

  }

  const handleDelete = () => {
    //! Modify local state using the function that App passed
    handleProjectDelete(id)
    //! Fire a DELETE fetch call to the json-server
    fetch(`http://localhost:4000/projects/${id}`, {
      method: "DELETE"
    }).then((resp) =>  {
      if (resp.status !== 200) {
        handleNewProject({ id, about, image, link, name, phase, claps })
      }
    })
  }

  return (
    <li className="card">
      <figure className="image">
        <img src={image} alt={name} />
        <button onClick={handleClick} className="claps">
          👏{clapCount}
        </button>
      </figure>

      <section className="details">
        <Link to={{pathname: `/projects/${id}`, state: {about}}}><h4>{name}</h4></Link>
        <p>{about}</p>
        {link ? (
          <p>
            <a href={link}>Link</a>
          </p>
        ) : null}
      </section>

      <footer className="extra">
        <span className="badge blue">Phase {phase}</span>
        <div className="manage">
          <Link className="button" to={`/projects/${id}/edit`}>
            <FaPencilAlt />
          </Link>
          <button onClick={handleDelete}>
            <FaTrash />
          </button>
        </div>
      </footer>
    </li>
  );
};
  
export default ProjectListItem;
  