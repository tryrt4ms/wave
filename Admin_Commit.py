import subprocess
try:
    #subprocess.call('C:/GIT/cmd/git init',shell=True)
    subprocess.call('C:/GIT/cmd/git config --global user.email "tryrt4ms@gmail.com"', shell=True)
    subprocess.call('C:/GIT/cmd/git config --global user.name "tryrt4ms"', shell=True)
    subprocess.call('C:/GIT/cmd/git add "users.csv"',shell=True)
    subprocess.call('C:/GIT/cmd/git add "symbol.csv"',shell=True)
    subprocess.call('C:/GIT/cmd/git commit -F "users.csv"',shell=True)
    subprocess.call('C:/GIT/cmd/git commit -F "symbol.csv"',shell=True)
    subprocess.call('C:/GIT/cmd/git remote add origin https://github.com/tryrt4ms/wave.git',shell=True)
    subprocess.call('C:/GIT/cmd/git config -l',shell=True)
    subprocess.call('C:/GIT/cmd/git config remote.origin.url https://tryrt4ms:a19081984@github.com/tryrt4ms/wave.git',shell=False)
    subprocess.call('C:/GIT/cmd/git push origin master',shell=True)
except Exception, e:
    print str(e)
