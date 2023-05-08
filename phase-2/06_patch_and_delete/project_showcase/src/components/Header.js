const Header = ({handleClick, darkModeOn}) => {

  return (
    <header>
      <h1>
        <span className="logo">{"//"}</span>
        Project Showcase
      </h1>
      <button onClick={handleClick}>{darkModeOn ? "Light" : "Dark"} Mode</button>
    </header>
  );
}

export default Header;