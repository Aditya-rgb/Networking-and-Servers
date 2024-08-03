import requests  #Imported the library for performing the HTTP requests.
import time  #Imported for handeling time realated code add ons.
from tabulate import tabulate  #Importing this library to display the output in tabular format please.

class SubdomainTester:
    #Initializing the class and passing subdomain urls with it along with sleep time
    def __init__(self, subdomains, sleep_time=60):

        self.subdomains = subdomains
        self.sleep_time = sleep_time

    #Checking the status of the sub-domain provided
    def status_of_subdomain(self, url):
 
            response = requests.get(url, timeout=5) 
            if (response.status_code == 200):
                return "UP AND RUNNING :)"
            else:
                return "DOWN AND STILL DOWN :("
 
    #Created this function to display the result in tabular format:)
    def showcase_display(self, all_status):
        
        tabular_display = []
        for link, status in all_status.items():
            tabular_display.append([link, status])
        #Found this code to clear the screen    
        print("\033[H\033[J") 
        print(tabulate(tabular_display, headers=["Subdomain Name", "Status"], tablefmt="grid"))

    #Calling all the function we created above :)
    def go_live(self):
        #Putting this in while loop to check continously
        while True:
            all_status = {}
            for link in self.subdomains:
                status = self.status_of_subdomain(link)
                all_status[link] = status
            self.showcase_display(all_status)
            #after sleep time gets over check again
            time.sleep(self.sleep_time)  

if __name__ == "__main__":

    subdomains = [
        "https://mailchimp.com/resources/subdomain-example/"
    ]
    
    
    subdomain_availability = SubdomainTester(subdomains)
    subdomain_availability.go_live()
