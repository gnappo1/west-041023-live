import  {useParams, useHistory } from 'react-router-dom'
import {useEffect, useState} from 'react'
import styled from 'styled-components'

function ProductionDetail({handleEdit, deleteProduction, currentUser}) {
  const [production, setProduction] = useState({crew_members:[]})
  const [error, setError] = useState(null)
  const {prodId} = useParams()
  const history = useHistory()
  
  //Student Challenge: GET One 
  
  useEffect(()=>{
    //! Retrieve the Production with the id from the params
    //! If the production is not found, set an error message
    //! If the production is found, set the production in state
    fetch(`/api/v1/productions/${prodId}`)
    .then(resp => {
      if (resp.ok) { //same as saying if you get a 2** response status code
        resp.json().then(setProduction)
      } else {
        resp.json().then(error => setError(error.message))
      }
    })
    .catch(console.error)
  },[prodId])

  const handleDelete = (e) => {
    //! Delete the production from the database
    //! If the production is not found, set an error message
    //! If the production is found, send the use back to the list of productions
    fetch(`/api/v1/productions/${prodId}`, {
      method: "DELETE"
    })
    .then(resp => {
      if (resp.ok) { //same as saying if you get a 2** response status code
        deleteProduction(production)
        history.push("/")
      } else {
        resp.json().then(error => setError(error.message))
      }
    })
    .catch(console.error)
  }

  
  const {id, title, genre, image,description, crew_members} = production 
  
  if(error) return <h2>{error}</h2>

  return (
      <CardDetail id={id}>
        <h1>{title}</h1>
          <div className='wrapper'>
            <div>
              <h3>Genre:</h3>
              <p>{genre}</p>
              <h3>Description:</h3>
              <p>{description}</p>
              <h2>Cast Members</h2>
              <ul>
                {crew_members?.map(crew => <li key={crew.id}>{`${crew.role} : ${crew.name}`}</li>)}
              </ul>
            </div>
            <img src={image} alt={description}/>
          </div>
      {currentUser ? (
        <>
          <button onClick={()=> handleEdit(production)} >Edit Production</button>
          <button onClick={handleDelete} >Delete Production</button>
        </>
      ) : null}

      </CardDetail>
    )
  }
  
  export default ProductionDetail
  const CardDetail = styled.li`
    display:flex;
    flex-direction:column;
    justify-content:start;
    font-family:Arial, sans-serif;
    margin:5px;
    h1{
      font-size:60px;
      border-bottom:solid;
      border-color:#42ddf5;
    }
    .wrapper{
      display:flex;
      div{
        margin:10px;
      }
    }
    img{
      width: 300px;
    }
    button{
      background-color:#42ddf5;
      color: white;
      height:40px;
      font-family:Arial;
      font-size:30px;
      margin-top:10px;
    }
  `