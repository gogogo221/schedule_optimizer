import React, { useEffect, useState } from "react";
import Course from "./Course";

export default function Schedule(props){
    let courses = props.schedule ? props.schedule["course_combos"] : null
    
    return(
        <>


        <div className="schedule-box row">
            {courses ? courses.map((course_combo,index)=><Course course_combo={course_combo} key={index} />) : ""}

        </div>
            
        </>
    )
} 