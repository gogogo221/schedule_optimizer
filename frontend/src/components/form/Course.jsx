import React, { useEffect, useState } from "react";
import Session from "./Session";


export default function Course(props)
{
    const course_combo = props.course_combo ? props.course_combo : null
    const course = course_combo ? course_combo.course : null
    const sessions = course_combo ? course_combo.sessions : null

    let professors = []
    for (let i = 0; i<sessions.length; i++){
        let session = sessions[i]
        for (let j = 0; j<session.professor.length; j++){
            professors.push(session.professor[j])
        }
    }

    return(
        props.course_combo ? 
        <div className="course-box col-12">
            <div className="course-info row">
                <h4 className="col-2">{course.tag}</h4>
                <h5 className="col-1">units: {course.units}</h5>
                <h5 className="col-4">instructor: {professors[0].name} </h5>
                <h5 className="col-1">⭐ {professors[0].rating}  </h5>
                <h5 className="col-1"> 💀 {professors[0].difficulty}</h5>
                <h5 className="col-2"> {professors[0].num_ratings} ratings</h5>

            </div>
            
        </div>
        : ""
    )
    
    
}