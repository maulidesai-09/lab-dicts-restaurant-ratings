"""Restaurant rating lister."""


#create a function
#access the file using the open and read commands
#split the data into a list that we can iterate 
#create an empty dictionary 
#loop through each line in the file and add the key values to the dict
    #key --> restaurant name [0]
    #value --> rating [1]
#print using the .items() so that we can create a tuple with the key/values
#sort the dictionary kkeys with the sorted() function

def read_ratings(file):

    ratings_dict = {}

    data = open(file)
    
    for line in data:
        rest_rating = line.rstrip().split(":")
        dict_key = rest_rating[0]
        dict_value = rest_rating[1]
        ratings_dict[dict_key] = dict_value

    while True: 
    
        for dict_key, dict_value in sorted(ratings_dict.items()):
            print(f"{dict_key} is rated at {dict_value}.")
        
        print("")

        while True:

            want_to_add = input("Would you like to add a rating? (y/n): ")
            print("")
            want_to_add = want_to_add.lower()

            if want_to_add != "y" and want_to_add != "n":
                print("Please enter 'y or 'n': ")
            
            else:
                break


        if want_to_add == "n":
            print("Thank you! Have a great day.")
            break

        elif want_to_add == "y":
            new_restaurant = input("What's the name of the restaurant would you like to rate?: ")
            new_rating = int(input("Please enter the rating: "))
            print("")
            ratings_dict[new_restaurant] = new_rating
            




            # if want_to_add == "y" or want_to_add == "n":

            #     if want_to_add == "y":
            #         new_restaurant = input("What's the name of the restaurant would you like to rate?: ")
            #         new_rating = int(input("Please enter the rating: "))
            #         print("")
            #         ratings_dict[new_restaurant] = new_rating
            #         break

            #     elif want_to_add == "n":
            #         print("Thank you! Have a great day.")
            #         break
            
            # else:
            #     print("Please enter 'y or 'n': ")
                
                
                
            
            
            
        
        # if want_to_add == "n":
        #     break


#create another new function add_ratings that includes a parameter of the dictionary ratings_dict
#get user input for restaurant name
#get user input for score --> convert to int 
#add the user input key/value pair to the dict 


#########WHEN WE TRIED WITH MULTIPLE FUNCTIONS#####
# def add_ratings(dict):
#     new_restaurant = input("What restaurant would you like to rate?: ")
#     new_rating = int(input("Please enter the rating: "))
#     dict[new_restaurant] = new_rating


#create another function that calls both that includes a parameter of the file 

# def run_ratings(file):
    
#     read_ratings(file)
    
#     while True: 

#         want_to_add = input("Would you like to add a rating? (y/n): ")
#         want_to_add = want_to_add.lower()

#         if want_to_add == "y":
#             add_ratings(ratings_dict)

#         # elif want_to_add != "y" or want_to_add != "n":
#         #     print("Please enter 'y or 'n': ")
#         else:
#             print("Thank you! Have a great day.")
#             break 


# run_ratings("scores.txt")
    


read_ratings("scores.txt")
    



