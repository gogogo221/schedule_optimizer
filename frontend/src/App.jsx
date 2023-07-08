import { useState } from 'react'
import { Route, Routes } from "react-router-dom"
import Navbar from './components/Navbar';
import Landing from './pages/Landing';
import ToolForm from "./pages/ToolForm"
import Login from './pages/Login';
import Register from './pages/Register';
import SavedSchedules from './pages/SavedSchedules';
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/tool-form" element={<ToolForm />} />
      <Route path="/register" element={<Register />} />
      <Route path="/login" element={<Login />} />
      <Route path="/saved-schedules" element={<SavedSchedules />} />
    </Routes>

    </>
  )
}

export default App
