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
        self.path_to_review_folder="raw_data_reviews"
        self.path_to_processed_data= "processed_data"
        self.read_rest = []
        self.read_list = []
        global read_file


    def search(self, city_id, entity_type):
        """This api provides you with list
        of restaurant details in provided city.

        Parameters:
        city_id: ID of city 
        entity_type: 
        """

        
        # if city_id.isnumeric() == False:
        #     raise ValueError("Invalid city_id")

        headers = {'user-key': self.user_key}
        response = requests.get(self.base_url + "search?entity_id="+ str(city_id) + "&entity_type=" + str(entity_type)+"&start=1&count=20", headers=headers)
        self.read_rest = json.loads(response.text)
        self.read_list.append(self.read_rest)

        # # check if directory exists
        if not os.path.isdir(self.path_to_folder):
            # make directory
            try:
                os.makedirs(self.path_to_folder)
            except FileExistsError:
                print("Directory " + self.path_to_folder + " already exist")

        
        # check if file exists
        if not os.path.isfile(str(city_id)+'_'+str(entity_type+'.json')):
            try:
                # make filr
                # name of file 
                path = os.path.join(self.path_to_folder,str(city_id)+'_'+str(entity_type)+'.json') 
                
                # # dumping json file
                with open(path, 'w') as jsonfile:
                    json.dump(self.read_list, jsonfile)
                    print("File saved successfully. . .")
            except:
                print("File "+str(city_id)+'_'+str(entity_type)+'.json already exists')

        return self.read_list

    
    def get_reviews(self, restaurant_id):

        """This api provides you with list
        of reviews for restaurant .

        Parameters:
        restaurant_id: ID of restaurant 
        """
        
        headers = {'user-key': self.user_key}
        response = requests.get(self.base_url + "reviews?res_id="+str(restaurant_id), headers=headers)
        self.read_rest = json.loads(response.text)
        
        for i in range(len(self.read_rest)):

                print("yes")

        # self.read_list.append(self.read_rest)


        # path = os.path.join(self.path_to_review_folder,'reviews_restaurant.json') 
                
        # with open(path, 'w') as jsonfile:
        #     json.dump(self.read_list, jsonfile)
        #     print("File saved successfully. . .")
        

    def get_reviews(self):


        """This api provides you with list
        of reviews for restaurant .

        Parameters:
        restaurant_id: ID of restaurant 
        """
        
        headers = {'Accept': 'application/json', 'user-key': self.user_key}

        review_details = {}

        # Read restaurant file 
        try:
            with open(os.path.join(self.path_to_processed_data,"restaurant_id.txt"), "r") as read_file:
                rest_ID= []
                for i in read_file:
                    i = i.replace('\n', '')
                    rest_ID.append(i)
        except IOError:
            print("File not found")
            return

        for rest_id in rest_ID[900:1800]:
            response = (requests.get(self.base_url + "reviews?res_id="+str(rest_id), headers=headers).content).decode('utf-8')
            loaded_file = json.loads(response)
        
            for i in loaded_file['user_reviews']:
                review_details.update({i['review']['review_text'] : rest_id})
            
            print("Printing for : {}".format(rest_id))

            # save review of received restaurant to json
        path = os.path.join(self.path_to_review_folder,'reviews_restaurant_900_1800.json') 
                
        with open(path, 'w') as jsonfile:
            json.dump(review_details, jsonfile)
            print("File saved successfully. . .")
