# CometsAIAgent

This is interactive AI agnets project to help UTD students for thier career plan

Mac Environ ment to VS code 
Creating files and path for VS code 
mkdir AIAgent
cd AIAgent
code .

Environment creation in VS code 

cd path/to/your/project
python3 -m venv .venv
source .venv/bin/activate

To create files in folder of environment
touch agents/__init__.py

Create README.md, main.py, requirement.txt

For github repo cmds
git init
git add .
git commit -m "Initial commit"

Create git repo going to account and do not create README.mdit is already in vscode
git remote add origin http://github.com/harshachinthala/CometsAIAgent (URL of repo)

git push -u origin main
refresh it sends all files 


install all required liibraries

          pip install -r requirements.txt
          python -m spacy download en_core_web_sm


# Prereqisites
1. Create an user using IAM 
IAM all perimission required ex:Fullaccess to Aws bedrock, IAM, S3 etc

2. Make note of Acess key and security key

3. AWS User configure in local system

          aws configure --profile agent1_user

   gives

   AWS Secret Access Key [None]: 
   AWS Secret Access Key [None]: 
   Default region name [None]: us-east-1
   Default output format [None]: json

4. to check use cmd 
aws sts get-caller-identity --profile agent1_user

Step 1: 

Create scraper.py to extract job postings from Linkedin and command to run the file

          python3 scraper.py --max 2"
chrome tab login to linkr=edin and scraps data 
Linkedin jobs were saved in linkedin_cookies.json






