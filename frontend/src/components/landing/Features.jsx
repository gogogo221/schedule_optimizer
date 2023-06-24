import React from "react"
import Feature from "./Feature"

export default function Features(){

    return (
        <div id="features">
            <div id="features-top">
                <p id="feature-header">features</p>
                <p id="features-sub">Let our schedule helper <br/>  pick classes for you</p>
            </div>
            <div id="features-list">
                <Feature 
                    img="public/assets/scheduling_large_target_graphic.jpg"
                    name="Build"
                    text="Fill in your desired courses and our generators will pick a selection of schedules for you to chose from"
                />
                <Feature 
                    img="public/assets/another_image.jpg"
                    name="Save Time"
                    text="Skip the hassle of juggling the webreg, calendar, and the USC course catalog"
                />
                <Feature 
                    img="public/assets/rmp_logo.jpg"
                    name = "Reviews"
                    text = "We're integrated with RMP, removing the need to clutter your browser with professor reviews"
                />


            </div>
        </div>
        
    )
}