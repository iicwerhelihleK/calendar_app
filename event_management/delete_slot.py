# import initialise.cal_setup.get_calendar_service as get_calendar_service
from cal_setup import get_calendar_service

def delete_event(event_id):
    # Delete the event
    service = get_calendar_service()
    
    try:
        service.events().delete(
            calendarId='primary',
            eventId=event_id,
        ).execute()
    except googleapiclient.errors.HttpError:
        print("Failed to delete event")

    print("Event deleted")

if __name__ == '__main__':
    event_id = input("Please enter event ID: ")
    delete_event(event_id)