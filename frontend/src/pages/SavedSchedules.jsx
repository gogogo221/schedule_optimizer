import React, { useEffect, useState } from "react";
import $ from 'jquery'; 
import Navbar from "../components/Navbar"
import Footer from "../components/Footer"
import Schedule from "../components/form/Schedule";

class SavedSchedules extends React.Component {
    constructor(props){
        super(props)
        this.state = {
            schedules : null
        }

        this.getSchedules = function(){
            
            $.ajax({
                url: "http://127.0.0.1:8000/getschedules",
                type: "GET", 
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization", `Token ${localStorage.getItem("Token")}`);
                  },
                dataType: "text",
                success: function (data){
                    const data_obj = JSON.parse(data)
                    this.user = data_obj.user
                    this.setState({schedules : data_obj})

    
                }.bind(this),
                error:function(x,e) {
                    if (x.status==0) {
                        alert('You are offline!!\n Please Check Your Network.');
                    }else if(x.status==401) {
                        window.location.pathname = '/login'
                    }else if(x.status==404) {
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

        this.deleteSchedule = function(event){
            const schedule_index = event.target.id.slice(-1)[0]
            console.log(this.state.schedules.schedules)
            const schedule_id = this.state.schedules.schedules[schedule_index].id
            console.log(schedule_id)
            const formData = `schedule_id=${schedule_id}`
            $.ajax({
                url: "http://127.0.0.1:8000/delete/schedule",
                type: "DELETE", 
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization", `Token ${localStorage.getItem("Token")}`);
                  },
                data: formData,
                dataType: "text",
                
                success: function (data){
                    event.target.parentElement.parentElement.remove()
                }.bind(this),
                error:function(x,e) {
                    if (x.status==0) {
                        alert('You are offline!!\n Please Check Your Network.');
                    }else if(x.status==401) {
                        window.location.pathname = '/login'
                    }else if(x.status==404) {
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

        }.bind(this)



    }
    componentDidMount() {
        this.getSchedules()
    }
    
    render() {
        return(
        <>
            <Navbar />
        
                <div className="schedules-container container saved-schedules">
                            
                    <table className="table">
                    <thead className="form-result-table">
                        <tr>
                        <th scope="col">#</th>
                        <th scope="col">Schedules</th>
                        </tr>
                    </thead>
                    
                    <tbody className="course-table-row">
                        
                        {this.state.schedules ? 
                        
                        this.state.schedules.schedules.map( (schedule, index) => 
                        <tr key={index}>
                            <th scope="row">
                                {index+1} 
                                <button type="button" id = {`delete-button-${index}`} className={`btn btn-danger `} onClick={this.deleteSchedule}>Delete Schedule</button>
                             </th>
                           
                        <td><Schedule schedule={(schedule.course_data && schedule.course_data != "[object Object]") ? JSON.parse(schedule.course_data) : null} /></td>
                        </tr>) 
                        : null}
                    </tbody>
                    </table>
                </div> 
            <Footer />
        </>)
    }
}
export default SavedSchedules;
