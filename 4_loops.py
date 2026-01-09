#list -> how we store data in python, we use list for storing multiple values of multiple types
#array -> data sturecture which can hold multiple values of same type
list_of_cloud = ["aws" , "azure" , "gcp" , "digital ocean" , "utho" , "alibaba" , "oracle"]
cloud = "gcp" #variable

print(list_of_cloud)


#add a new cloud  salesforce

list_of_cloud.append("salesforce") #add to the end of list

#add a new cloud IBM
list_of_cloud.append("IBM")

print(list_of_cloud)

#add a item to list after 2nd position

list_of_cloud.insert(2, "Heroku")

print(list_of_cloud)

#find the length of list
print(len(list_of_cloud))

#insert "Hello cloud " to 0th index of list 

list_of_cloud.insert(0 , "Hello cloud")

print(list_of_cloud)

#if you want to iterate the item use for
#iteration of list

for cloud in list_of_cloud:
    print(" ")
    print(cloud)

for i in range(0,10): #it goes from i to 10-i, means 0 to 9
    print(i)









