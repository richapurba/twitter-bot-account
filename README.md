# twitter-bot-account

This is the step by step how to create the twitter bot account

#Preparation from Twitter

First, create 2 twitter accounts. One for the bot, and one is for the testing.
Then, go to developer twitter API href="https://developer.twitter.com" and create an account with your bot account, then hit apply. Follow the steps and make sure you have a mobile number and email that integrated with your bot account. In the specific section, only choose "Yes" for the retweet etc functionality question (second one). Then, review your summary and put a check with the developer agreement. Next step is to confirm your email. After email confirmation, you shall get a notice that your application is under review. Sometimes it's instant but sometimes you need to be patience. Once it's done, go the "App" section from the menu bar. Create an app and fill the information that needed; for the website url is your twitter account url. Remember, you don't need to fill up all of the information, some of the questions are optionals. Then, when everything is okay, hit the create button. Once it's done, go to the "Keys and tokens" tab and click the generate button when you want to change your secret key, or you may just straight copy what are already available there: API key and API secret key. Copy and paste that to your code file. Go to the "Permission" tab and check if the access permission is "Read and write", then you're doing good.

#Local preparation

Create a folder where you want to store all of your bot account's data, e.g "Twitter Bot Account". Open the folder in your code editor. Check wether the tweepy has been installed by opening your terminal and do these commands:

'cd [your folder url]
 pip install tweepy'			#you should see the success message after this code
'pip3 install --user tweepy'	#an alternative if the last pip command doesn't work
'python --version'				#you should use python 3 or above. If you don't, please download it.

#Start the code
See the instruction from the video "Create The Ultimate Bot With Python In 30 Minutes" by Code Wizard

#Deploy your bot account for 24/7 works
Go to the pythonanywhere.com and upload your files. Make sure you choose the python 3 version. In the console, go to the bash, type the command 'pip3 install --user tweepy'.

CONGRATULATIONS!! Your bot now is ready to use.
