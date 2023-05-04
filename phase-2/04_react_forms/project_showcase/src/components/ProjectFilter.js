import React from 'react'

const ProjectFilter = ({handleChange, handleClick}) => {
  return (
    <>
        <div className="filter">
        <button onClick={handleClick}>All</button>
        <button onClick={handleClick}>Phase 5</button>
        <button onClick={handleClick}>Phase 4</button>
        <button onClick={handleClick}>Phase 3</button>
        <button onClick={handleClick}>Phase 2</button>
        <button onClick={handleClick}>Phase 1</button>
      </div>
      <input type="text" onChange={handleChange} placeholder="Search project by name..."/>

    </>
  )
}

export default ProjectFilter