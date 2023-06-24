import { useState } from 'react'
import { Route, Routes } from "react-router-dom"
import Navbar from './components/Navbar';
import Landing from './pages/Landing';
import ToolForm from "./pages/ToolForm"
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/tool-form" element={<ToolForm />} />
    </Routes>

    </>
  )
}

export default App
