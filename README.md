# Upgraded Odoo eLearning Module

## Overview

A odoo module designed for Wizeline, Inc.

Wizeline, Inc. requires the importation of courses via a Google Docs Document, importation of skills, adding skills to courses, exportation of students with their respective skills.

This module facilitates said requirements.

## Odoo Module
Every odoo module follows the structure below. To create a module you need to atleast have two files  ```manifest.py```  and  ```__init__.py``` . 

    my_module
    ├── __init__.py
    ├── __manifest__.py
    ├── controllers
    │   ├── __init__.py
    │   └── controllers.py
    ├── demo
    │   └── demo.xml
    ├── models
    │   ├── __init__.py
    │   └── models.py
    ├── security
    │   └── ir.model.access.csv
    └── views
        ├── templates.xml
        └── views.xml
If you do not want to bother installing Odoo on your computer, you can also [download](https://www.odoo.com/documentation/16.0/_downloads/b7f3a4243ae7f3166cd5c4d23a256739/my_module.zip) this module structure template in which you replace every occurrences of my_module to the name of your choice. For more information visit the official [Odoo Documentation](https://www.odoo.com/documentation/16.0/administration/odoo_sh/getting_started/first_module.html) .

You can also create this structure manually, you can visit the official documentation on how to [Build an Odoo module](https://www.odoo.com/documentation/16.0/developer/howtos/backend.html) to understand the structure of a module and the content of each file.

## Deployment
To deploy a custom module to Odoo.sh simply add the folder containing your module to the repository. If you worked on your module locally: 

1. Clone the repository linked to Odoo.sh.
2. Add the custom module folder, in this case ```eLearning_upgraded```, to the cloned folder.
3. Commit the changes and push to the remote repository.
**Note:**
Your can also follow this [tutorial](https://www.youtube.com/watch?v=rZaHSTvljuA)


Every commit to the repository will be automatically applied in Odoo.sh. If you are in a development branch in Odoo.sh every commit will generate a new build for more information on Odoo.sh branches visit [here](https://www.odoo.com/documentation/16.0/administration/odoo_sh/getting_started/branches.html#odoosh-gettingstarted-branches-tabs-settings).  
