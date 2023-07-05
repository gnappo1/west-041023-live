import { useState } from 'react'
import {Link} from 'react-router-dom'
import styled from 'styled-components'
import { GiHamburgerMenu } from 'react-icons/gi'

function Navigation({handleEdit, currentUser, updateCurrentUser, addError}) {
  const [menu, setMenu] = useState(false)
  const handleLogout = (e) => {
    fetch("/api/v1/logout", {method: "DELETE"})
    .then((res) => {
      if (res.ok) {
        localStorage.removeItem("token")
        localStorage.removeItem("refreshToken")
        updateCurrentUser(null)
      } else {
        addError("Something went wrong!")
      }
    })
  }
  return (
    <Nav> 
      <NavH1>Flatiron Theater Company</NavH1>
      <Menu>
        {!menu?
          <div onClick={() => setMenu(!menu)}>
            <GiHamburgerMenu size={30}/> 
        </div>:
        <ul>
          <li onClick={() => setMenu(!menu)}>x</li>
          <li><Link to='/'> Home</Link></li>
          {currentUser ? (
            <>
              <li ><Link to='/productions/new'>New Production</Link></li>
              <li onClick={handleLogout}><Link to='/'>Logout</Link></li>
            </>
          ) : (
            <li><Link to='/auth'>Register</Link></li>
          )}
        </ul>
        }
      </Menu>
    </Nav>
  )
}

export default Navigation


const NavH1 = styled.h1`
font-family: 'Splash', cursive;
`
const Nav = styled.div`
  display: flex;
  justify-content:space-between;
  
`;

const Menu = styled.div`
  display: flex;
  align-items: center;
  a{
    text-decoration: none;
    color:white;
    font-family:Arial;
  }
  a:hover{
    color:pink
  }
  ul{
    list-style:none;
  }
  
`;
