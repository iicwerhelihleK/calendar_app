from cal_setup import get_calendar_service

def main():
   service = get_calendar_service()
   # Call the Calendar API
   print('Getting list of calendars')
   calendars_result = service.calendarList().list().execute()

   calendars = calendars_result.get('items', [])

   if not calendars:
       print('No calendars found.')
   for calendar in calendars:
       summary = calendar['summary']
       id = calendar['id']
       primary = "Primary" if calendar.get('primary') else ""
       print("%s\t%s\t%s" % (summary, id, primary))





#  if err.resp.get('content-type', '').startswith('application/json'):
#     reason = json.loads(err.content).get('error').get('errors')[0].get('reason')



#  from googleapiclient.errors import HttpError
#  try:
#     ...
#  except HttpError as err:
#    # If the error is a rate limit or connection error,
#    # wait and try again.
#    if err.resp.status in [403, 500, 503]:
#      time.sleep(5)
#    else: raise
if __name__ == '__main__':
   main()