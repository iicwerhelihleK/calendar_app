from datetime import datetime, timedelta
from cal_setup import get_calendar_service


def host_event(user_email, user):

    service = get_calendar_service()

    summary = (f"{user}_open_slot")
    description = (f"Code Clinic Open Slot with Host: {user}")
    date = input("date (yyyy-mm-dd): ")
    start_time = input("start time (hh:mm): ")

    # convert string to datetime format
    datetime_object = datetime.strptime(start_time, '%H:%M')
    # add 90min
    end_object = datetime_object + timedelta(minutes=90)
    # remove date so it's just time
    end_time = end_object.time().strftime("%H:%M")

    event_result = service.events().insert(calendarId='primary',
        body={
            "summary": summary,
            "description": description,
            "start": {"dateTime": f"{date}T{start_time}:00+02:00"},
            "end": {"dateTime": f"{date}T{end_time}:00+02:00"},
            "attendees": [{"email": user_email}],
            # "hangoutLink" : "link",
        }, maxAttendees = 2
    ).execute()

    print("Event Booking Time Created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])
    print("attendee: ", event_result['attendees'][0])
    # print("hangout link: ", event_result['hangoutLink'])


if __name__ == '__main__':
    user_email = 'ejohns@student.wethinkcode.co.za'
    host_event(user_email)
