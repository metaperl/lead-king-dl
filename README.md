# lead-king-dl
automatically download leads from www.lead-king.net

# ACKNOWLEDGEMENTS

## This code was written by Bartosz Kolodziej

* /u/hectorlab on reddit
* official website - http://bartoszkolodziej.com

Here is the spec he coded to:

### Project Spec

#### 1. Visit the main page

https://www.lead-king.net/

#### 2. Login to the account 

Click "Login" which will bring you to this page since you are
not authenticated:

https://www.lead-king.net/amember/member.php

The source code of the login page is in 
the file `data\login-page.html` in this repo for
reference.

#### 3. Visit the leads page

Once logged in, you may make a GET request to this page

https://www.lead-king.net/amember/promember/

#### 4. Download the leads

On the leads page you will see a link to download
today's leads:

![](https://i.imgur.com/KOxwfEr.pngp)

Download the .zip file into the `downloads` folder.

#### 5. Unzip the zip file

#### 6. Append the CSV file contents into a a weekly file

The file is probably best named for the year and week of the year.
E.g: 2022-02 contains all files downloaded during the 2nd week
of 2022.

