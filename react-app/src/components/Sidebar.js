import React, { useState } from 'react';
import { FaBars } from 'react-icons/fa';
import { AiOutlineDoubleRight } from 'react-icons/ai';
import { IconContext } from 'react-icons';
import './Sidebar.css';
import City from './City';
import Details from './Details';
import Chart from './Chart/Chart';

function Sidebar() {
  const [sidebar, setSidebar] = useState(false);

  const showSidebar = () => {
    setSidebar(!sidebar);
  };

  //
  const data = JSON.stringify({
    "insurance": 8.8,
    "past_trade_dollars_2020": 410087.1744,
    "county": "Ramsey",
    "frequent_physical_distress_in_2018_percent": 10.3,
    "air_pollution_2018": 7.8,
    "alltransit_performance_score": 7.7,
    "preventive_services_2018": 36.3,
    "speak_a_language_other_than_english": 22.4,
    "score": "62.88",
    "percentage_of_residents_living_in_poverty_in_2019": 15.9,
    "foreign_born": 20.8,
    "state_annual_total_nonrenewables_net_generation_m_wh_2020": 40636378.0,
    "state": "Minnesota",
    "state_id": "MN",
    "government_finances_revenue_per_resident_in_2018": 2362.8,
    "two_or_more_races": 4.2,
    "longitude": -93.104,
    "population": 308096.0,
    "government_finances_cash_and_securities_per_resident_in_2018": 13838.1,
    "name": "St.Paul",
    "future_trade_tons_2030": 598128.9857,
    "population_percent": 32.6,
    "crimes_occurred": 16.1,
    "walkability_2019": 59.8,
    "city_id": 1840008940.0,
    "past_trade_tons_2020": 551319.2859,
    "employees_imputed_2017": 17.86,
    "registered_voters": 74.01,
    "latitude": 44.9477,
    "park_access": 70.5,
    "park_access_2018": 98.3,
    "zips": 5.5114551175511656e+104,
    "walkability": 36.5,
    "county_fips": 27123.0,
    "air_quality_2020": 7.3,
    "broadband_connection_2019": 70.3,
    "government_finances_debt_per_resident_in_2018": 18123.32,
    "bachelors_degree_or_higher": 43.6,
    "unemployment_in_november_2020": 4.6,
    "violent_crimes": 1329.8,
    "median_gross_rent_in_2019": 1001.0,
    "religious_diversity": 50.0,
    "cost_of_living_index_in_march_2019": 113.0,
    "government_finances_expenditure_per_resident_in_2018": 2690.24,
    "density": 2288.0,
    "revenue_imputed_2017": 19.8,
    "vacant_houses": 0.172975504,
    "state_annual_total_renewables_net_generation_m_wh_2020": 15864248.0,
    "future_trade_dollars_2030": 482276.5035,
    "close_access_to_healthy_foods": 44.0,
    "average_domestic_production_to_consumption_ratio_2020": 1.314962129,
    "payroll_imputed_2017": 16.07,
    "state_annual_co_2_equivalent_total_output_emission_rate_lb_m_wh_2020": 770.366,
    "Ecology": {
        "WaterAndAir": {
            "breakdown": {
                "air_quality_2020": 92.91262135922331,
                "air_pollution_2018": 81.13207547169812
            },
            "score": 87.02
        },
        "HabitatAndSettlements": {
            "breakdown": {
                "park_access_2018": 98.49699398797596
            },
            "score": 98.5
        },
        "BuiltFormAndTransport": {
            "breakdown": {
                "alltransit_performance_score": 80.20833333333334
            },
            "score": 80.21
        },
        "EmbodimentAndSustenance": {
            "breakdown": {
                "frequent_physical_distress_in_2018_percent": 50.95238095238095
            },
            "score": 50.95
        },
        "score": 79.17
    },
    "Economics": {
        "ProductionAndResourcing": {
            "breakdown": {
                "cost_of_living_index_in_march_2019": 56.64160401002506
            },
            "score": 56.64
        },
        "ExchangeAndTransfer": {
            "breakdown": {
                "past_trade_dollars_2020": 13.462734111588096,
                "past_trade_tons_2020": 20.039568177162757,
                "future_trade_dollars_2030": 13.075478846733308,
                "future_trade_tons_2030": 20.03516378016979
            },
            "score": 16.65
        },
        "AccountingAndRegulation": {
            "breakdown": {
                "government_finances_expenditure_per_resident_in_2018": 11.352483419046079,
                "government_finances_revenue_per_resident_in_2018": 11.918026494255106,
                "government_finances_debt_per_resident_in_2018": 66.08836491665163,
                "government_finances_cash_and_securities_per_resident_in_2018": 54.70874072363825
            },
            "score": 36.02
        },
        "ConsumptionAndUse": {
            "breakdown": {
                "average_domestic_production_to_consumption_ratio_2020": 42.16157746497934
            },
            "score": 42.16
        },
        "LabourAndWelfare": {
            "breakdown": {
                "revenue_imputed_2017": 84.39897698209718,
                "payroll_imputed_2017": 67.89184621884242,
                "employees_imputed_2017": 64.3371757925072
            },
            "score": 72.21
        },
        "TechnologyAndInfrastructure": {
            "breakdown": {
                "broadband_connection_2019": 76.57952069716775,
                "preventive_services_2018": 83.06636155606407,
                "park_access_2018": 98.49699398797596,
                "walkability_2019": 63.347457627118644
            },
            "score": 80.37
        },
        "WealthAndDistribution": {
            "breakdown": {
                "unemployment_in_november_2020": 89.95215311004785,
                "percentage_of_residents_living_in_poverty_in_2019": 62.95336787564767,
                "median_gross_rent_in_2019": 36.268115942028984
            },
            "score": 63.06
        },
        "score": 52.44
    },
    "Culture": {
        "IdentityAndEngagement": {
            "breakdown": {
                "two_or_more_races": 24.000000000000004
            },
            "score": 24.0
        },
        "GenderAndGenerations": {
            "breakdown": {
                "speak_a_language_other_than_english": 24.137931034482758
            },
            "score": 24.14
        },
        "CreativityAndRecreation": {
            "breakdown": {
                "park_access": 70.57057057057057
            },
            "score": 70.57
        },
        "MemoryAndProjection": {
            "breakdown": {
                "foreign_born": 27.476882430647294
            },
            "score": 27.48
        },
        "BeliefsAndIdeas": {
            "breakdown": {
                "religious_diversity": 66.66666666666666
            },
            "score": 66.67
        },
        "EnquiryAndLearning": {
            "breakdown": {
                "bachelors_degree_or_higher": 53.76078914919853
            },
            "score": 53.76
        },
        "WellbeingAndHealth": {
            "breakdown": {
                "walkability": 38.66525423728813,
                "close_access_to_healthy_foods": 65.67164179104478
            },
            "score": 56.67
        },
        "score": 46.18
    },
    "Politics": {
        "OrganizationAndGovernance": {
            "breakdown": {
                "vacant_houses": 48.76763880321352
            },
            "score": 48.77
        },
        "LawAndJustice": {
            "breakdown": {
                "population_percent": 86.01583113456465
            },
            "score": 86.02
        },
        "CommunicationAndCritique": {
            "breakdown": {
                "crimes_occurred": 77.40384615384616
            },
            "score": 77.4
        },
        "RepresentationAndNegotiation": {
            "breakdown": {
                "registered_voters": 87.68957345971565
            },
            "score": 87.69
        },
        "SecurityAndAccord": {
            "breakdown": {
                "violent_crimes": 68.81954147906639
            },
            "score": 68.82
        },
        "score": 73.74
    }
  });

  //

  return (
    <>
        <div className='navbar'>
            <div className='button-bar'>
                <IconContext.Provider value={{ color: '#fff' }}>
                <FaBars onClick={showSidebar} />
                </IconContext.Provider>
            </div>
        </div>
        <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}>
            <ul className='nav-menu-items'>
                <li className='navbar-toggle'>
                    <div className='menu-bar'>
                        <IconContext.Provider value={{ color: '#fff' }}>
                        <AiOutlineDoubleRight onClick={showSidebar}/>
                        </IconContext.Provider>
                    </div>
                </li>
                <City data={data}/>
                <Details/>
                <div className='chartPanel'>
                    <Chart city={data}/>
                </div>
            </ul>
        </nav>
    </>
  );
}

export default Sidebar;