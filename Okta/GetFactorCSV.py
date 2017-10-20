from okta import UsersClient
from okta import FactorsClient

site = 'Your Site'
skey = 'Your Key'

usersClient = UsersClient(site, skey)
factorClient = FactorsClient(site, skey)

currentDate = time.strftime('%Y%m%d')

lst = []
users = usersClient.get_paged_users()
while True:
    for user in users.result:
        if user.status == 'ACTIVE': # Get only active users
            lst.append(user)
            
    if not users.is_last_page():
        # Keep on fetching pages of users until the last page
        users = usersClient.get_paged_users(url=users.next_url)
    else:
        break

EnrolledUsers = open('C:\\temp\\EnrolledUsers'+currentDate+'.csv', 'w+')
EnrolledUsers.write("Username,FactorType,UserID,DateEnrolled,TimeEnrolled")

for user in lst:
    lifecycle = factorClient.get_lifecycle_factors(user_id=user.id)
   
    for life in lifecycle:
        if life.factorType == 'sms': # Select factor type here
            EnrolledUsers.write('\n')
             time = str(i.created)
            timecreated = time1.split()[1]
            datecreated = time1.split()[0]

            EnrolledUsers.write(user.profile.login+','+i.factorType+','+i.id+','+datecreated+','+timecreated)
EnrolledUsers.close()
