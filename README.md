# README

# simple app to detect language of input text 
# " English / Arabic / Franco " 
## simple html form code to execute python script  
------------------------------------------------------------------------------
#to install apache2 server :
 ## sudo apt-get install apache2
#you have to Set up CGI with Apache 
------------------------------------------------------------------------------
#create a file if not found 
##/etc/apache2/conf-available/cgi-enabled.conf:

#cgi-enabled.conf content :
##<Directory "/var/www/html/cgi-enabled">
##      Options +ExecCGI
 ##     AddHandler cgi-script .cgi .py
##</Directory>
------------------------------------------------------------------------------
#/etc/apache2/conf-enabled/cgi-enabled.conf:
 ##     <Directory "/var/www/html/cgi-enabled">
 ##           Options +ExecCGI
 ##          AddHandler cgi-script .cgi .py
 ##     </Directory>
------------------------------------------------------------------------------
#append this code to /etc/apache2/apache2.conf:
##AddDefaultCharset utf-8 
------------------------------------------------------------------------------
#to start/stop/restart server :

##sudo service apache2 status
##sudo service apache2 start
##sudo service apache2 stop
##sudo service apache2 restart
#or
##sudo /etc/init.d/apache2 start
##sudo /etc/init.d/apache2 stop
##sudo /etc/init.d/apache2 restart
##sudo /etc/init.d/apache2 status
------------------------------------------------------------------------------
#your HTML script can be located anywhere 
#your python script should be located in 
##/usr/lib/cgi-bin/python_script_name.python
------------------------------------------------------------------------------
#to make python script executable :
##chmod 755 python_script_name.py
------------------------------------------------------------------------------
#install Language detection library :
##pip install langdetect
------------------------------------------------------------------------------
#this tutorial may help :
##https://www.youtube.com/watch?v=CTvsjQi5oCM
------------------------------------------------------------------------------
------------------------------------------------------------------------------
