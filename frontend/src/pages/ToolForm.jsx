import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar"
import Footer from "../components/Footer"




export default function ToolForm(){
    const [count, setCount] = useState(0)

    return (
      <>    
      <Navbar />
      <div>
            <form>
                <div class="form-group">
                    <label for="exampleFormControlInput1">Email address</label>
                    <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com"/>
                </div>
            </form>
      </div>

      <Footer />
      </>
    )
}