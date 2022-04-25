import React from 'react'
import { RiCommunityLine } from 'react-icons/ri'
import './City.css'

function City({data}) {
  const cityData = JSON.parse(data);

  function getCityName(){
    if (typeof(sessionStorage) !='undefined'){
      if(cityData != null) 
        if(typeof cityData.name != undefined && cityData.name !== undefined) 
          return cityData.name;
    }
    return 'Unknown';
  }

  function getCityScore(){
    if (typeof(sessionStorage) !='undefined'){
      if(cityData != null) 
        if(typeof cityData.score != undefined && cityData.score !== undefined) 
        return cityData.score;
    }
    return '0';
  }

  function getCityRank(){
    if (typeof(sessionStorage) !='undefined'){
      if(cityData != null) 
        if(typeof cityData.rank != undefined && cityData.rank !== undefined) 
          return cityData.rank;
    }
    return '0';
  }
  
  return (
    <>
      <div className='title'>
        <RiCommunityLine/>
        <h1 title='City Name'>{getCityName()}</h1>
      </div>
      <div className='scoreAndRank'>
        <span title='City Score'>Score: {getCityScore()}</span>
        <span title='City Rank'>Rank: {getCityRank()}</span>
      </div>
    </>
  )
}

export default City