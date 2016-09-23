import json
from urllib2 import urlopen
from do_not_push_to_github import *


#takes in key word entered by user
def take_in_keyword():
    search_item = raw_input("What are you searching for?")
    return search_item
    
#takes in the date,moht and year of the searched item entered by the user
def take_in_date_user_wants_to_go_out():
    month = raw_input("Please tell me the month you would like to search for, using numerical values ")

    year = raw_input("Please, tell me the year that you would like to search for ")
    

    date_string = year + "-" + month.zfill(2) + "-"+ "01" + "T00:00:00Z"
    end_Date = year + "-" + str(int(month) + 01).zfill(2) + "-" + "01" + "T00:00:00Z"
    
    print date_string
    print end_Date
    return date_string, end_Date 
    
    
#takes in the the country where user lives
def take_in_user_country():
    user_country = raw_input("Please, let me know the country that you live in? ")
    return user_country
#takes in the city where the user wants the event to be in

def take_in_user_city():

    user_location = raw_input("What city would you like the event to be in? ").replace(' ', '%20')
    return user_location

   
#this makes the keyword,city,date request to ticketmaster api
def make_keyword_request_to_ticket_master_api(user_keyword,city,startDatetime,endDateTime):
     # https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&dmaId=324&{apikey}
    
    api_url = "http://app.ticketmaster.com/discovery/v2/events.json?keyword="+ user_keyword+ "&startDateTime=" + startDatetime + "&endDateTime="+ endDateTime + "&city="+ city+ "&apikey="+api_key#&callback=myFunction"
    print api_url
    response = urlopen(api_url)

    json_obj = json.load(response)
   

    return json_obj
    
# analysis of information
   
def parse_json_obj_for_useful_info(json_obj):
    
    #navigate dictionary to get what you want:
    if json_obj.get('_embedded'):
        for event in json_obj["_embedded"]['events']:
            
            if event.get('dates'):
                print event['dates']["start"]['dateTime'] 


            if event.get('info'):
                print event['info']
            if event.get('description'):
                print event['description'].encode('ascii','ignore')
            print event['name']
    
    else:
        return "There are no events that match your keyword"



def main():
    user_keyword = take_in_keyword()

    print take_in_user_country()
    user_city = take_in_user_city()
    startDatetime, endDateTime = take_in_date_user_wants_to_go_out()


    json_obj = make_keyword_request_to_ticket_master_api(user_keyword,user_city,startDatetime,endDateTime)
    parse_json_obj_for_useful_info(json_obj)
    
    



if __name__ == '__main__':
    main()


