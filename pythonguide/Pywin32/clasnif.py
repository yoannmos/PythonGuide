import datetime
import win32com.client


def getCalendarEntries(days=1):
    """
    Returns calender entries for days default is 1
    """
    Outlook = win32com.client.Dispatch("Outlook.Application")
    ns = Outlook.GetNamespace("MAPI")
    appointments = ns.GetDefaultFolder(
        9
    ).Items  # "9" refers to the index of a folder - in this case,
    # the events/appointments. You can change that number to reference
    # any other folder

    # Returning only today appointment
    appointments.Sort("[Start]")
    appointments.IncludeRecurrences = "True"
    today = datetime.datetime.today()
    begin = today.date().strftime("%d/%m/%Y")
    tomorrow = datetime.timedelta(days=days) + today
    end = tomorrow.date().strftime("%d/%m/%Y")
    appointments = appointments.Restrict(
        "[Start] >= '" + begin + "' AND [END] <= '" + end + "'"
    )

    # events={'Start':[],'Subject':[],'Duration':[]}
    for a in appointments:
        print("Subject = ", a.Subject)
        print("BusyStatue = ", a.BusyStatus)
        print("Location = ", a.Location)
        print("AllDayEvent = ", a.AllDayEvent)
        print("Start = ", a.Start)
        print("End   = ", a.End)
        print("")
        # adate=datetime.datetime.fromtimestamp()
        # adate=datetime.datetime.fromtimestamp(int(a.Start))
        # print (a.Start, a.Subject,a.Duration)
        # events['Start'].append(a.date)
        # events['Start'].append(a.Start)
        # events['Subject'].append(a.Subject)
        # events['Duration'].append(a.Duration)
    return  # events


getCalendarEntries(days=1)
