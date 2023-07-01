import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar"
import Hero from "../components/landing/Hero"
import Footer from "../components/Footer"
import Features from "../components/landing/Features"


export default function Landing(){
    const [count, setCount] = useState(0)

    return (
      <>    
      <Navbar />
      <div className="container">
        <div className="row">
          <div className="col-12">
          <Hero />
          <Features />
          </div>
        </div>
        
      </div>
      <Footer />
  
      </>
    )
}