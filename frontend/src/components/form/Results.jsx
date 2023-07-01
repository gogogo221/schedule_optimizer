import React, { useEffect, useState } from "react";
import Schedule from "./Schedule";

export default function Results(props){
    const schedules = props.schedule

    //const session = schedules[0]["course_combos"][0]["sessions"][0]
    //const schedule1 = schedules[0]
    //const course = schedules[0]["course_combos"]
    //const course_combos = schedule1["course_combos"]
 
 
    return (
        <>
        
        <div className="schedules-container container">
                    
            <table className="table">
            <thead className="form-result-table">
                <tr>
                <th scope="col">#</th>
                <th scope="col">Schedules</th>
                </tr>
            </thead>
            
            <tbody className="course-table-row">
                {
                schedules ? 
                schedules.map((schedule,index) => 
                <tr key={index}>
                    <th scope="row">{index+1}</th>
                    <td><Schedule schedule={schedule} /></td>
                </tr>) : null
                }
            </tbody>
            </table>
            
            {/* <p>{JSON.stringify(schedule1)}</p>  */}

            {/* <p>{JSON.stringify(course)}</p> */}
        </div>
            
        </>
    )

}