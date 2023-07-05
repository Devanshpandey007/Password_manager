import pandas as pd
lst1 = ["website1","website2","website3","website4"]
lst2 = ["email1","email2","email3","email4"]
lst3 = ['Pass1',"pass2","pass3","pass4"]
dict = {"website": lst1,
        "Email": lst2,
        "password":lst3}

df = pd.DataFrame(dict)