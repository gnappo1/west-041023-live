// 📚 Review With Students:
    // Request response cycle
    //Note: This was build using v5 of react-router-dom
import { Route, Switch, useHistory } from 'react-router-dom'
import {createGlobalStyle} from 'styled-components'
import {useEffect, useState} from 'react'
import Home from './components/Home'
import ProductionForm from './components/ProductionForm'
import ProductionEdit from './components/ProductionEdit'
import Navigation from './components/Navigation'
import ProductionDetail from './components/ProductionDetail'
import NotFound from './components/NotFound'
import "./App.css"
import Registration from './components/Registration'

function App() {
  const [productions, setProductions] = useState([])
  const [production_edit, setProductionEdit] = useState(false)
  const [currentUser, setCurrentUser] = useState(null);
  const [errors, setErrors] = useState([])
  const history = useHistory()
  //5.✅ GET Productions

  useEffect(() => {
    (async () => {
      const [productions_resp, auth_resp] = await Promise.all([fetch("/api/v1/productions"), fetch("/api/v1/me")]);
      if (productions_resp.ok) {
        const prods = await productions_resp.json()
        setProductions(prods)
      } else {
        const error = await productions_resp.json()
        setErrors(current => [...current, error.error])
      }

      if (auth_resp.ok) {
        const user = await auth_resp.json()
        setCurrentUser(user)
      }
    })();
  }, []);

  
  // 6.✅ navigate to client/src/components/ProductionForm.js

  const addProduction = (production) => setProductions(productions => [...productions,production])
  const updateProduction = (updated_production) => setProductions(productions => productions.map(production =>{
    if(production.id === updated_production.id){
      return updated_production
    } else {
      return production
    }
  } ))
  const deleteProduction = (deleted_production) => setProductions(productions => productions.filter((production) => production.id !== deleted_production.id))

  const handleEdit = (production) => {
    setProductionEdit(current => !current)
    history.push({
      pathname: `/productions/edit/${production.id}`,
      state: production
    })
  }

  const updateCurrentUser = (user) => { setCurrentUser(user) }
  const addError = (error) => { setErrors(current => [...current, error]) }

  if (!currentUser) {
    return (
      <>
        <GlobalStyle />
        <Navigation handleEdit={handleEdit} currentUser={currentUser}/>
        <Switch>
          <Route path='/auth'>
              <Registration updateCurrentUser={updateCurrentUser} addError={addError} />
          </Route>
          <Route path='/productions/:prodId'>
            <ProductionDetail handleEdit={handleEdit} deleteProduction={deleteProduction} currentUser={currentUser} />
          </Route>
          <Route exact path='/'>
            <Home  productions={productions} />
          </Route>
          <Route>
            <NotFound />
          </Route>
        </Switch>
      </>
  )
}

  return (
    <>
    <GlobalStyle />
    <Navigation handleEdit={handleEdit} updateCurrentUser={updateCurrentUser} currentUser={currentUser}/>
    <Switch>
      <Route  path='/productions/new'>
        <ProductionForm addProduction={addProduction}/>
      </Route>
      <Route  path='/productions/edit/:id'>
        <ProductionEdit updateProduction={updateProduction} production_edit={production_edit}/>
      </Route>
      <Route path='/productions/:prodId'>
          <ProductionDetail handleEdit={handleEdit} deleteProduction={deleteProduction} currentUser={currentUser} />
      </Route>
      <Route exact path='/'>
        <Home  productions={productions} />
      </Route>
      <Route>
        <NotFound />
      </Route>
    </Switch>
    </>
  )
}

export default App

const GlobalStyle = createGlobalStyle`
    body{
      background-color: black; 
      color:white;
    }
    `
