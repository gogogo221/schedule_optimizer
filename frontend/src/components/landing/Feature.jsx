import React from "react"

export default function Feature(props){

    return (

        <div className="feature-container">
            <img className="feature-img" src={props.img} alt={props.img}/>
            <p  className="feature-name">{props.name}</p>
            <p className="feature-text">{props.text}</p>
        </div>
        
    )
}