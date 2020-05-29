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


    def search(self, city_id, entity_type):
        """This api provides you with list
        of restaurant details in provided city.

        Parameters:
        city_id: ID of city 
        entity_type: 
        """

        
        if city_id.isnumeric() == False:
            raise ValueError("Invalid city_id")

        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "search?entity_id="+ str(city_id) + "&entity_type=" + str(entity_type), headers=headers).content).decode("utf-8")
        a = json.loads(r,strict=False)

        # name of file 
        path = os.path.join(path_to_folder,str(city_id)+'_'+str(entity_type)+'.json') 

        # dumping json file
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(a, f, ensure_ascii=False, indent=4)
            print("File saved successfully. . .")

        return a

    