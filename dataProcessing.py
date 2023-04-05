import pandas as pd

def convertToInt(val):
    if val=='>90':
        return 90
    elif val=='<10':
        return 10
    else:
        return int(val)

#Hollis-brookline in twice since name changed to add dash
schools = [ "Amherst Middle School", "Boynton Middle School", "Elm Street Middle School", "Fairgrounds Middle School", "Great Brook School",
"Henry J. McLaughlin Middle School", "Hillsboro-Deering Middle School", "Hillside Middle School",
            "Hollis Brookline Middle School" , "Hollis-Brookline Middle School",
"Hudson Memorial School" ,"Litchfield Middle School","Merrimack Middle School","Middle School At Parkside",
"Milford Middle School", "Mountain View Middle School", "Pelham Memorial School", "Pennichuck Middle School"
,"Ross A. Lurgio Middle School", "South Meadow School", "Southside Middle School","Weare Middle School",
"Wilton-Lyndeboro Middle School"]
subjects = ['sci']
dfTotal = pd.DataFrame()
for i in range(9,20):
    df = pd.read_csv('assessment'+str(i)+'.csv')
    df = df.drop(df[(df.grade != 8)].index)
    #asd_students = df[df['schname']=='Academy for Science and Design Charter (M)'][['NumberStudents','subject']]
    asd_students = pd.read_csv('asdYearlyEnrollment.csv')
    asd_students = asd_students[asd_students['Year']==i]['enrollment']

    #print(asd_students.iloc[0])
    #df = df[df['subject']=='mat']
    df = df[['schname', 'pAboveprof']]

    #df = df[['schname', 'subject', 'grade', 'pAboveprof', 'pBelowProf']]
    df = df[df.schname.isin(schools)]
    df['pAboveprof'] = df['pAboveprof'].apply(lambda x: convertToInt(x))
    df2 = df.groupby(by=["schname"])['pAboveprof'].mean()
    df2 = df2
    df2.to_csv('overall/'+str(i)+'.csv')
    df2 = pd.read_csv(str(i)+'.csv')
    #df2.insert(2, 'asd_enrollment', int(asd_students))
    #df2.to_csv('science/'+str(i)+'sci.csv')
    print(df2)
    #df2['pAboveprof'].to_csv(str(i)+'.csv')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
