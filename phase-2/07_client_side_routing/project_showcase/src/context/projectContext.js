import {createContext, useState, useEffect, useReducer} from 'react'

const ProjectContext = createContext()

const reducer = (state, action) => {
    switch (action.type) {
        case "fetch":
            return action.payload
        case "add":
            return [action.payload, ...state]    
        case "patch":
            return state.map(project => project.id === action.payload.id ? action.payload : project)
        case "remove":
            return state.filter(project => project.id !== action.payload)   
        default:
            return state;
    }
}

const ProjectProvider = ({children}) => {
    // const [projects, setProjects] = useState([]);
    const [projects, dispatch] = useReducer(reducer, [])

    // const handleFetchAsync = async () => {
    //     try {
    //       const resp = await fetch(' http://localhost:4000/projects')
    //       if (resp.status === 200) {
    //         const projectList = await resp.json()
    //         setProjects(projectList)
    //       } else {
    //         throw new Error('Could not complete the request! Check request parameters please.')
    //       }
    //     } catch (error) {
    //       alert(error)
    //     }
    //   }
      
    const handleFetchTraditional = () => {
        fetch(' http://localhost:4000/projects')
        .then(resp => {
            resp.json().then(data => {
            if (resp.status === 200) {
                dispatch({type: 'fetch', payload: data})
            } else {
                throw new Error('Could not complete the request! Check request parameters please.')
            }
            })
        })
        .catch(error =>  alert(error))
    }

    const handleUpdateProject = (updatedProjectObj) => {
        dispatch({type: 'patch', payload: updatedProjectObj})
    }
    
    const handleProjectDelete = (projectToDeleteId) => {
        dispatch({type: 'remove', payload: projectToDeleteId})    
    }

    const handleNewProject = (newProjectObj) => {
        dispatch({type: 'add', payload: newProjectObj})    
    }
    
    useEffect(() => {
        handleFetchTraditional()
    }, [])

    return (
        <ProjectContext.Provider value={{projects, handleNewProject, handleUpdateProject, handleProjectDelete}}>
            {children}
        </ProjectContext.Provider>
    )
}
export { ProjectContext, ProjectProvider }