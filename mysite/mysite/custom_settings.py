import os                                                                        
                                                                             
DEBUG = True                                                                     
TEMPLATE_DEBUG = DEBUG                                                           
                                                                                 
DATABASES = {                                                                    
   'default': {                                                                  
       'ENGINE': 'django.db.backends.postgresql_psycopg2',                       
       'NAME': 'mysite3',             # change it to your postgres database name
       'USER': 'tonyhlee',             # change it to the postgres database user    
       'PASSWORD': '',                 # change it to your own password      
       'HOST': 'localhost',                                                      
       'PORT': '5432',                                                           
   }                                                                             
}                                                                         
