import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import $ from 'jquery'; 

export default function Login(){
    
    //username
    
    //email
    //password
    function Login(event){
        event.preventDefault();
        const url="http://3.144.82.207/auth/login/"
        const username = document.getElementById("username").value
        const password = document.getElementById("password").value

        //make ajax query to register user
        let formData = `username=${username}&password=${password}`
        
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
                <form className="registration-box" onSubmit={Login}>
                    <div className="row justify-content-center">
                        <div className="form-group form-units col-3">
                        <h1 className="registration-header">Log In</h1>
                        </div>
                    </div>
                    
                    <div className="row justify-content-center">
                        <div className="form-group form-units col-9">
                            <input required id="username" type="text" className="form-control" placeholder="Username"/>
                        </div>
                    </div>

                    <div className="row justify-content-center">
                        <div className="form-group form-units col-9">
                        
                            <input required id="password" type="password" className="form-control" placeholder="Password"/>
                        </div>
                    </div>
                    
                    <div className="row justify-content-center">
                        <div className="form-group form-units col-9">
                        <button type="submit" className="btn btn-primary register-button">log in</button>
                        </div>
                    </div>

                    <div className="row justify-content-center">
                        <div className="form-group form-units col-9">
                        <p className="alr-have">Don't have an account? <a href="register">Register Here</a> </p> 
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    </div>



    </>)
}