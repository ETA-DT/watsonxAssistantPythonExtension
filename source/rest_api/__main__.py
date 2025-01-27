# ======================================================= #
#  IBM Cloud Code Engine - Functions-as-a-Service Sample  #
#                                                         #
#  __main.py__ (Python sample function)                   #
#                                                         #
#  This sample code uses an external module "lorem"       #
#  to generate an arbitrary result message. IBM code      #
#  engine functions code with references to external      #
#  modules have to be deployed as code-bundles.           # 
#
#  This sample shows how to access URL parameters in a    #
#  function.                                              #
#                                                         #
#  This sample shows how an external reference is coded   #
#  in the source file (__main__.py) and how the modul     #
#  is referenced in the requirements.txt.                 #
#                                                         #
# ======================================================= #

##
 # import the referenced "lorem" module 
from lorem_text import lorem
# import TM1py

##
 # The `main` function is the entry-point into the function.
 # 
 # A function can define multiple functions, but it needs to
 # have one dedicated 'main' function, which will be called
 # by the runtime.
 # 
 # The 'main' function has one optional argument, which 
 # carries all the parameters the function was invoked with.
 # 
 # Those arguments are dynamic and can change between 
 # function invocations. 
 # 
 # Additionally, a function has access to some 
 # predefined and also user-defined environment variables.
 #  
def main(params):
    words = 10
    # tm1_credentials = {
    #     "auth_type":"""basic""",
    #     "password" : "erwan.tang",
    #     "service_root": "91.236.254.119",
    #     "username" : "",
    #     "port" : 5029,
    #     "view_name" : "TM1View"    
    # } 
    # with TM1Service(address=tm1_credentials["service_root"],
    #             port=tm1_credentials["port"],
    #             user=tm1_credentials["username"],
    #             password=tm1_credentials["password"],
    #             ssl=False) as tm1:
    #     first_cube_name = tm1.cubes.get_all_names()[0]
    return {
        # specify headers for the HTTP response
        # we only set the Content-Type in this case, to 
        # ensure the text is properly displayed in the browser
        "headers": {
            "Content-Type": "text/plain;charset=utf-8",
        },
        
        ## use the text generator to create a response sentence
        #  with 10 words
        "body": 'AAAAAAAAAAAAAA',
    }
# Optional:
#   If you used a function name different from 'main', make
#   the function known under the 'main' symbol to the 
#   runtime, so it can be invoked.
#
#   Example:
#
#   def my_main_func_with_another_name(params) {
#     ...
#   }
#   ...
#   main = my_main_func_with_another_name
