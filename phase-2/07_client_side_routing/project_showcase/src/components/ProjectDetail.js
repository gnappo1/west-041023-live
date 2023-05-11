// Deliverable 4: Using the useParams hook, access the :id param from the URL
// to trigger appropriate GET requests

import { useEffect, useState } from "react";
import {useParams, useLocation} from "react-router-dom"

const ProjectDetail = () => {
  const [claps, setClaps] = useState(0);
  const [project, setProject] = useState(null);
  const [loading, setLoading] = useState(true);
  const {id} = useParams()
  const location = useLocation()
  
  console.log(location)
  useEffect(() => {
    fetch(`http://localhost:4000/projects/${id}`)
      .then((r) => r.json())
      .then((project) => {
        
        // Currently, before we can get to this step,
        // we're trying to destructure "project"
        setProject(project);

        // Invoke setIsLoaded to change isLoaded State
        setLoading(current => !current)
      });
  }, [id]);

  // Reference isLoaded State. If False, Render Simple H1 "Loading..." Component
  
  const handleClapClick = () => {
    setClaps((claps) => claps + 1);
  }
  
  if (loading) return <h1>Loading...</h1>
  const { image, name, about, link, phase } = project;
  return (
    <section>
      <div className="project-detail box">
        <div className="project-image">
          <img src={image} alt={name} />
          <button className="claps" onClick={handleClapClick}>
            👏{claps}
          </button>
        </div>
        <div className="details">
          <h2>{name}</h2>
          <p>{about}</p>
          {link ? (
            <p>
              <a target="_blank" rel="noreferrer" href={link}>
                Project Homepage
              </a>
            </p>
          ) : null}
          <div className="extra">
            <span className="badge blue">Phase {phase}</span>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProjectDetail;
