from okta import UsersClient
from okta import FactorsClient

usersClientdev = UsersClient(site, skey)

lst = []
users = usersClient.get_paged_users()
while True:
    for user in users.result:
        if user.status == 'ACTIVE':
            lst.append(user)
            #lst.append(user.profile.login)

    if not users.is_last_page():
        # Keep on fetching pages of users until the last page
        users = usersClient.get_paged_users(url=users.next_url)
    else:
        break

currentDate = time.strftime('%Y%m%d')
faccli = FactorsClient(site, skey)

EnrolledUsers = open('C:\\temp\\EnrolledUsers'+currentDate+'.csv', 'w+')
EnrolledUsers.write("Username,FactorType,UserID,DateEnrolled,TimeEnrolled")

for user in lst:
    cat = faccli.get_lifecycle_factors(user_id=user.id)
    # print("\n")
    # print(user.profile.login)
    for i in cat:
        #createdtime = str(i.created)
        #timesplit = createdtime.split(' ')[0]
        #total = datetime.strptime(timesplit, "%Y-%m-%d")

        if i.factorType == 'sms': # total >= date1 and
            EnrolledUsers.write('\n')
            # print(user.profile.login)
            time = str(i.created)
            timecreated = time1.split()[1]
            datecreated = time1.split()[0]

            EnrolledUsers.write(user.profile.login+','+i.factorType+','+i.id+','+datecreated+','+timecreated)
EnrolledUsers.close()
