"""Vanessa wants:
to be more adventurous by going to more activities

about Music,festivals, art, animals, food, languages, sunsets, photography
"""
import json
import urllib2

def take_in_keyword():
    # takes in user's interest via raw_input
    # return string
    pass

def take_in_date_user_wants_to_go_out():
    # takes in month by raw_input
    # takes in date by raw_input
    # takes in year by raw_input
    # return date_tuple
    pass

def take_in_time_user_wants_to_go_out():
    # takes in hour of day
    # takes in am/pm
    pass


def make_keyword_request_to_ticket_master_api(user_keyword='Shakira'):
    # user_keyword = "Madonna" #raw_input("what event to you want to search for")
    api_key = "<add key here"
    api_url = "http://app.ticketmaster.com/discovery/v1/events.json?keyword="+ user_keyword+"&apikey="+api_key+"&callback=myFunction"

    response = urllib2.urlopen(api_url)

    json_obj = json.load(response)

    return json_obj

def parse_json_obj_for_useful_info(json_obj):
    #navigate dictionary to get what you want:
    for key in json_obj:
        print key



    pass

# def make_recommendations_about_other_artists():
#     # maybe compare artist_name with other playlists
#     # would need to find another api like spotifiy or soundcloud??
#     pass

# def 

def main():
    user_keyword = raw_input("What event do you want to search for?: ")
    json_obj = make_keyword_request_to_ticket_master_api(user_keyword)
    parse_json_obj_for_useful_info(json_obj)

if __name__ == '__main__':
    main()







