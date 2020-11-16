from datetime import datetime, timedelta
from cal_setup import get_calendar_service
from output.list_events import list_events
from event_management.book_slot import book_event
from event_management.delete_slot import delete_event
from event_management.host_slot import host_event
from user_input import get_user


# def main():
#    # creates one hour event tomorrow 10 AM IST
#    service = get_calendar_service()

#    d = datetime.now().date()
#    tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
#    start = tomorrow.isoformat()
#    end = (tomorrow + timedelta(hours=1)).isoformat()

#    event_result = service.events().insert(calendarId='primary',
#        body={
#            "summary": 'Automating calendar',
#            "description": 'This is a tutorial example of automating google calendar with python',
#            "start": {"dateTime": start, "timeZone": 'Africa/Johannesburg'},
#            "end": {"dateTime": end, "timeZone": 'Africa/Johannesburg'},
#        }
#    ).execute()

#    print("created event")
#    print("id: ", event_result['id'])
#    print("summary: ", event_result['summary'])
#    print("starts at: ", event_result['start']['dateTime'])
#    print("ends at: ", event_result['end']['dateTime'])



def attend(email, user):
    list_events()
    event_id = input("Please enter event ID: ")
    book_event(event_id, email, user)
    
def delete(email, user):
    list_events()
    event_id = input("Please enter event ID: ")
    # delete_event(event_id, email, user)
    delete_event(event_id)

def host(email, user):
    host_event(email,user)

def host_or_attend(email, user):
    choice = input("Do you want to 'host','attend' or 'delete' a clinic? : ")
    if choice.lower() == "attend":
        attend(email,user)
    elif choice.lower() == "host":
        host(email, user)
    elif choice.lower() == "delete":
        delete(email,user)

def run_booking_system():
    email,user = get_user.get_email()
    host_or_attend(email, user)




if __name__ == '__main__':
    # main()
    run_booking_system()