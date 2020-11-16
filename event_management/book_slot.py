from datetime import datetime, timedelta
# from initialise.cal_setup import get_calendar_service
# import initialise.cal_setup.get_calendar_service as get_calendar_service
from cal_setup import get_calendar_service



def book_event(event_id, user_email, user_name):
    service = get_calendar_service()

    event = service.events().get(
        calendarId='primary',
        eventId=event_id,).execute()

    host_email = event['attendees'][0]['email']
    host_name = host_email.split('@')[0]
    summary = (f'{host_name}_{user_name}_booked_slot')
    description = (f"Code Clinic Booked Slot with Host: {host_name} and Attendee: {user_name}")

    event_result = service.events().patch(
        calendarId='primary',
        eventId=event_id,
        body={
        "summary": summary,
        "description": description,
        "attendees": [{"email": host_email},{"email": user_email}],
        "attendees": [{"responseStatus" : "accepted", "email": host_email},
                        {"responseStatus" : "accepted", "email": user_email}],
        },sendUpdates='all'
    ).execute()

    print("updated event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("attendee: ", event_result['attendees'][0]['email'])
    print("attendee: ", event_result['attendees'][1]['email'])



if __name__ == '__main__':
    user_email = "abecker@student.wethinkcode.co.za"
    user_name = user_email.split('@')[0]
    event_id = input("Please enter event ID: ")
    book_event(event_id, user_email, user_name)

    # ,sendUpdates='all'