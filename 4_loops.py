#list -> how we store data in python, we use list for storing multiple values of multiple types
#array -> data sturecture which can hold multiple values of same type
list_of_cloud = ["aws" , "azure" , "gcp" , "digital ocean" , "utho" , "alibaba" , "oracle"]
cloud = "gcp" #variable

print(list_of_cloud)


#add a new cloud  salesforce

list_of_cloud.append("salesforce")

#add a new cloud IBM
list_of_cloud.append("IBM")

print(list_of_cloud)

#add a item to list after 2nd position

list_of_cloud.insert(2, "Heroku")

print(list_of_cloud)







