// Deliverable 3: Demonstrate the unmounting and cleanup 
// phase of a component through `useEffect`

import { useState, useEffect } from "react"

    // Return a cleanup function inside the `useEffect` 
    // with a console.log()

    // Open up the devtools to observe when the cleanup 
    // will occur during the stages of Component Lifecycle

function Timer() {
    const [timer, setTimer] = useState(0);
    const [isPaused, setIsPaused] = useState(false);

    useEffect(() => {
        const consoleLog = () => console.log("Inside the useEffect")
        document.addEventListener("click", consoleLog)

        const intervalId = setInterval(() => {
            if (!isPaused) {
                setTimer(currentTimer => currentTimer + 1)
            }
        }, 1000)

        return () => {
            console.log("Inside the cleanup")
            clearInterval(intervalId)
            document.removeEventListener("click", consoleLog)
        }
    }, [isPaused])

    return (
        <>
        <button onClick={() => setIsPaused(currentVal => !currentVal)}>{isPaused ? "Resume" : "Pause"}</button>
        <h2>{timer}</h2>
        </>
    )
}

export default Timer