import {useEffect, useState, useReducer, createContext} from 'react'

const ProjectContext = createContext()

const initialState = []

const reducer = (state, action) => {
    switch (action.type) {
        case "fetch":
            return action.payload
        case "add":
            
            return [...state, action.payload];
        case "patch":
            
            return state.map(project => project.id === action.payload.id ? action.payload : project);
        case "remove":
            
            return state.filter(project => project.id !== action.payload);
    
        default:
            return state;
    }

}
const ProjectProvider = ({children}) => {

    // const [projects, setProjects] = useState([]);
    const [projects, dispatch] = useReducer(reducer, initialState)

    // const handleFetchAsync = async () => {
    //     try {
    //       const resp = await fetch(' http://localhost:4000/projects')
    //       if (resp.status === 200) {
    //         const projectList = await resp.json()
    //         dispatch({
    //             type: 'fetch',
    //             payload: projectList
    //         })          } else {
    //         throw new Error('Could not complete the request! Check request parameters please.')
    //       }
    //     } catch (error) {
    //       alert(error)
    //     }
    // }

    // const handleNewProject = (newProjectObj) => {
    //     setProjects(currentProjects => [...currentProjects, newProjectObj])
    //   }
      
    const handleFetchTraditional = () => {
    fetch(' http://localhost:4000/projects')
    .then(resp => {
        resp.json().then(data => {
        if (resp.status === 200) {
            dispatch({
                type: 'fetch',
                payload: data
            })
        } else {
            throw new Error('Could not complete the request! Check request parameters please.')
        }
        })
    })
    .catch(error =>  alert(error))
    }

    // const handleUpdateProject = (updatedProjectObj) => {
    //     setProjects(currentProjects => {
    //       // const newProjectsState = currentProjects.map(project => {
    //       //   if (project.id === updatedProjectObj.id ) {
    //       //     return updatedProjectObj
    //       //   } else {
    //       //     return project
    //       //   }
    //       // })
    //       return currentProjects.map(project => project.id === updatedProjectObj.id ? updatedProjectObj : project)
    
    //     })
    //   }
    
    // const handleProjectDelete = (projectToDeleteId) => {
    // setProjects(currentProjects => currentProjects.filter(project => project.id !== projectToDeleteId))
    // }
    

    useEffect(() => {
        handleFetchTraditional()
    }, [])
    
    return (
        <ProjectContext.Provider value={{projects, dispatch}}>
            {children}
        </ProjectContext.Provider>
    )
}

export {ProjectContext, ProjectProvider}