import React from "react"
import CourseField from "./CourseField"
import $ from 'jquery'; 

export default function Form(props){


    function GetCourses(event) {
        event.preventDefault();
        props.setSchedule(null)
        //http://127.0.0.1:8000/generate/?available=True&courses=CSCI-104&courses=CSCI-201&format=json&semester_id=20231&units_wanted=8
        let url = "http://127.0.0.1:8000/generate/?"
        //semester_id
        url += `semester_id=${semester_id.value}`

        //units wanted
        url+= `&units_wanted=${units_wanted.value}`

        //want open
        url+= `&want_available=${want_available.checked}`

        //courses
        for (let i = 0; i<course_ids.length; i++){
            let id = course_ids[i].value
            if (id.length > 0){
                url+= `&courses=${id}`
            }
        }

        //min_rmp
        if(min_rmp.value.length > 0){
            url += `&min_rmp=${min_rmp.value}`
        }

        //max rmp difficulty
        if(max_rmp_difficulty.value.length > 0){
            url += `&max_rmp_difficulty=${max_rmp_difficulty.value}`
        }

        function shuffle(array) {
            let currentIndex = array.length,  randomIndex;
          
            // While there remain elements to shuffle.
            while (currentIndex != 0) {
          
              // Pick a remaining element.
              randomIndex = Math.floor(Math.random() * currentIndex);
              currentIndex--;
          
              // And swap it with the current element.
              [array[currentIndex], array[randomIndex]] = [
                array[randomIndex], array[currentIndex]];
            }
          
            return array;
          }

        //make a ajax querry to get json response 
        let formData = ""
        $.ajax({
            url: url,
            type: "GET", 
            beforeSend: function(request) {
                request.setRequestHeader("Authorization", `Token ${localStorage.getItem("Token")}`);
              },
            data: formData,
            dataType: "text",
            
            success: function (data){
                
                let data_obj = JSON.parse(JSON.parse(data))
                data_obj = shuffle(data_obj)
                props.setSchedule(data_obj.slice(0, Math.min(10, data_obj.length)))
                props.setSemesterState(semester_id.value)
                props.setUnitsState(units_wanted.value)

            },
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


    return (
        <>
        <div className="container form-container">
                <div className="row form-wrapper">
                    <div className="col-12">
                        <h1>Course Form</h1>
                        <form id="classForm" className="" onSubmit={GetCourses}>
                        <h3 className="form-subheading">General Information</h3>
                        {/* semester */}
                        <div className="form-group form-semester row">
                            <div className="col-6">
                                <label className="" htmlFor="semester_id">Semester</label>
                                
                                <select className="form-control col-6" id="semester_id">
                                <option value="20231">2023 Spring</option>
                                <option value="20232">2023 Summer</option>
                                <option value="20233">2023 Fall</option>
                                <option value="20241">2024 Spring</option>
                                <option value="20242">2024 Summer</option>
                                <option value="20243">2024 Fall</option>
                                </select>
                            </div>
                            <div className="col-6">

                            </div>
                            
                        </div>
                        <div className="row">
                        {/* units wanted */}
                        <div className="form-group form-units col-6">
                            <label className="" htmlFor="units_wanted">Units Wanted</label>
                            <input required id="units_wanted" type="text" className="form-control" placeholder="16"/>
                        </div>
                        </div>
                        
                        

                        {/* want available seats */}
                        <div className="form-check form-group">
                            <input className="form-check-input" type="checkbox" name="want_available" id="want_available"/>
                            <label  className="form-check-label" htmlFor="available">
                                Only courses with open seats
                            </label>
                        </div>

                        <h3 className="form-subheading">Courses</h3>

                        {/* courses */}
                        <CourseField number="1" placeholder="CSCI-104" />
                        <CourseField number="2" placeholder="CSCI-201" />
                        <CourseField number="3" placeholder="CSCI-270" />
                        <CourseField number="4" placeholder="CSCI-360" />
                        {/* required courses */}
                        {/* blocked out times */}

                        <h3 className="form-subheading">Rate My Professor Info</h3>
                        <div className="form-group row">
                            {/* min rmp */}
                            <div className="col-6">
                                <label htmlFor="min_rmp">Minimum RMP Score</label>
                                <input id="min_rmp" type="text" className="form-control" placeholder="2.3"/>
                            </div>
                        </div>
                        <div className="row form-difficulty">
                            {/* max rmp difficulty */}
                            <div className="col-6">
                                <label htmlFor="max_rmp_difficulty">Maximum RMP Difficulty</label>
                                <input id="max_rmp_difficulty" type="text" className="form-control" placeholder="3.8"/>
                            </div>
                        </div>
                        {/* submit */}
                        <div className="row">
                            <button type="submit" className="btn btn-primary form-submit col-6">Generate</button>
                        </div>
                        
                        </form>
                    </div>
                    
                </div>
            </div>
        </>
    )
}