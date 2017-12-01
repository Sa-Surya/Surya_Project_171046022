#*********************************************
#Main function for connecting to Streaming API
#*********************************************

import sys, dataGen

def main():
	keyword=raw_input("Enter the Keyword: ")
	filename=raw_input("Give a datastore name(as .csv): ")
	dataGen.fetchTweets(keyword,filename)	
	
if __name__ == "__main__": 
	main()