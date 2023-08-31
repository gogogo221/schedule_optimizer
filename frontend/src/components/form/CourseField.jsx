import React from "react";

export default function CourseField(props){
    return (
    <div className="form-group row course-field">
        <label className="col-1" htmlFor="course_ids">Course {props.number}</label>
        <div className="col-5">
            <input type="text" className="form-control" id="course_ids" defaultValue={props.placeholder} />
        </div>
    </div>
    )


}