import {useRef, useState} from 'react'

const Test = () => {
    const [stateCount, setStateCount] = useState(0);
    let localCount = 0
    const refCount = useRef(0)
    
    const handleClick = (e) => {
        console.log("The before: ", stateCount, localCount, refCount.current)
        if (e.target.name === 'add') {
            localCount++
            refCount.current++
            setStateCount(current => current + 1)
        } else {
            localCount--
            refCount.current--
            setStateCount(current => current - 1)
        }
        console.log("The after: ", stateCount, localCount, refCount.current)
    }

    return (
        <div>
            <p>State is {stateCount} | Local Var is {localCount} | Ref is {refCount.current}</p>
            <button name="add" onClick={handleClick}>Increase</button>
            <button name="remove" onClick={handleClick}>Decrease</button>
        </div>
    )
}

export default Test