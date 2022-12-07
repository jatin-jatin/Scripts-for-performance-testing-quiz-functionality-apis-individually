# Initial configurations
### NOTE : Do these steps in the initial_configuration folder
 1. Place the latest copys of credentials.py and Answers.py in the initial_configuration folder.
 2. Ensure you have requests  and json library installed . In case not, you can use pip for installing them.
 3. configure the host in host.py by editing host.py
 4. Run buildcookies.py that will take significant time and will generate "cookies.py"
 5. Ensure that quizid.py exists and was executed once to store the quizid. Also ensure that buildcookies.py was successfully executed.
 6. Execute buildkeystate.py this will generate the "keystate.py" file.
 7. Also execute coursecode.py in order to store the coursecode.
 <!-- 8. Also ensure that Answers.py is in the initial_configuration folder. -->
 <!-- 8. execute files.sh to apply changes to all files -->
# Running Each API with locust
 $ locust -f <API.py>
example to run quiz_info use : locust -f quiz_info.py
### NOTE : After everytime you run login.py the cookies.py needs to be updated by running the buildcookies.py .
