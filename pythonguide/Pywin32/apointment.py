import sys
import datetime
import logging

import win32com.client

# log = logging.getLogger(__name__)
# log.setLevel(logging.DEBUG)
# log_formatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s] %(message)s")
# log_consolehandler = logging.StreamHandler()
# log_consolehandler.setFormatter(log_formatter)
# log.addHandler(log_consolehandler)
# logfname = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
# log_filehandler = logging.FileHandler('cal-%s.txt' % logfname, mode='a', encoding='utf-8')
# log_filehandler.setFormatter(log_formatter)
# log.addHandler(log_filehandler)

# Then declare the my_date variable as datetime.date.

start_date = datetime.datetime.today()

list_Email_Mechanic = ["youremail@email.com"]

# def print_folders(folders, indent=0):
#     prefix = ' ' * (indent*2)
#     i = 0
#     for folder in folders:
#         log.info("{0}{1}. {2} ({3})".format(prefix, i, folder.Name, folder.DefaultItemType))
#         print_folders(folder.Folders, indent + 1)
#         i += 1


def getCalendarEntries(days=1):
    """
    Return calendar entries for days default is 1
    """
    Outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = Outlook.GetNamespace("MAPI")

    appointments = namespace.GetDefaultFolder(9).Items
    # "9" refers to the index of a folder - in this case,
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

    events = {"Start": [], "Subject": [], "Duration": []}
    for a in appointments:
        # print("Subject = ",a.Subject)
        # print("BusyStatue = ",a.BusyStatus)
        # print("Location = ",a.Location)
        # print("AllDayEvent = ",a.AllDayEvent)
        # print("Start = ",a.Start)
        # print("End   = ",a.End)
        # print("")
        # adate=datetime.datetime.today()
        # adate=datetime.datetime.fromtimestamp(int(a.Start))
        print(a.Start, a.Subject, a.Duration)
        # events['Start'].append(a.date)
        events["Start"].append(a.Start)
        events["Subject"].append(a.Subject)
        events["Duration"].append(a.Duration)
    return events


getCalendarEntries()

