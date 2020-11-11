## Script to delete events from google calendar
from googleapiclient.discovery import build
from cal_setup import get_calendar_service
from googleapiclient.errors import HttpError



def main():
    # if err.resp.get('content-type', '').startswith('application/json'):
    #     reason = json.loads(err.content).get('error').get('errors')[0].get('reason')


    # from googleapiclient.errors import HttpError
    # try:
    #     ...
    # except HttpError as err:
    # # If the error is a rate limit or connection error,
    # # wait and try again.
    #     if err.resp.status in [403, 500, 503]:
    #         time.sleep(5)
    #     else: raise

    
    # Delete the event
    service = get_calendar_service()
    try:
        service.events().delete(
            calendarId='primary',
            eventId='<place your event ID here>',
        ).execute()
    except HttpError:
        print("Failed to delete event")

    print("Event deleted")

if __name__ == '__main__':
    main()