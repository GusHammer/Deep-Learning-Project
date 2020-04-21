

"""

To execute this python file, please, verify that you have installed the xampp 
application on your computer. Xampp is open source application made to ease the 
criation of a server on your computer. We used it to run some PHP scripts that 
gather google search images by a query. 

The link to dowload the application is given below:
https://www.apachefriends.org/download.html

If you select a version to download and just accept the download, it
will automatically download itself on "C:/". That means that by default 
it should be saved on C:/xampp/. That is true at least if you install the 
windows version of the app. My O.S. windows so I could not tell for any 
instance if it has the same directory on IOS. In any case, I setted a default
path to it if you using windows. But, if you try to run this python file on IOS,
please, verify that: first, you have downloaded the xampp application; second,
that you've changed the directory path if you need to.


As mentioned on the first report and here now, this python file is by default 
not executed within the application main functionalities; the reason, for it to be
defined this way, is that this is a setter python file, which means that it's executed
only once previously to gather the database files and it saves it on the application's 
database folder for the server to use them. Therefore, proving that: first, you don't 
need to install the xampp application in order to run the application(only if you wish 
to change the database files by yurself); second, that the php files have no direct 
relation to the application main functionalities, they are just to ease the complexity
over acquiring imaged for the database.


Click on the start apache button on your xampp control panel or simply type
into the cmd: C:/xampp/apache_start


This main script should only be executed when the server is started.

"""

from GetImages import extractor as Extractor
from push_extractor_to_xampp import preparator as Preparator
import time

cheese_types = ["mozzarella cheese -pearson -burguer",
                "parmesan cheese -pearson -burguer",
                "cheddar cheese -burguer -meat -potato",
                "gouda cheese -city -church -house -pearson -burguer",
                "swiss cheese -house -airplane -switzerland",
                "camembert cheese",
                "feta cheese",
                "provolone cheese -sausage",
                "edam cheese -house -city -pearson -ball -car",
                "emmental cheese",
                "gorgonzola cheese",
                "ricotta cheese -pearson",
                "cottage cheese -pearson -house -tree"]

additional_features = []  # ["italian", "french", "white background"]
# No additional features were used in the extraction

minimum_number_of_images =  300 # It will save not more than 20 images plus minimum.

# Clean the database/cheese_photos folder before running it.
proceed = str(input("\nDo you wish to execute this script?[yes/no]\n"))

preparator = Preparator()
preparator.make()

if proceed == "yes":
    # Close all your chrome tabs. Open just one new tab.
    first_time_clean = "yes"
    extractor = None
    for i in range(0, len(cheese_types), 4):
        extractor = Extractor("C:/xampp", cheese_types[i:(i+4)], minimum_number_of_images, additional_features, first_time_clean)
        if first_time_clean == "yes":
            extractor.start_apache()
        first_time_clean = "no"
        extractor.thread_start()
        time.sleep(130)

    extractor.stop_apache()
