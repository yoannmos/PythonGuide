import win32com.client


# Outlook = win32com.client.Dispatch("Outlook.Application")
# ns = Outlook.GetNamespace("MAPI")
def folderTree(folders, indent = 0):
    """Displays all available folders in a tree structure.
    Keyword arguments:
    folders    --  The current Folders iterator
    indent     --  The current indent level
    """
    prefix = ' ' * (indent*2)
    i = 0
    for folder in folders:
        print("{0}{1}. {2} ({3})".format(prefix, i, folder.Name, folder.DefaultItemType))
        folderTree(folder.Folders, indent + 1)
        i = i + 1


Outlook = win32com.client.Dispatch("Outlook.Application")
print("Outlook version: {}".format(Outlook.Version))
print("Default profile name: {}".format(Outlook.DefaultProfileName))

# get the Namespace / Session object
# namespace = Outlook.GetNamespace("MAPI") 
namespace = Outlook.Session         # identical to GetNameSpace("MAPI") (starting with Outlook 98)
print("Current profile name: {}".format(namespace.CurrentProfileName))

##### Show tree of all available folders
print("\nFolders")
print("-------")
folderTree(namespace.Folders)

##### get own calendar and print all entries in the next 30 days
print("\nMy calendar")
print("---------------")
myCalendar = namespace.GetDefaultFolder(9)
# printCalendar(myCalendar)
