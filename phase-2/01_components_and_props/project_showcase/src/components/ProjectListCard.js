import React from 'react'

const ProjectListCard = ({project}) => {
    console.log(project)
  return (
    <div className="card">
        <h3>{project.name}</h3>
        <img className="card" src={project.image} alt={project.about}/>
    </div>
  )
}

export default ProjectListCard