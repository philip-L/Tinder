'''This is the command line interface for tinder with auto swiping, messaging (commented out) run in terminal like "python tinder_cli.py" '''

import features as tinder
import tinder_api as api
from time import sleep
import argparse

#if __name__ == '__main__':

if api.authverif():
    '''loop while there are matches available'''
    '''will need to check the response from a swipe and send msg if it's a match then continue swiping'''
    '''will need to have a stopping case when there's no one left or I'm out of swipes'''
    try:
        nap_length = 0.5
        while 1:
            user_info = tinder.get_users_to_swipe()
            if len(user_info) == 0:
                break  # no users to swipe on
            for index in range(len(user_info)):
                sleep(nap_length)
                print('Napping for %f seconds...' % nap_length)

                user_id = user_info[index]["id"]
                user_name = user_info[index]["name"]

                print("Swiping right on " + user_name)
                result = api.like(user_id)
                print(str(result['likes_remaining']) + " likes remaining")
                if result['likes_remaining'] == 0:
                    print("No likes remaining... exiting")
                    exit(0)

            # code to check matches with 0 messages and send automatic message
            '''match_info = get_match_info()
            for match in match_info:
                person = match_info[match]
                messages_len = len(person["messages"])
                if messages_len == 0:
                    api.send_msg(person["match_id"], "Hey you're cute! Add me on snapchat @pa_leblanc :)")'''
            # pprint(getmembers(match_info)) # to var dump

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

else:
    print("Something went wrong. You were not authorized.")
