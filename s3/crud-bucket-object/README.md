## Create bash files 

- Open the file in your text editor and add the bash at the top. This line tells the system to use the Bash shell to execute the commands in the script. 
- Use more portable shebang line #!/usr/bin/env that ensures the script runs with a compatible shell
- Write your script below the shebang line
- Now using this command `ls -la s3/bash-scripts/` permission:
example: -rw-r--r-- 1 gitpod gitpod  19 Aug 20 00:38 create-bucket
- Make the Script Executable: chmod +x script_name. To apply on everything into folder chmod +x s3/bash-scripts/*
after: -rwxr-xr-x 1 gitpod gitpod  19 Aug 20 00:38 create-bucket
