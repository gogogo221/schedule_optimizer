import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import $ from 'jquery'; 

export default function Register(){
    
    //username
    
    //email
    //password
    function Register(event){
        event.preventDefault();
        const url="http://127.0.0.1:8000/auth/register/"
        const username = document.getElementById("username").value
        const email = document.getElementById("email").value
        const password = document.getElementById("password").value

        //make ajax query to register user
        let formData = `username=${username}&email=${email}&password=${password}`
        
        let token = ""
        $.ajax({
            url: url,
            type: "POST", 
            async: false,
            data: formData,
            dataType: "text",
            success: function (data){
                //save the token
                let result = JSON.parse(data)
                localStorage.setItem("Token", result.token)
                window.location.pathname = '/tool-form'
                

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

    

    return(
    <>
    <Navbar />
    <div className="registration-page">
    <div className="container">
        <div className="row justify-content-center">
            <div className="col-5">
                <form className="registration-box" onSubmit={Register}>
                    <div className="row justify-content-center">
                        <div className="form-group form-units col-6">
                        <h1 className="registration-header">Create an Account</h1>
                        </div>
                    </div>
                    
                    <div className="row justify-content-center">
                        <div className="form-group form-units col-9">
                            <input required id="username" type="text" className="form-control" placeholder="Username"/>
                        </div>
                    </div>
                    <div className="row justify-content-center">
                        <div className="form-group form-units col-9">
                            <input required id="email" type="email" className="form-control" placeholder="Email"/>
                        </div>
                    </div>
                    <div className="row justify-content-center">
                        <div className="form-group form-units col-9">
                        
                            <input required id="password" type="password" className="form-control" placeholder="Password"/>
                        </div>
                    </div>
                    
                    <div className="row justify-content-center">
                        <div className="form-group form-units col-9">
                        <button type="submit" className="btn btn-primary register-button">Register</button>
                        </div>
                    </div>

                    <div className="row justify-content-center">
                        <div className="form-group form-units col-9">
                        <p className="alr-have">Already have an account? <a href="login">Log In here</a> </p> 
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    </div>



    </>)
}