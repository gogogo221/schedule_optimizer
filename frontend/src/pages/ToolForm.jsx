import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar"
import Footer from "../components/Footer"
import CourseField from "../components/form/CourseField";



export default function ToolForm(){
  const [count, setCount] = useState(0)

  return (
    <>    
    <Navbar />
    <div>
        <form>
          
          {/* semester */}
          <div className="form-group">
            <label htmlFor="semester_id">Semester</label>
            <select className="form-control" id="semester_id">
            <option value="20231">2023 Spring</option>
            <option value="20232">2023 Summer</option>
            <option value="20233">2023 Fall</option>
            <option value="20241">2024 Spring</option>
            <option value="20242">2024 Summer</option>
            <option value="20243">2024 Fall</option>
            </select>
        </div>
        {/* courses */}
        <CourseField number="1" placeholder="CSCI-104" />
        <CourseField number="2" placeholder="CSCI-201" />
        <CourseField number="3" placeholder="CSCI-270" />
        
        {/* required courses */}
        {/* blocked out times */}
        {/* want available seats */}
        <div className="form-check">
          <input className="form-check-input" type="checkbox" value="True" id="available"/>
          <label className="form-check-label" htmlFor="available">
            Only want courses with available seats
          </label>
        </div>

        
        <div class="form-group row">
          {/* min rmp */}
          <div class="col">
            <label for="min_rmp">Minimum RMP Score</label>
            <input id="min_rmp" type="text" class="form-control" placeholder="2.3"/>
          </div>
          {/* max rmp difficulty */}
          <div class="col">
            <label for="max_rmp_difficulty">Maximum RMP Difficulty</label>
            <input id="max_rmp_difficulty" type="text" class="form-control" placeholder="3.8"/>
          </div>
          {/* units wanted */}
          <div class="col">
            <label for="units_wanted">Units Wanted</label>
            <input id="units_wanted" type="text" class="form-control" placeholder="12"/>
          </div>
        </div>
        {/* submit */}
        <button type="submit" class="btn btn-primary">Generate</button>
        </form>
    </div>

    <Footer />
    </>
  )
}