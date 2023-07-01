import React, { useEffect, useState } from "react";

export default function Professor(props){
    console.log(props.professor)
    return (
        <div className="professor-info">
            <h6>Professor: {props.professor.name}</h6>
            <div className="rmp-info sub-session row">
                <p className="col-4">rating: {props.professor.rating}</p>
                <p className="col-4">num: {props.professor.num_ratings}</p>
                <p className="col-4">diff: {props.professor.difficulty}</p>
            </div>
        </div>
    )

}