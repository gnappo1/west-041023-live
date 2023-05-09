// Deliverable 3: Add navigation to the application using the `Link` and 
// `NavLink` components

  // - Convert any html anchor tags to `Link` or `NavLink`

  // - Demonstrate the difference between `Link` and `NavLink`

  const Header = ({handleClick, darkModeOn}) => {
    const buttonTextContent = darkModeOn ? "Light Mode" : "Dark Mode";
  
    return (
      <header>
        <nav>
          <h1 className="branding">
            <span className="logo">{"//"}</span>
            Project Showcase
          </h1>
          <div className="navigation">
            <a className="button" href="/projects">
              All Projects
            </a>
            <a className="button" href="/projects/new">
              Add Project
            </a>
            <button onClick={handleClick}>{buttonTextContent}</button>
          </div>
        </nav>
      </header>
    );
  };
  
  export default Header;
  