## Putting It All Together
### Course 6, Week 4

The scripts presented here accomplish the same tasks as required by
the Qwiklabs assignment but may or may not complete the assignment
milestones if you choose to directly copy-paste them in your Qwiklabs
instance. This is because I have refactored and organised them differently
after having completed the project as I did not like how the Qwiklabs
instructions asked us to approach the solutuion, not to mention the
confusing naming scheme.

#### What each of the scripts is:
`convert-images_and-post.py`: Combination of _changeImage.py_ and
_supplier\_image\_upload.py_ in the Qwiklabs  
**Dependencies:**  
- TIFF images in `supplier-data/images/` folder  
- _Webservice_ to upload the converted images to  

`read-descriptions_and-post.py`: Same as the _run.py_ script in the
Qwiklabs assignment  
**Dependencies:**  
- TXT files in `supplier-data/descriptions/` folder  
- _Webservice_ to upload the descriptions to  

`generate-pdf_and-email.py`: Combination of the _report-email.py_
and _reports.py_ script	in the Qwiklabs  
**Dependencies:**  
- TXT files in `supplier-data/descriptions/` folder  
- _emails.py_ imported as a module  

`health-check_and-email.py`: Same as the _health_check.py_ script
in the Qwiklabs assignment  
**Dependencies:**  
- _emails.py_ imported as a module  

`emails.py`: Same as the _emails.py_ script in the Qwiklabs
assignment  
**Dependencies:**  
- _Mailserver_ to use to send emails  


#### These scripts are meant to be executed in the following order:
1. convert-images_and-post.py
2. read-descriptions_and-post.py
3. generate-pdf_and-email.py

#### The following script needs to be executed as a cron job:
- health-check_and-email.py

#### The following script needs to be imported as a module only:
- emails.py

### License of Images
Please check the _LICENSE_ file in `supplier-data/images/` for information
about the license of the images.
