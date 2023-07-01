import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar"
import Footer from "../components/Footer"
import CourseField from "../components/form/CourseField";
import Form from "../components/form/Form";
import Results from "../components/form/Results";


export default function ToolForm(){
  const [scheduleResult, setScheduleResult] = useState(0)

  return (
    <>    
    <Navbar />
    <Form  schedule={scheduleResult} setSchedule={setScheduleResult} />
    <Results schedule={scheduleResult} setSchedule={setScheduleResult} /> 
    <Footer />
    </>
  )
}