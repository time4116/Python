from okta import AppInstanceClient

site = 'Your Site'
skey = 'Your Key'

appInstance = AppInstanceClient(site, skey)
apps = appInstance.get_paged_app_instances()

OktaAppList = open('C:\\temp\\ApplicationList.csv', 'w+')
OktaAppList.write("Name,SSO Mode,ID,Created")

while True:
       
    for i in apps.result:
        
        if i.status == 'ACTIVE':

            #print(i.label, i.signOnMode, i.id, i.created)
            
            OktaAppList.write('\n')
            OktaAppList.write(str(i.label)+','+str(i.signOnMode)+','+str(i.id)+','+str(i.created))

    if not apps.is_last_page():
        # Keep on fetching pages of applications until the last page
        apps = appInstance.get_paged_app_instances(url=apps.next_url)
        
    else:
        break

OktaAppList.close()
