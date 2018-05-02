import meetup.api
client = meetup.api.Client('186444642f3e8592d3a7f117a31514')
#group_info = client.GetGroup({'urlname': 'Meetup-API-Testing'})
#print(group_info.name)

client.GetDashboard()

