import React from "react"
import { Link } from 'react-router-dom';
export default function Hero(){

    return (
        <div id="hero">
         
                <div id="hero-text" >
                    <h1 id="title">Trojan Schedule Helper</h1>
                    <h4 id="subtitle">Stress free course selection </h4>
                    <Link to="/tool-form"><button id="try-button" type="button" className="btn btn-light">Try it Out</button></Link> 
                </div>
                <img  src="../public/assets/knowledge-base_Calendars-01.png" id="hero-graphic"/>
        </div>
           
        
    )
}