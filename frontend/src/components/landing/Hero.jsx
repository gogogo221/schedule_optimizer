import React from "react"
import { Link } from 'react-router-dom';
import calendar_graphic from "../../assets/knowledge-base_Calendars-01.png"

export default function Hero(){

    return (
        <div id="hero">
         
                <div id="hero-text" >
                    <h1 id="title">Trojan Schedule Helper</h1>
                    <h4 id="subtitle">Stress free course selection </h4>
                    <Link to="/register"><button id="try-button" type="button" className="btn btn-light">Try it Out</button></Link> 
                </div>
                <img src={calendar_graphic} id="hero-graphic"/>
                {console.log(document.querySelector("#hero-graphic"))}
        </div>
           
        
    )
}