import React from "react"
import Feature from "./Feature"
import target from "../../assets/scheduling_large_target_graphic.jpg"
import rmp from "../../assets/rmp_logo.jpg"
import another from "../../assets/another_image.jpg"
export default function Features(){

    return (
        <div id="features">
            <div id="features-top">
                <p id="feature-header">features</p>
                <p id="features-sub">Let our schedule helper <br/>  pick classes for you</p>
            </div>
            <div id="features-list">
                <Feature 
                    img={target}
                    name="Build"
                    text="Fill in your desired courses and our generators will pick a selection of schedules for you to chose from"
                />
                <Feature 
                    img={another}
                    name="Save Time"
                    text="Skip the hassle of juggling the webreg, calendar, and the USC course catalog"
                />
                <Feature 
                    img={rmp}
                    name = "Reviews"
                    text = "We're integrated with RMP, removing the need to clutter your browser with professor reviews"
                />


            </div>
        </div>
        
    )
}