#***
# 1. configure the host in host.py by editing host.py
# 2. Place the credentials.py file in the same folder as buildCookies.py in order to build cookie credentials.
# 3. Ensure you have requests lib  and json modules installed . In case not use pip for installing  them
# 4. Run buildcookies.py that will take significant time and will generate "cookies.py"
# 5. Ensure that testname.py exists and was executed once to store the quizid. Also ensure that buildcookies.py was successfully executed.
# 6. Execute buildkeystate.py this will generate the "keystate.py" file.
# 7. Also execute coursecode.py in order to store the coursecode.
# 8. execute files.sh to apply changes to all files
#******

#***
#* There are 7 APIs 
# 1. login.py  -> this requires "credentials.py" and "host.py" in the same folder.
# 2. courselist.py -> this requires "cookies.py" and "host.py" in the same folder.
# 3. quizlist.py -> this requires "cookies.py","host.py" and "coursecode.py" in the same folder.
# 4. quizinfo.py -> this requires "cookies.py","host.py" and "quizid.py" in the same folder.
# 5. quizdownload.py -> this requires "cookies.py","host.py" and "quizid.py" in the same folder.
# 6. quizauthenticate.py -> this requires "cookies.py","host.py" and "quizid.py" in the same folder.
# 7. submit.py -> this requires "cookies.py","Answers.py","host.py" and "keystate.py" in the same folder.
#******


#NOTE : After everytime you run login.py the cookies.py needs to be updated.
