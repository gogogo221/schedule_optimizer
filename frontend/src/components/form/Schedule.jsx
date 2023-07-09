import React, { Component } from "react";
import Course from "./Course";
import {DayPilotCalendar} from "@daypilot/daypilot-lite-react";

export default class Schedule extends Component{
    constructor(props){
        super(props)
        this.course_combos = props.schedule ? props.schedule["course_combos"] : null
        const start_date = "2023-01-01"
        const colors = ["#e52b50", "#8155be", "#318ce7", "#139139", "#ffbf00"]
        let id_counter = 1
        
        let schedule_format_course = []
        for (let i=0; i<this.course_combos.length; i++){
            let course_combo = this.course_combos[i]
            
            const course = course_combo.course
            const sessions = course_combo.sessions
   
            

            const tag = course.tag
            const color = colors[i]
            for (let j = 0; j< sessions.length; j++){
                const session = sessions[j]
                let type = session.type
                let time = session.time 
                
                
                let days = time.day
             
                for (let k = 0; k < days.length; k++){
                    let day = days.charAt(k)
                    const start = `${start_date}T${time.start}:00`
                    const end = `${start_date}T${time.end}:00`
                    const text = tag + " " + type + " | id " + session.id + "\n" 
                        + session.registered + "/" + session.capacity + " registered" + "\n"
  
                    schedule_format_course.push({
                        id: id_counter,
                        text: text,
                        start: start,
                        end: end,
                        resource: day,
                        barColor: color
                    })
                    id_counter++
                }
            }
            
            
        }


        this.state = {
            viewType: "Resources",
            startDate: "2023-01-01",
            columns: [
              {name: "Monday", id: "M"},
              {name: "Tuesday", id: "T"},
              {name: "Wednesday", id: "W"},
              {name: "Thursday", id: "H"},
              {name: "Friday", id: "F"},
            ],
            events: schedule_format_course,
            heightSpec: "BusinessHours",
            businessBeginsHour: 8,
            businessEndsHour: 22,
            cellHeight: 20,
            

            
          };
    }

    render(){
        return(
            <>
    
    
            <div className="schedule-box row">
                {this.course_combos ? this.course_combos.map((course_combo,index)=><Course course_combo={course_combo} key={index} />) : ""}
                <DayPilotCalendar
                    {...this.state}
                />
            </div>
                
            </>
        )
    }
    
} 