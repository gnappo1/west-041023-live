import React, {useEffect} from 'react'
import styled from 'styled-components'


const Notification = ({errors, resetErrors}) => {

  useEffect(() => {
    const timer = setTimeout(() => resetErrors(), 3000)
    
    return () => {
      clearTimeout(timer)
    };
  }, [resetErrors]);

  const mappedErrors = errors?.map(error => <Div className='error'>{error}</Div>)
  
  return (
    <div>{mappedErrors}</div>
  )
}

const Div = styled.div`
  background-color: red;
  color: #fff;
  text-align: center;
  font-weight: bold;
  height: 1.5rem;
`


export default Notification;