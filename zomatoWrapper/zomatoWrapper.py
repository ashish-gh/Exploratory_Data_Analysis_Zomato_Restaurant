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
        self.read_rest = []
        self.read_list = []


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

    