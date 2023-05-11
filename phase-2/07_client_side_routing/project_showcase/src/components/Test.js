import {useState, useRef} from 'react'

const Test = () => {
    const [stateVar, setStateVar] = useState(0);

    let localVar = 0

    const refVar = useRef(0)
    
    const handleClick = (e) => {
        
            console.log(`state var INITIALLY is ${stateVar}`)
            console.log(`local var INITIALLY is  ${localVar}`)
            console.log(`ref var INITIALLY is  ${refVar.current}`)
        if (e.target.name === "add") {
            localVar++
            refVar.current++
            setStateVar(current => current + 1)

        } else {
            localVar--
            refVar.current--
            setStateVar(current => current - 1)
        }
        console.log(`state var FINALLY is ${stateVar}`)
        console.log(`local var FINALLY is  ${localVar}`)
        console.log(`ref var FINALLY is  ${refVar.current}`)
    }

    return (
        <div>
            <p>State Var is {stateVar} | Local Var is {localVar} | ref Var is {refVar.current}</p>
            <button name="add" onClick={handleClick}>Increment</button>
            <button name="remove" onClick={handleClick}>Decrement</button>
        </div>
    )
}

export default Test