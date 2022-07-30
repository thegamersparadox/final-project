import json, requests

apiKey= "367dde354e65a936886c62cd5e38d1fe"

baseURL = "https://api.openweathermap.org/data/2.5/weather"



print ('Hello, welcome to "Weather 4 U", please input your city now.')
City = input()





URL= f"{baseURL}?q={City}&units=imperial&APPID={apiKey}"
print (URL)

response=requests.get(URL)
unformatedData=response.json()

again = 'yes'

while again == 'yes':
  print (unformatedData)
  current = unformatedData['main']['temp']
  max=unformatedData['main']['temp_max']
  print ('Your current temperature is: ',current)
  print ('The max tepmerature is: ',max)
else:
  print ("Have a nce day.")