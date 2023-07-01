import React, { useEffect, useState } from "react";
import Professor from "./Professor";

export default function Session(props){
    

    return (
        <div className="col-4">
            <div className="session-box">
                <h5 className="col-12">type: {props.session.type}</h5>
                <div className="session-info sub-session row">
                    <p className="col-4">id: {props.session.id}</p>
                    <p className="col-4">d-req: {props.session.dclearence ? "Yes" : "No"}</p>
                </div>
                <div className="day-time sub-session row">
                    <p className="col-4">day: {typeof props.session.time.day ==="string" ? props.session.time.day : "None"}</p>
                    <p className="col-4">start: {props.session.time.start}</p>
                    <p className="col-4">end: {props.session.time.end}</p>
                </div>
                
                <div className="availability-info sub-session row">
                    <p className="col-12">space: {props.session.registered}/{props.session.capacity}</p>
                </div>

                {props.session.professor ? props.session.professor.map((professor, index)=> <Professor key={index} professor={professor} />) : null}


            </div>
        </div>
        
    )
}