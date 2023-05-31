#Nesting
capital = {
            "India" : "Delhi",
            "France":"Paris",
            "Germany":"Berlin"
}

#Nesting a list in dictionary

travel_log_01 = {
                "India":["Hyderabad","Mumbai","Bangalore"],
                "France":["Paris","Lille","Dijon"],
               "Germany":["Berlin","Hamburg","Stuttgart"]
}

#Nesting a Dictionary in a Dictionary

travel_log_02 = {
                "India":{
                            "Cities_visited": ["Hyderabad","Mumbai","Bangalore"],
                            "Total_visites":12
                        },
                "France":{
                            "Cities_visited":["Paris","Lille","Dijon"],
                            "Total_visited":3
                        }  ,
               "Germany":{
                            "Cities_visited":["Berlin","Hamburg","Stuttgart"],
                            "Total_visited":3
                         }
}

#Nesting a Dictionary in List

travel_log_02 = [
                    {   
                        "Country":"India",
                        "Cities_visited": ["Hyderabad","Mumbai","Bangalore"],
                        "Total_visites":12
                    },
                    {   
                        "Country":"France",
                        "Cities_visited":["Paris","Lille","Dijon"],
                        "Total_visited":3
                    }  ,
                    {
                        "Country":"Germany",
                        "Cities_visited":["Berlin","Hamburg","Stuttgart"],
                        "Total_visited":3
                    }
]