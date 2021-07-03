MathTeam = {
    'schedule' :'wednesday',
    'interest' :'math',
    'available' : False,
    'interested' : False,
    'name' : 'Math Team'
}

ScienceOlympiad = {
    'schedule' : 'friday',
    'interest' : 'science',
    'available' : False,
    'interested' : False,
    'name':'Science Olympiad'
}

GirlsWhoCode = {
    'schedule' : 'tuesday',
    'interest' : 'compsci',
    'available' : False,
    'interested' : False,
    'name':'GirlsWhoCode'
}

TechHacks = {
    'schedule':'thursday',
    'interest':'compsci',
    'available':False,
    'interested':False,
    'name':'TechHacks'
}

Embroidery = {
    'schedule' : 'thursday',
    'interest' : 'art',
    'available' : False,
    'interested' : False,
    'name':'Embroidery'
}

Robotics = {
    'schedule' : 'monday',
    'interest' : 'compsci',
    'available' : False,
    'interested' : False,
    'name':'Robotics'
}

ModelUN = {
    'schedule':'monday',
    'interest':'humanities',
    'available':False,
    'interested':False,
    'name':'Model United Nations'
}

NationalHonorSociety = {
    'schedule':'wednesday',
    'interest':'service',
    'available':False,
    'interested':False,
    'name':'National Honor Society'
}

MuralPainting = {
    'schedule' : 'friday',
    'interest' : 'art',
    'available' : False,
    'interested' : False,
    'name':'Mural Painting'
}

HOPE = {
    'schedule':'thursday',
    'interest':'service',
    'available':False,
    'interested':False,
    'name':'H.O.P.E.'
}

Architecture = {
    'schedule':'tuesday',
    'interest':'art',
    'available':False,
    'interested':False,
    'name':'Architecture'
}

Astronomy = {
    'schedule':'wednesday',
    'interest':'science',
    'available':False,
    'interested':False,
    'name':'Astronomy'
}

PreMedSociety = {
    'schedule':'thursday',
    'interest':'science',
    'available':False,
    'interested':False,
    'name':'Pre-Med Society'
}

BETA = {
    'schedule':'monday',
    'interest':'service',
    'available':False,
    'interested':False,
    'name':'BETA'
}

AllECs = [MathTeam,ScienceOlympiad,GirlsWhoCode,Embroidery,Robotics, ModelUN, NationalHonorSociety, MuralPainting, HOPE, Architecture, PreMedSociety, Astronomy, BETA]

ECsSchedule =[]
def AskSchedule():
    print("First let's see what your schedule is")
    print('Type y for yes, n for no')
    if input('Are you free on Monday?')== 'y':
        ECsSchedule.append('monday')
    if input('Are you free on Tuesday?') == 'y':
        ECsSchedule.append('tuesday')
    if input('Are you free on Wednesday?') == 'y':
        ECsSchedule.append('wednesday')
    if input('Are you free on Thursday?') == 'y':
        ECsSchedule.append('thursday')
    if input('Are you free on Friday?') == 'y':
        ECsSchedule.append('friday')
    for EC in AllECs:
        for day in ECsSchedule:
            if EC['schedule'] == day:
                EC['available'] = True

ECsInterests = []
def AskInterests():
    print("Now let's see what you are interested in")
    print('Type y for yes, n for no')
    if input('Are you interested in Humanities?') == 'y':
        ECsInterests.append('humanities')
    if input('Are you interested in Math?') == 'y':
        ECsInterests.append('math')
    if input('Are you interested in Science?') == 'y':
        ECsInterests.append('science')
    if input('Are you interested in Computer science?') == 'y':
        ECsInterests.append('compsci')
    if input('Are you interested in Art?') == 'y':
        ECsInterests.append('art')
    if input('Are you interested in Community service and volunteering?') == 'y':
        ECsInterests.append('service')
    for EC in AllECs:
        for subject in ECsInterests:
            if EC['interest'] == subject:
                EC['interested'] = True

FinalECList = []
def FindECs():
    print("Let's find some extracurriculars for you.")
    AskSchedule()
    AskInterests()
    for EC in AllECs:
        if ((EC['available']==True) and (EC['interested']==True)):
            FinalECList.append(EC['name'])
    numberECs = 0
    for EC in FinalECList:
        numberECs +=1
    if (numberECs == 0):
        print('Sorry, nothing fit both your interests and schedule. Maybe try some new subjects or free up some time?')
    else:
        print('We found ' + str(numberECs) + ' extracurriculars that fit your interests and schedule! Here they are. Check the school website for more info.')
        print(FinalECList)
    MainFunction()

def ECInfo():
    search = input('Search for information about an extracurricular: ')
    for EC in AllECs:
        if EC['name']== search:
            print('This extracurricular meets on', EC['schedule'], '. It is recommended for people interested in' , EC['interest'],'.')
    continueornot = input('Would you like to search for information about another extracurricular? (type y or n)')
    if continueornot == 'y':
        ECInfo()
    else:
        MainFunction()

def MainFunction():
    userchoice = input('1 - Find extracurriculars based on interests and schedule\n2 - View information about each extracurricular\n')
    if userchoice == '1':
        FindECs()
    if userchoice == '2':
        ECInfo()

MainFunction()