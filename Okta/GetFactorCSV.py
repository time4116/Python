import time
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
EnrolledUsers.write("Username,FactorType,UserID,DateEnrolled,TimeEnrolled") # Set CSV Headers

for user in lst:
    lifecycle = factorClient.get_lifecycle_factors(user_id=user.id)
   
    for life in lifecycle:
        if life.factorType == 'Factor Name Here': # Select factor type here
            EnrolledUsers.write('\n')
            
            time = str(life.created)
            timecreated = time.split()[1]
            datecreated = time.split()[0]

            EnrolledUsers.write(user.profile.login+','+life.factorType+','+life.id+','+datecreated+','+timecreated)
EnrolledUsers.close()
