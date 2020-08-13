import csv
import math
import codecs
import ast

def knn():

    knn_list=[]
    Sorted_List=[]
    test_data=[0,1596978714-3117,'https://jobee.pk/accounting-taxation-jobs',"Accounts & Audit Trainee, Z2A ASSOCIATES",'https://jobee.pk/jobdetail/accounts-audit-trainee-f879be4717dfd26b','Accounting/Taxation Jobs',"Accounts, Finance &  Financial Services Jobs",2,"Lahore, Pakistan",'Full Time Jobs','No Preference',18,40,'Bachelors','BBA / B.Com / Equivalent','Entry Level',5000,10000,'Monthly','Fresh',"Jul 21, 2020","Oct 19, 2020",'Morning Shift',"[{'Skills':'Accounts Services'},{'Skills':'Task Management'},{'Skills':'Auditing'}]",'Z2A ASSOCIATES','Lahore','Entry-Level']
    #test_data=[770,'tt0031381','Gone with the Wind',1939,"[{'id': 18, 'name': 'Drama'}, {'id': 10749, 'name': 'Romance'}, {'id': 10752, 'name': 'War'}]","[{'name': 'Selznick International Pictures', 'id': 1553}, {'name': 'Metro-Goldwyn-Mayer (MGM)', 'id': 8411}]",7.618957752254195,"An American classic in which a manipulative woman and a roguish man carry on a turbulent love affair in the American south during the Civil War and Reconstruction.",1939-12-15,'/4o1yeosjSFMaI9pe1rOkYcZ6hHO.jpg',0.4452054794520548]
    #test_data=[389,'tt0050083','12 Angry Men',1957,"[{'id': 18, 'name': 'Drama'}]","[{'name': 'United Artists', 'id': 60}, {'name': 'Orion-Nova Productions', 'id': 10212}]",8.153591909848416,"The defense and the prosecution have rested and the jury is filing into the jury room to decide if a young Spanish-American is guilty or innocent of murdering his father. What begins as an open and shut case soon becomes a mini-drama of each of the jurors' prejudices and preconceptions about the trial, the accused, and each other.",1957-0-25,'/3W0v956XxSG5xgm7LB6qu8ExYJ2.jpg',0.5684931506849316]
    #test_data=[9603,'tt0112697','Clueless',1995,"[{'id': 35, 'name': 'Comedy'}, {'id': 18, 'name': 'Drama'}, {'id': 10749, 'name': 'Romance'}]","[{'name': 'Paramount Pictures', 'id': 4}]",6.834793145795854,"Shallow, rich and socially successful Cher is at the top of her Beverly Hills high school's pecking scale. Seeing herself as a matchmaker, Cher first coaxes two teachers into dating each other. Emboldened by her success, she decides to give hopelessly klutzy new student Tai a makeover. When Tai becomes more popular than she is, Cher realizes that her disapproving ex-stepbrother was right about how misguided she was -- and falls for him.",1995-0-19,'/i8gEHh2sszB6YWLC0jl559sxAeN.jpg',0.8287671232876712]

    #test_data=[862,'tt0114709','Toy Story',1995,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]","[{'name': 'Pixar Animation Studios', 'id': 3}]",7.684683758682903,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",1995-10-30,'/rhIRbceoE9lR4veEXuwCC2wARtG.jpg',0.8287671232876712]
    #test_data=[8844,'tt0113497','Jumanji',1995,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]","[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]",6.877012452950091,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",1995-12-15,'/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg']
    #xmax=2019
    #test_data=[24428,'tt0848228','The Avengers',2012,"[{'id': 878, 'name': 'Science Fiction'}, {'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}]","[{'name': 'Paramount Pictures', 'id': 4}, {'name': 'Marvel Studios', 'id': 420}]",7.393911631476678,"When an unexpected enemy emerges and threatens global safety and security, Nick Fury, director of the international peacekeeping agency known as S.H.I.E.L.D., finds himself in need of a team to pull the world back from the brink of disaster. Spanning the globe, a daring recruitment effort begins!",2012-0-25,'/cezWGskPY5x7GaglTTRN4Fugfb8.jpg',0.9452054794520548]

    #xmin=1900
    #test_data=[414,'tt0112462','Batman Forever',1995,"[{'id': 28, 'name': 'Action'}, {'id': 80, 'name': 'Crime'}, {'id': 14, 'name': 'Fantasy'}]","[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Polygram Filmed Entertainment', 'id': 31080}]",5.200976013313185,"The Dark Knight of Gotham City confronts a dastardly duo: Two-Face and the Riddler. Formerly District Attorney Harvey Dent, Two-Face believes Batman caused the courtroom accident which left him disfigured on one side. And Edward Nygma, computer-genius and former employee of millionaire Bruce Wayne, is out to get the philanthropist; as The Riddler. Former circus acrobat Dick Grayson, his family killed by Two-Face, becomes Wayne's ward and Batman's new partner Robin.",1995-0-16,'/eTMrHEhlFPHNxpqGwpGGTdAa0xV.jpg',0.8287671232876712]

    #scaled_Test=(test_data[4]-xmin)/(xmax-xmin)
    p=0
    eucledian_dist=0
    Skills_Tlist=[]
    skills_Test=ast.literal_eval(test_data[23])
    for skill in skills_Test:
        Skills_Tlist.append(skill['Skills'])
    print(Skills_Tlist)
    types_of_encoding=["utf8"]
    for encoding_type in types_of_encoding:
        with codecs.open('exported.csv',encoding=encoding_type,errors='replace') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if(row[0]!=test_data[0]):
                    Skills_Dlist=[]
                    eucledian_dist=0
                    Skills_Data=ast.literal_eval(row[23])
                    for skill in Skills_Data:
                        Skills_Dlist.append(skill['Skills'])
                    for j in (Skills_Tlist): 
                        if j not in Skills_Dlist:
                            #if len(Skills_Tlist)>4
                            eucledian_dist+=0.6
                    for l in (Skills_Dlist): 
                        if l not in Skills_Tlist:
                            eucledian_dist+=0.1
                    if (row[5]!=test_data[5]):
                        eucledian_dist+=0.2
                    if (row[6]!=test_data[6]):
                        eucledian_dist+=1
                    if (row[7]!=test_data[7]):
                        eucledian_dist+=0.4
                    if (row[8]!=test_data[8]):
                        eucledian_dist+=0.7
                    if (row[9]!=test_data[9]):
                        eucledian_dist+=0.7
                    if (row[10]!=test_data[10]):
                        eucledian_dist+=0.7
                    if (row[11]!=test_data[11]):
                        eucledian_dist+=0.3
                    if (row[12]!=test_data[12]):
                        eucledian_dist+=0.3
                    if (row[13]!=test_data[13]):
                        eucledian_dist+=0.7
                    if (row[16]!=test_data[16]):
                        eucledian_dist+=0.3
                    if (row[17]!=test_data[17]):
                        eucledian_dist+=0.8
                    if (row[18]!=test_data[18]):
                        eucledian_dist+=0.4
                    if (row[22]!=test_data[22]):
                        eucledian_dist+=0.6
                    if (row[24]!=test_data[24]):
                        eucledian_dist+=0.6
                    if (row[26]!=test_data[26]):
                        eucledian_dist+=0.8
                    eucledian_dist=math.sqrt(eucledian_dist)
                    knn_list.append([eucledian_dist,row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[16],row[17],row[18],row[19],row[20],row[21],row[22],Skills_Dlist,row[24],row[25],row[26]])
        knn_list.sort()
        #print(knn_list)
    for x in range(5):
        
        print("\nEuclidean distance: ")
        print(knn_list[x][0])
        print("\nJob Name: ")
        print(knn_list[x][1])
        print("\nIndustry: ")
        print(knn_list[x][3])
        print("\nFunctional Area: ")
        print(knn_list[x][4])
        print("\nTotal Positions: ")
        print(knn_list[x][5])
        print("\nJob Location: ")
        print(knn_list[x][6])
        print("\nJob Type: ")
        print(knn_list[x][7])
        print("\nGender: ")
        print(knn_list[x][8])
        print("\nMin Age: ")
        print(knn_list[x][9])
        print("\nMax Age: ")
        print(knn_list[x][10])
        print("\nEducation: ")
        print(knn_list[x][11])
        print("\nMin Salary: ")
        print(knn_list[x][12])
        print("\nMax Salary: ")
        print(knn_list[x][13])
        print("\nSalary Type: ")
        print(knn_list[x][15])
        print("\nPosted date: ")
        print(knn_list[x][16])
        print("\nApply by Date: ")
        print(knn_list[x][17])
        print("\nJob Shift: ")
        print(knn_list[x][18])
        print("\nSkills: ")
        print(knn_list[x][19])
        print("\nCompany Name: ")
        print(knn_list[x][20])
        print("\nCompany City: ")
        print(knn_list[x][21])
        print("\nExperience Level: ")
        print(knn_list[x][22])
        print("\nJob Link: ")
        print(knn_list[x][2])

        print("\n\n\n")

        #Sorted_List.append(knn_list[x])"""







                    

knn()
def main():
    knn

main()