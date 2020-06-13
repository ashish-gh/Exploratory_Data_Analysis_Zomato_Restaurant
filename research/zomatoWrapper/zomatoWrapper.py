import requests
import json,os,re,datetime
import ast
import csv



class Zomato:

    def __init__(self, user_key):
        """Define objects of type Zomato

        Parameters:
        api_key: API key to access https://developers.zomato.com/api/v2.1/

        """
        self.user_key = user_key
        self.base_url = "https://developers.zomato.com/api/v2.1/"
        self.path_to_folder="raw_data"
        self.path_to_processed_data= "processed_data"
        self.fileName = ""
        self.read_rest = []
        self.read_list = []
        self.rest_ID= []
        self.review_details = {}

        # global read_file


    def search(self, city_id, entity_type):
        """This api provides you with list
        of restaurant details in provided city.

        Parameters:
        city_id: ID of city 
        entity_type: 
        """  
        headers = {'user-key': self.user_key}
        response = requests.get(self.base_url + "search?entity_id="+ str(city_id) + "&entity_type=" + str(entity_type)+"&start=1&count=20", headers=headers)
        self.read_rest = json.loads(response.text)
        self.read_list.append(self.read_rest)
        # check if directory exists
        self.checkIfDirectoryExists()
        # check if file exists
        self.fileName = str(city_id)+'_'+str(entity_type)+'.json'
        self.checkIfRestaurantFileExists(self.fileName)

    

    def getReviews(self):
        """This api provides you with list
        of reviews for restaurant .
        """
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        # check if file exists

        self.fileName = 'restaurant_id.txt'
        self.checkIfFileExists(self.fileName)
        for rest_id in self.rest_ID[1900:2000]:
            response = (requests.get(self.base_url + "reviews?res_id="+str(rest_id), headers=headers).content).decode('utf-8')
            loaded_file = json.loads(response)        
            for i in loaded_file['user_reviews']:
                self.review_details.update({i['review']['review_text'] : rest_id})
            print("Restaurant review for : {}".format(rest_id))
        # save review
        self.saveReview()


    
    def checkIfFileExists(self, fileName):
        try:
            with open(os.path.join(self.path_to_processed_data,fileName), "r") as read_file:
                for i in read_file:
                    i = i.replace('\n', '')
                    self.rest_ID.append(i)
        except IOError:
            print("File not found")
            return
    


    def checkIfRestaurantFileExists(self, fileName):
        self.fileName = fileName
        if not os.path.isfile(self.fileName):
            try:
                path = os.path.join(self.path_to_folder,str(city_id)+'_'+str(entity_type)+'.json') 
                with open(path, 'w') as jsonfile:
                    json.dump(self.read_list, jsonfile)
                    print("File saved successfully. . .")
            except:
                print("File "+str(city_id)+'_'+str(entity_type)+'.json already exists')
        return self.read_list



    def checkIfDirectoryExists(self):
        if not os.path.isdir(self.path_to_folder):
            try:
                os.makedirs(self.path_to_folder)
            except FileExistsError:
                print("Directory " + self.path_to_folder + " already exist")


    def saveReview(self):
        path = os.path.join(self.path_to_folder,'reviews_restaurant_1900_2000.json') 
        with open(path, 'w') as jsonfile:
            json.dump(self.review_details, jsonfile)
            print("File saved successfully. . .")

        
