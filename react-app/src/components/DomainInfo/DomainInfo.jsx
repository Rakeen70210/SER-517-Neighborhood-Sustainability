import React, {useState} from 'react';
import './DomainInfo.css'

export default function DomainInfo({info, obj}) {
	const [isOpen, setIsOpen] = useState(false);


	var rows = []	

	for (const [key, value] of Object.entries(info)) {
		if(key !== "name" && key !== "score"){
			
			rows.push(<h3 className="subdomainName"> {key + ":\t " + value.score} </h3>);
			const listItems = Object.keys(value["breakdown"]).map((colName) => <li className="listItem">{colName + ": " + obj[colName]}</li>)
			rows.push(<ul>{listItems}</ul>);
		}
	}



	return (
		<div className="DomainInfo">
			<button className={"toggle "+info.name} onClick = {() => setIsOpen(!isOpen)}>
				{info.name + ": " + info.score}
			</button>
			{isOpen && <div className={"contents " + info.name}>
		      <React.Fragment>
				  {rows}
			  </React.Fragment>

			</div>}
		</div>
	);
}
