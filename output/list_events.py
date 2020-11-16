import datetime
from cal_setup import get_calendar_service

def list_events():
   service = get_calendar_service()
   # Call the Calendar API
   now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
   print('Getting List o 10 events\n')
   events_result = service.events().list(
       calendarId='primary', timeMin = now,
       maxResults=10, singleEvents=True,
       orderBy='startTime').execute()
   events = events_result.get('items', [])

   if not events:
       print('No upcoming events found.')
   for event in events:
       start = event['start'].get('dateTime', event['start'])
       end = event['end'].get('dateTime')
    #    start = event['start'].get('dateTime')
    #    print(start, event['summary'])
       print(f"Event Name: {event['summary']}   Event ID: {event['id']}")
       print(f"Event Start: {event['start'].get('dateTime')}   Event End: {event['end'].get('dateTime')}\n")

if __name__ == '__main__':
   list_events()