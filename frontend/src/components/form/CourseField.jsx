import React from "react";

export default function CourseField(props){
    return (
    <div className="form-group">
        <label htmlFor="course_ids">Course {props.number}</label>
        <input type="course" className="form-control" id="course_ids" placeholder={props.placeholder}/>
    </div>
    )


}