import React from "react"
import { Route, Routes, Link } from "react-router-dom"
// Bootstrap CSS
import "bootstrap/dist/css/bootstrap.min.css";
// Bootstrap Bundle JS
import "bootstrap/dist/js/bootstrap.bundle.min";

export default function Navbar(){

    return (
        <>
            <nav className="navbar navbar-expand-md navbar-custom shadow-sm">
                <Link className="navbar-brand" to="/" id="nav-title">Trojan Schedule Helper</Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" 
                    data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup"
                    aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div className="navbar-nav ms-auto  shadow-3" id="nav-right">
                        <Link className="nav-item nav-link" to="/login">Log in</Link>
                        <Link className="nav-item nav-link" to="/register">Register</Link>
                        <Link className="nav-item nav-link" to="/saved-schedules">Saved Schedules</Link>
                        <Link className="nav-item nav-link" to="/tool-form">Schedule Tool</Link>
                    
                    </div>
                </div>
            </nav>
        </>
    )
}

