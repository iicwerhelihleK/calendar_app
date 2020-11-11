from abc import ABCMeta
from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def main():
    # update the event to tomorrow 9 AM IST
    service = get_calendar_service()

    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 9)+timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=2)).isoformat()

    event_result = service.events().update(
        calendarId='primary',
        eventId='<place your event ID here>',
        body={
        "summary": 'Updated Automating calendar',
        "description": 'This is a tutorial example of automating google calendar with python, updated time.',
        "start": {"dateTime": start, "timeZone": 'Africa/Johannesburg'},
        "end": {"dateTime": end, "timeZone": 'Africa/Johannesburg'},
        },
    ).execute()

    print("updated event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])


    


# def main():
#     # First retrieve the event from the API.
#     event = service.events().get(calendarId='primary', eventId='eventId').execute()

#     event['summary'] = 'Appointment at Somewhere'

#     updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()

#     # Print the updated date.
#     print (updated_event['updated'])


if __name__ == '__main__':
    main()