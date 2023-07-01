import React, { useEffect, useState } from "react";
import Session from "./Session";

export default function Course(props)
{
    const course_combo = props.course_combo ? props.course_combo : null
    const course = course_combo ? course_combo.course : null
    const sessions = course_combo ? course_combo.sessions : null
    return(
        props.course_combo ? 
        <div className="course-box col-12">
            <div className="course-info row">
            <h4 className="col-2">{course.tag}</h4>
            <p className="col-3">units: {course.units}</p>
            </div>
            {/* sessions */}
            <div className="sessions row">
                {sessions.map((session,index) => <Session key={index} session={session}/>)}
            </div>
        </div>
        : ""
    )
    
    
}