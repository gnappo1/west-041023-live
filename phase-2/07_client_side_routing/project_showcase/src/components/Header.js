// Deliverable 3: Add navigation to the application using the `Link` and 
// `NavLink` components

  // - Convert any html anchor tags to `Link` or `NavLink`

  // - Demonstrate the difference between `Link` and `NavLink`
import {Link, NavLink} from 'react-router-dom'

  const Header = ({handleClick, darkModeOn}) => {
    const buttonTextContent = darkModeOn ? "Light Mode" : "Dark Mode";
  
    return (
      <header>
        <nav>
          <h1 className="branding">
          <NavLink to="/">
            <span className="logo">{"//"}</span>
            Project Showcase
            </NavLink>
          </h1>
          <div className="navigation">
            <NavLink exact className="button" to="/projects">
              All Projects
            </NavLink>
            <NavLink className="button" to="/projects/new">
              Add Project
            </NavLink>
            <button onClick={handleClick}>{buttonTextContent}</button>
          </div>
        </nav>
      </header>
    );
  };
  
  export default Header;
  