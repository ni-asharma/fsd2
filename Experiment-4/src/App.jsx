import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import CounterLocalState from "./components/CounterLocalState";
import { CounterContextProvider } from "./components/context/CounterGlobalContextAPI";
import CounterGlobalContextParent from "./components/CounterGlobalContextParent";
import CounterReduxParent from "./components/CounterGlobalReduxParent";

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h2>Experiment 4</h2>

      <CounterLocalState cno="Counter 1" />
      <CounterLocalState cno="Counter 2" />

      <CounterContextProvider>
        <CounterGlobalContextParent cno="Global Counter A" />
        <CounterGlobalContextParent cno="Global Counter B" />
      </CounterContextProvider>

      <h2>Experiment 4: Global State (Redux)</h2>
      <CounterReduxParent cno="Redux Counter A" />
      <CounterReduxParent cno="Redux Counter B" />
    </>
  )
}

export default App
