import json, requests

apiKey= "367dde354e65a936886c62cd5e38d1fe"

baseURL = "https://api.openweathermap.org/data/2.5/weather"



print ('Hello, welcome to "Weather 4 U"')
City=''

again = 'yes'

while again == 'yes':
  print('please enter your city now:')
  City= input()
  URL= f"{baseURL}?q={City}&units=imperial&APPID={apiKey}"
  response=requests.get(URL)
  unformatedData=response.json()
  if response.status_code==200:
    current = unformatedData['main']['temp']
    max=unformatedData['main']['temp_max']
    print ('Your current temperature is: ',current)
    print ('The max tepmerature is: ',max)
    print()
    print('would you like to search for another city? (yes or no)')
    again= input()
  else:
    print ('that is an invalid city, please try again.')
    
print ("Have a nice day.")