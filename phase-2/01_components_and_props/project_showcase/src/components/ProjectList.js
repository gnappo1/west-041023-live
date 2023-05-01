import React from 'react'
import ProjectListCard from './ProjectListCard'

const ProjectList = ({projects}) => {
    console.log(projects)

    const mappedProjects = projects.map(project => <ProjectListCard key={project.id} project={project}/>)

  return (
    <div>{mappedProjects}</div>
  )
}

export default ProjectList