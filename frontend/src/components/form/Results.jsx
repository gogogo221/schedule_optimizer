import React, { useEffect, useState } from "react";
import Schedule from "./Schedule";
import $ from 'jquery'; 

export default function Results(props){
    const schedules = props.schedule

    //const session = schedules[0]["course_combos"][0]["sessions"][0]
    //const schedule1 = schedules[0]
    //const course = schedules[0]["course_combos"]
    //const course_combos = schedule1["course_combos"]
    function saveSchedule(event){
        
        const schedule_index = event.target.id.slice(-1)[0]
        const schedule_data = schedules[schedule_index]
        console.log(schedule_data)
        const formData = `semester=${props.semesterState}&units=${props.unitsState}&course_data=${JSON.stringify(schedule_data)}`
     
        let url = "http://127.0.0.1:8000/add/schedule"
        $.ajax({
            url: url,
            type: "POST", 
            beforeSend: function(request) {
                request.setRequestHeader("Authorization", `Token ${localStorage.getItem("Token")}`);
              },
            data: formData,
            dataType: "text",
            
            success: function (data){
                
                alert("save successful")
            },
            error:function(x,e) {
                if (x.status==0) {
                    alert('You are offline!!\n Please Check Your Network.');
                } else if(x.status==404) {
                    alert('Requested URL not found.');
                } else if(x.status==500) {
                    alert('Internel Server Error.');
                } else if(e=='parsererror') {
                    alert('Error.\nParsing JSON Request failed.');
                } else if(e=='timeout'){
                    alert('Request Time out.');
                } else {
                    alert('Unknow Error.\n'+x.responseText);
                }
            }
        })

    }
 
    return (
        <>
        {schedules ? 
            <div className="schedules-container container">
                        
                <table className="table">
                <thead className="form-result-table">
                    <tr>
                    <th scope="col">#</th>
                    <th scope="col">Schedules</th>
                    </tr>
                </thead>
                
                <tbody className="course-table-row">
                    
                    {schedules.map((schedule,index) => 
                    <tr key={index}>
                        <th 
                            scope="row">{index+1} <br/>  
                            <button onClick={saveSchedule} id={`schedule-button-${index}`} className="btn btn-success">Save</button>
                        </th>
                        
                        <td><Schedule schedule={schedule} /></td>
                        
                    </tr>)}
                    
                </tbody>
                </table>
                
                {/* <p>{JSON.stringify(schedule1)}</p>  */}

                {/* <p>{JSON.stringify(course)}</p> */}
            </div> : null
        }
        </>
    )

}