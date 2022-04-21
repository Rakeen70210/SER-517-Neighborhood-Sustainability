import React from 'react';
import {
  Chart as ChartJS,
  RadialLinearScale,
  ArcElement,
  Tooltip,
  Legend,
} from 'chart.js';
import DomainInfo from '../DomainInfo/DomainInfo';
import { PolarArea } from 'react-chartjs-2';
import "./Chart.css";
ChartJS.register(RadialLinearScale, ArcElement, Tooltip, Legend);


export default function Chart({ city }) {
    

    city = {    "insurance": 21.5,    "past_trade_dollars_2020": 308208.2221,    "county": "Jefferson",    "frequent_physical_distress_in_2018_percent": 16.6,    "air_pollution_2018": 10.3,    "alltransit_performance_score": 0.2,    "preventive_services_2018": 30.1,    "speak_a_language_other_than_english": 2.8,    "score": "54.41",    "percentage_of_residents_living_in_poverty_in_2019": 25.2,    "foreign_born": 4.1,    "state_annual_total_nonrenewables_net_generation_m_wh_2020": 119834631.0,    "state": "Alabama",    "state_id": "AL",    "government_finances_revenue_per_resident_in_2018": 3320.85,    "two_or_more_races": 1.3,    "longitude": -86.7987,    "population": 739573.0,    "government_finances_cash_and_securities_per_resident_in_2018": 2470.21,    "name": "Birmingham",    "future_trade_tons_2030": 413998.9279,    "population_percent": 18.6,    "crimes_occurred": 14.0,    "walkability_2019": 35.4,    "city_id": 1840006507.0,    "past_trade_tons_2020": 375360.0095,    "employees_imputed_2017": 19.67,    "registered_voters": 64.34,    "latitude": 33.5277,    "park_access": 51.2,    "park_access_2018": 45.8,    "zips": 3.5218352143521536e+249,    "walkability": 35.4,    "county_fips": 1073.0,    "air_quality_2020": 8.8,    "broadband_connection_2019": 53.9,    "government_finances_debt_per_resident_in_2018": 13865.34,    "bachelors_degree_or_higher": 29.5,    "unemployment_in_november_2020": 6.8,    "violent_crimes": 356.3,    "median_gross_rent_in_2019": 839.0,    "religious_diversity": 53.0,    "cost_of_living_index_in_march_2019": 86.6,    "government_finances_expenditure_per_resident_in_2018": 3387.07,    "density": 553.0,    "revenue_imputed_2017": 19.81,    "vacant_houses": 0.067492507,    "state_annual_total_renewables_net_generation_m_wh_2020": 17007402.0,    "future_trade_dollars_2030": 363950.4192,    "close_access_to_healthy_foods": 20.0,    "average_domestic_production_to_consumption_ratio_2020": 0.931252416,    "payroll_imputed_2017": 17.33,    "state_annual_co_2_equivalent_total_output_emission_rate_lb_m_wh_2020": 721.058,    "Ecology": {        "WaterAndAir": {            "breakdown": {                "air_quality_2020": 91.45631067961165,                "air_pollution_2018": 530.4504504504505            },            "score": 31.95        },        "HabitatAndSettlements": {            "breakdown": {                "park_access_2018": 44.15718717683556            },            "score": 44.16        },        "BuiltFormAndTransport": {            "breakdown": {                "alltransit_performance_score": 2.0833333333333335            },            "score": 2.08        },        "EmbodimentAndSustenance": {            "breakdown": {                "frequent_physical_distress_in_2018_percent": 20.952380952380945            },            "score": 20.95        },        "score": 94.53    },    "Economics": {        "ProductionAndResourcing": {            "breakdown": {                "cost_of_living_index_in_march_2019": 6.539735099337742            },            "score": 6.54        },        "ExchangeAndTransfer": {            "breakdown": {                "past_trade_dollars_2020": 10.11815439292507,                "past_trade_tons_2020": 13.643731851455824,                "future_trade_dollars_2030": 9.867422470249622,                "future_trade_tons_2030": 13.867470936196103            },            "score": 11.87        },        "AccountingAndRegulation": {            "breakdown": {                "government_finances_expenditure_per_resident_in_2018": 12.224966982208425,                "government_finances_revenue_per_resident_in_2018": 16.550476490955567,                "government_finances_debt_per_resident_in_2018": 468.0555469665088,                "government_finances_cash_and_securities_per_resident_in_2018": 9.765906068287807            },            "score": 26.65        },        "ConsumptionAndUse": {            "breakdown": {                "average_domestic_production_to_consumption_ratio_2020": 29.85870848348452            },            "score": 29.86        },        "LabourAndWelfare": {            "breakdown": {                "revenue_imputed_2017": 84.44160272804774,                "payroll_imputed_2017": 73.21504013519221,                "employees_imputed_2017": 70.85734870317003            },            "score": 76.17        },        "TechnologyAndInfrastructure": {            "breakdown": {                "broadband_connection_2019": 32.68206039076376,                "preventive_services_2018": 53.58361774744027,                "park_access_2018": 44.15718717683556,                "walkability_2019": 32.8782707622298            },            "score": 40.83        },        "WealthAndDistribution": {            "breakdown": {                "unemployment_in_november_2020": 326.6304347826087,                "percentage_of_residents_living_in_poverty_in_2019": 196.21621621621622,                "median_gross_rent_in_2019": 9.55743879472693            },            "score": 77.47        },        "score": 67.06    },    "Culture": {        "IdentityAndEngagement": {            "breakdown": {                "two_or_more_races": 5.263157894736842            },            "score": 5.26        },        "GenderAndGenerations": {            "breakdown": {                "speak_a_language_other_than_english": 0.4424778761061946            },            "score": 0.44        },        "CreativityAndRecreation": {            "breakdown": {                "park_access": 47.46494066882416            },            "score": 47.46        },        "MemoryAndProjection": {            "breakdown": {                "foreign_born": 3.892617449664429            },            "score": 3.89        },        "BeliefsAndIdeas": {            "breakdown": {                "religious_diversity": 65.625            },            "score": 65.62        },        "EnquiryAndLearning": {            "breakdown": {                "bachelors_degree_or_higher": 29.218106995884778            },            "score": 29.22        },        "WellbeingAndHealth": {            "breakdown": {                "walkability": 32.8782707622298,                "close_access_to_healthy_foods": -67.85714285714286            },            "score": -34.28        },        "score": 16.8    },    "Politics": {        "OrganizationAndGovernance": {            "breakdown": {                "vacant_houses": 14.248075493563967            },            "score": 14.25        },        "LawAndJustice": {            "breakdown": {                "population_percent": 46.83195592286501            },            "score": 46.83        },        "CommunicationAndCritique": {            "breakdown": {                "crimes_occurred": 64.3979057591623            },            "score": 64.4        },        "RepresentationAndNegotiation": {            "breakdown": {                "registered_voters": 53.55406344061125            },            "score": 53.55        },        "SecurityAndAccord": {            "breakdown": {                "violent_crimes": 17.11806468577439            },            "score": 17.12        },        "score": 39.23    }}
    
    
    const colours = [
        ["FF1700", "EF4F3F", "C23C2F", "92251A", "A00F00", "CC1503", "E01804"], // red
        ["005EFD", "2D77F5", "5991F1", "4172C5", "1E4D9C", "04307A", "002769"], // blue
        ["FCCB00", "F3CD30", "E9D16D", "BDA74E", "8F791F", "8A6F00", "B89504"], // yellow
        ["85FF00", "A0F642", "9DD65F", "76A345", "568B1B", "3E6315", "539E00"]  // green
    ]

    var subDomainsLabels = []
    var subDomainsData = []
    var backgroundColor = []


    // Ecology
    var i = 0;
    for (const [key, value] of Object.entries(city.Ecology)) {
        if(key !== "score"){
            subDomainsLabels.push(key);
            subDomainsData.push(value.score);
            backgroundColor.push("#"+colours[0][i++]);
        }
    }

    // Economics
    i = 0;
    for (const [key, value] of Object.entries(city.Economics)) {
        if(key !== "score"){
            subDomainsLabels.push(key);
            subDomainsData.push(value.score);
            backgroundColor.push("#"+colours[1][i++]);
        }
    }

    // Politics
    i = 0;
    for (const [key, value] of Object.entries(city.Politics)) {
        if(key !== "score"){
            subDomainsLabels.push(key);
            subDomainsData.push(value.score);
            backgroundColor.push("#"+colours[2][i++]);
        }
    }

    // Culture
    i = 0;
    for (const [key, value] of Object.entries(city.Culture)) {
        if(key !== "score"){
            subDomainsLabels.push(key);
            subDomainsData.push(value.score);
            backgroundColor.push("#"+colours[3][i++]);
        }
    }


    // ['Red: Ecology', 'Blue: Economics', 'Yellow: Politics', 'Green: Culture'],
    const data = {
      labels: subDomainsLabels,     
      datasets: [
        {
          label: '# of Votes',
          data: subDomainsData,
          backgroundColor: backgroundColor,
          borderWidth: 1,
        },
	  ],
    options: {
          plugins:{   
             legend: { hidden: true }
                }

    }
    };


    city.Ecology.name = "Ecology";
    city.Economics.name = "Economics";
    city.Politics.name = "Politics";
    city.Culture.name = "Culture";


    return <>
        <div className="chart">
            <PolarArea data={data} />
            <DomainInfo info={city.Ecology} obj={city} />
            <DomainInfo info={city.Economics} obj={city}/>
            <DomainInfo info={city.Politics} obj={city}/>
            <DomainInfo info={city.Culture} obj={city}/>
        </div>
    </>
}



