from datetime import datetime
from okta import UsersClient
from okta import FactorsAdminClient
from okta import FactorsClient

# Get a users ID
usersClient = UsersClient("Your Site", "Your Token")

usersClient.get_user('Login Name').id
# Or this:
# 	usr = usersClient.get_user('Login Name').id
# 	usr.id

# Get a users factor, ID and time enrolled
userClients = FactorsClient("Your Site", "Your Token")

userClients = uclient.get_lifecycle_factors(user_id="User ID")
for client in userClients:
    print(client.factorType, client.id, client.created)

# Get the org's list of active factors
factorClient = FactorsAdminClient("Your Site", "Your Token")

clients = factorClient.get_org_factors()
for client in clients:
    if client.status != 'NOT_SETUP' and client.status != 'INACTIVE':
        print(client.factorType, client.id, client.status)

# Get all users enrollment date for a specific factor
site = 'Your Site'
skey = 'Your Key'

usersClient = UsersClient(site, skey)
factorClient = FactorsClient(site, skey)

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

date = '2017-10-01'
date = datetime.strptime(date, "%Y-%m-%d")

for user in lst:
    lifecycle = factorClient.get_lifecycle_factors(user_id=user.id)
    
    for life in lifecycle:
        createdtime = str(life.created)
        timesplit = createdtime.split(' ')[0]  # Select just the year, month and day.
        enrolledtime = datetime.strptime(timesplit, "%Y-%m-%d")
		
        if enrolledtime >= date and life.factorType == 'Factor Name Here': # Make sure to enter the desired factor here
            print(user.profile.login, life.factorType, life.id, life.created)
