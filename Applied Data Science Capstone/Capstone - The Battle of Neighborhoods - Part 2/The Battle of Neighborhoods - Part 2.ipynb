{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# THE BATTLE OF NEIGHBORHOODS"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "New York City's demographics show that it is a large and ethnically diverse metropolis. With it's diverse culture , comes diverse food items. There are many resturants in New york City, each beloning to different categories like Chinese , Indian , French etc.\n",
    "\n",
    "So as part of this project , we will list and visualize all major parts of New York City that has great indian resturants."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For this project we need the following data:\n",
    "1. New York City data that contains list Boroughs, Neighborhoods along with their latitude and longitude.\n",
    "2. Indian resturants in each neighborhood of new york city.\n",
    "3. GeoSpace data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Questions that will be answers at the end of this project :"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. What are best location in New York City for Indian Cuisine?\n",
    "### 2. Which areas have potential Indian Restaurant Market?\n",
    "### 3. Which all areas lack Indian Restaurants?\n",
    "### 4. Which is the best place to stay if you prefer Indian Cuisine?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Methodology:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. We begin by collecting the New York city data from \"https://cocl.us/new_york_dataset\".\n",
    "2. We will find all venues for each neighborhood using FourSquare API.\n",
    "3. We will then filter out all Indian Restuarant venues.\n",
    "4. Next using FourSquare API, we will find the Ratings, Tips, and Like count for all the Indian Resturants.\n",
    "5. Next we will sort the data keeping Ratings as the constraint.\n",
    "6. Finally, we will visualize the Ranking of neighborhoods using python's Folium library."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lets Start by importing the required Libraries."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Libraries imported.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "pd.set_option('display.max_columns', None)\n",
    "pd.set_option('display.max_rows', None)\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "#!pip install geocoder\n",
    "import geocoder\n",
    "import os\n",
    "#!pip install folium\n",
    "import folium # map rendering library\n",
    "from geopy.geocoders import Nominatim # convert an address into latitude and longitude values\n",
    "# Matplotlib and associated plotting modules\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.cm as cm\n",
    "import matplotlib.colors as colors\n",
    "%matplotlib inline\n",
    "\n",
    "\n",
    "print('Libraries imported.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we define a function to get the geocodes i.e latitude and longitude of a given location using geopy."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def geo_location(address):\n",
    "    # get geo location of address\n",
    "    geolocator = Nominatim(user_agent=\"ny_explorer\")\n",
    "    location = geolocator.geocode(address)\n",
    "    latitude = location.latitude\n",
    "    longitude = location.longitude\n",
    "    return latitude,longitude"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We define a function to intract with FourSquare API and get top 100 venues within a radius of 1000 metres for a given latitude and longitude. Below function will return us the venue id , venue name and category."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_venues(lat,lng):\n",
    "    \n",
    "    #set variables\n",
    "    radius=1000\n",
    "    LIMIT=100\n",
    "    CLIENT_ID = ['CLIENT_ID'] # your Foursquare ID\n",
    "    CLIENT_SECRET = ['CLIENT_SECRET'] # your Foursquare Secret\n",
    "    VERSION = '20200401' # Foursquare API version\n",
    "    \n",
    "    #url to fetch data from foursquare api\n",
    "    url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(\n",
    "            CLIENT_ID, \n",
    "            CLIENT_SECRET, \n",
    "            VERSION, \n",
    "            lat, \n",
    "            lng, \n",
    "            radius, \n",
    "            LIMIT)\n",
    "    \n",
    "    # get all the data\n",
    "    results = requests.get(url).json()\n",
    "    venue_data=results[\"response\"]['groups'][0]['items']\n",
    "    venue_details=[]\n",
    "    for row in venue_data:\n",
    "        try:\n",
    "            venue_id=row['venue']['id']\n",
    "            venue_name=row['venue']['name']\n",
    "            venue_category=row['venue']['categories'][0]['name']\n",
    "            venue_details.append([venue_id,venue_name,venue_category])\n",
    "        except KeyError:\n",
    "            pass\n",
    "        \n",
    "    column_names=['ID','Name','Category']\n",
    "    df = pd.DataFrame(venue_details,columns=column_names)\n",
    "    return df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we will define a function to get venue details like like count , rating , tip counts for a given venue id. This will be used for ranking."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_venue_details(venue_id):\n",
    "        \n",
    "    CLIENT_ID = ['CLIENT_ID'] # your Foursquare ID\n",
    "    CLIENT_SECRET = ['CLIENT_SECRET'] # your Foursquare Secret\n",
    "    VERSION = '20200401' # Foursquare API version\n",
    "    \n",
    "    #url to fetch data from foursquare api\n",
    "    url = 'https://api.foursquare.com/v2/venues/{}?&client_id={}&client_secret={}&v={}'.format(\n",
    "            venue_id,\n",
    "            CLIENT_ID, \n",
    "            CLIENT_SECRET, \n",
    "            VERSION)\n",
    "    \n",
    "    # get all the data\n",
    "    results = requests.get(url).json()\n",
    "    venue_data=results['response']['venue']\n",
    "    venue_details=[]\n",
    "    try:\n",
    "        venue_id=venue_data['id']\n",
    "        venue_name=venue_data['name']\n",
    "        venue_likes=venue_data['likes']['count']\n",
    "        venue_rating=venue_data['rating']\n",
    "        venue_tips=venue_data['tips']['count']\n",
    "        venue_details.append([venue_id,venue_name,venue_likes,venue_rating,venue_tips])\n",
    "    except KeyError:\n",
    "        pass\n",
    "        \n",
    "    column_names=['ID','Name','Likes','Rating','Tips']\n",
    "    df = pd.DataFrame(venue_details,columns=column_names)\n",
    "    return df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we define a funtion to get the new york city data such as Boroughs, Neighborhoods along with their latitude and longitude."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_new_york_data():\n",
    "    url='https://cocl.us/new_york_dataset'\n",
    "    resp=requests.get(url).json()\n",
    "    # all data is present in features label\n",
    "    features=resp['features']\n",
    "    \n",
    "    # define the dataframe columns\n",
    "    column_names = ['Borough', 'Neighborhood', 'Latitude', 'Longitude'] \n",
    "    # instantiate the dataframe\n",
    "    new_york_data = pd.DataFrame(columns=column_names)\n",
    "    \n",
    "    for data in features:\n",
    "        borough = data['properties']['borough'] \n",
    "        neighborhood_name = data['properties']['name']\n",
    "        \n",
    "        neighborhood_latlon = data['geometry']['coordinates']\n",
    "        neighborhood_lat = neighborhood_latlon[1]\n",
    "        neighborhood_lon = neighborhood_latlon[0]\n",
    "    \n",
    "        new_york_data = new_york_data.append({'Borough': borough,\n",
    "                                          'Neighborhood': neighborhood_name,\n",
    "                                          'Latitude': neighborhood_lat,\n",
    "                                          'Longitude': neighborhood_lon}, ignore_index=True)\n",
    "    \n",
    "    return new_york_data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will call the above funtion to get the new york city data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "new_york_data=get_new_york_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Borough</th>\n",
       "      <th>Neighborhood</th>\n",
       "      <th>Latitude</th>\n",
       "      <th>Longitude</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Wakefield</td>\n",
       "      <td>40.894705</td>\n",
       "      <td>-73.847201</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Co-op City</td>\n",
       "      <td>40.874294</td>\n",
       "      <td>-73.829939</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Eastchester</td>\n",
       "      <td>40.887556</td>\n",
       "      <td>-73.827806</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Fieldston</td>\n",
       "      <td>40.895437</td>\n",
       "      <td>-73.905643</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Riverdale</td>\n",
       "      <td>40.890834</td>\n",
       "      <td>-73.912585</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Borough Neighborhood   Latitude  Longitude\n",
       "0   Bronx    Wakefield  40.894705 -73.847201\n",
       "1   Bronx   Co-op City  40.874294 -73.829939\n",
       "2   Bronx  Eastchester  40.887556 -73.827806\n",
       "3   Bronx    Fieldston  40.895437 -73.905643\n",
       "4   Bronx    Riverdale  40.890834 -73.912585"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_york_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(306, 4)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_york_data.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The above result shows that there are 306 different Neighborhoods in New York."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let create a BAR PLOT to show different Neighborhoods in New York."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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QRCw6qqrLunqaJhbfvnlAZgxYwZjx45tu5uQg4UlSZIGWG1MwKhRo5ZwTfRKUTuX+jPexEBAkiRpkNgdSJ3SiXPJQECSJEnqQgYCkiRJGnDrrLMO55xzTsv5p06dSkRw++2395hn0qRJjBkzphPVW8SUKVOIiCUyy9PEiRPZYostBnw/DhaWJElagtY54apB3d/U0/fsU/6DDz6Yiy++mNNOO40TTjhhQfoVV1zBu971LjKzpXJ+//vfs8IKK/Rp3xpYtghIkiSpVyNHjuSMM87gn//8Z9tlvPrVrx42g6W75YZvBgKSJEnq1S677MK4ceM47bTTesxz0003scMOO7D88suz1lprcfTRRzN79uwF6xu7Bt17771sv/32jBw5kk022YTJkycTEVxxxRULlfu3v/2Nt7zlLYwaNYrNN9+cm2++eZF9X3HFFWywwQaMHDmSXXfdlUceeWSh9eeffz7rrbceyy67LBtuuCHf/e53F1ofEXzjG99gr732YoUVVuALX/jCgnV/+MMf2HLLLRk1ahTbbbcd9913X5/Kfvjhh9lrr71YccUVWWmlldhvv/2YPn36QnlOP/10Vl99dUaPHs2hhx7KvHnzejzOnWQgIEmSpF6NGDGCL37xi5x77rk8+uiji6y/8847eetb38o+++zDHXfcwY9+9CNuuOEGjjzyyKblvfTSS+y9996MGjWKW2+9lW9+85ucfPLJTfOefPLJfOITn+D2229ngw024H3vex8vvPDCgvVz5szh1FNP5eKLL+bGG2/kmWee4b3vfe+C9ZdffjnHHHMMH//4x7nrrrv4yEc+wiGHHMKvf/3rhfZzyimnsNdee3HnnXfyoQ99aKH9n3XWWdx2220svfTSC61bXNmZyd57780//vEPrr/+eq655hoeeOAB9t9//wVlXHrppZxyyimceuqp3Hbbbayxxhqcd955vb0dHROt9usaTBGxNDAReD8wDngcmAR8ITNfqvIEcArwH8AqwK3AEZn55xb3sRIwc+bMmay00kqdfgmSJA0rg91Pfbjoa3/6nsybN48HH3yQ8ePHM3LkyIXWDYcxAk8//TRXXHEF2267LZtssgkXXnjhQmMEDjzwQJZffnkuuOCCBdvdcMMNTJgwgdmzZzNy5EjWWWcdjj32WI499lh+8Ytf8I53vINHHnmEcePGATB58mR23XVXLr/8cvbee2+mTp3K+PHj+da3vsWhhx4KwN13382mm27KPffcw0YbbcSkSZM45JBDuOWWW/i3f/s3oLQ0bLzxxtx6661svfXWvOlNb2LTTTflm9/85oK67bfffsyePZurrirHPiI49thj+fKXv7wgz5QpU3jLW97C5MmT2XnnnQG4+uqr2XPPPZk7dy4jR45cbNnXXHMNe+yxBw8++CBrrbXWQq/hd7/7HVtttRXbbbcdm2++Oeeff/6CMrbZZhvmzZvX60Dp3s6pZ555hpVXXhlg5cx8pqcyhmqLwPHAR4EjgY2B44BPAkfV5TkO+FiVZytgGnBNRIwe3KpKkiR1hzPOOIOLL76Yu+++e6H0P/zhD0yaNIkVV1xxwfLWt76Vl156iQcffHCRcu677z7WWmutBUEAwNZbb910n5ttttmCv9dYYw2g3FG3Zumll2bLLbdc8HyjjTZizJgx3HPPPQDcc889vOlNb1qozDe96U0L1tfUl9Hq/hdX9j333MNaa621IAgA2GSTTRap37bbbrtQGY3PB8pQnTVoW+AnmVkLkadGxPuALWFBa8CxwKmZeVmVdhAwHTgAuGDRIiVJktQfO+ywA29961s56aSTOPjggxekv/TSS3zkIx/h6KOPXmSb17zmNYukZWbLN8RaZpllFvxd2+all15aKE+zsurTGtc3239PMxotbv+9ld3T6+zL6x9IQ7VF4AZg54jYACAiNge2B66u1o+ndBn6VW2DzJwPXA9s16zAiFguIlaqLYAtB5IkSX102mmnceWVV3LTTTctSHvDG97An//8Z1772tcusiy77LKLlLHRRhvx8MMPLzRo9ve//31b9XnhhRe47bbbFjy/7777ePrpp9loo40A2HjjjbnhhhsW2uamm25i4403bmt/9RZX9iabbMLDDz+80ODlu+++m5kzZy7Is/HGG3PLLbcsVEbj84EyVFsEzgBWBu6NiBeBEcDJmfmDan2tHWl6w3bTgbV7KPNEypgCSZIktWmzzTbj/e9/P+eee+6CtOOPP55tttmGI444gg9/+MOssMIK3HPPPVxzzTUL5avZddddWW+99TjooIM488wzmTVr1oLBwn39pXyZZZbhqKOO4qtf/SrLLLMMRx55JNtss82Crkaf/OQn2W+//XjDG97AzjvvzJVXXslll13G5MmT+3EUaKnsXXbZZcHx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\n",
      "text/plain": [
       "<Figure size 900x500 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(9,5), dpi = 100)\n",
    "# title\n",
    "plt.title('Number of Neighborhood for each Borough in New York City')\n",
    "#On x-axis\n",
    "plt.xlabel('Borough', fontsize = 15)\n",
    "#On y-axis\n",
    "plt.ylabel('No.of Neighborhood', fontsize=15)\n",
    "#giving a bar plot\n",
    "new_york_data.groupby('Borough')['Neighborhood'].count().plot(kind='bar')\n",
    "#legend\n",
    "plt.legend()\n",
    "#displays the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### From the above Bar Plot, we can see that Queens has highest number of neighborhoods."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next we will collect Indian resturants for each Neighborhood."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "( 1 / 306 ) Indian Resturants in Wakefield, Bronx:0\n",
      "( 2 / 306 ) Indian Resturants in Co-op City, Bronx:0\n",
      "( 3 / 306 ) Indian Resturants in Eastchester, Bronx:0\n",
      "( 4 / 306 ) Indian Resturants in Fieldston, Bronx:0\n",
      "( 5 / 306 ) Indian Resturants in Riverdale, Bronx:0\n",
      "( 6 / 306 ) Indian Resturants in Kingsbridge, Bronx:0\n",
      "( 7 / 306 ) Indian Resturants in Marble Hill, Manhattan:0\n",
      "( 8 / 306 ) Indian Resturants in Woodlawn, Bronx:1\n",
      "( 9 / 306 ) Indian Resturants in Norwood, Bronx:0\n",
      "( 10 / 306 ) Indian Resturants in Williamsbridge, Bronx:0\n",
      "( 11 / 306 ) Indian Resturants in Baychester, Bronx:0\n",
      "( 12 / 306 ) Indian Resturants in Pelham Parkway, Bronx:0\n",
      "( 13 / 306 ) Indian Resturants in City Island, Bronx:0\n",
      "( 14 / 306 ) Indian Resturants in Bedford Park, Bronx:0\n",
      "( 15 / 306 ) Indian Resturants in University Heights, Bronx:0\n",
      "( 16 / 306 ) Indian Resturants in Morris Heights, Bronx:0\n",
      "( 17 / 306 ) Indian Resturants in Fordham, Bronx:0\n",
      "( 18 / 306 ) Indian Resturants in East Tremont, Bronx:0\n",
      "( 19 / 306 ) Indian Resturants in West Farms, Bronx:0\n",
      "( 20 / 306 ) Indian Resturants in High  Bridge, Bronx:0\n",
      "( 21 / 306 ) Indian Resturants in Melrose, Bronx:0\n",
      "( 22 / 306 ) Indian Resturants in Mott Haven, Bronx:0\n",
      "( 23 / 306 ) Indian Resturants in Port Morris, Bronx:0\n",
      "( 24 / 306 ) Indian Resturants in Longwood, Bronx:0\n",
      "( 25 / 306 ) Indian Resturants in Hunts Point, Bronx:0\n",
      "( 26 / 306 ) Indian Resturants in Morrisania, Bronx:0\n",
      "( 27 / 306 ) Indian Resturants in Soundview, Bronx:0\n",
      "( 28 / 306 ) Indian Resturants in Clason Point, Bronx:0\n",
      "( 29 / 306 ) Indian Resturants in Throgs Neck, Bronx:0\n",
      "( 30 / 306 ) Indian Resturants in Country Club, Bronx:0\n",
      "( 31 / 306 ) Indian Resturants in Parkchester, Bronx:1\n",
      "( 32 / 306 ) Indian Resturants in Westchester Square, Bronx:0\n",
      "( 33 / 306 ) Indian Resturants in Van Nest, Bronx:0\n",
      "( 34 / 306 ) Indian Resturants in Morris Park, Bronx:0\n",
      "( 35 / 306 ) Indian Resturants in Belmont, Bronx:0\n",
      "( 36 / 306 ) Indian Resturants in Spuyten Duyvil, Bronx:1\n",
      "( 37 / 306 ) Indian Resturants in North Riverdale, Bronx:0\n",
      "( 38 / 306 ) Indian Resturants in Pelham Bay, Bronx:0\n",
      "( 39 / 306 ) Indian Resturants in Schuylerville, Bronx:0\n",
      "( 40 / 306 ) Indian Resturants in Edgewater Park, Bronx:0\n",
      "( 41 / 306 ) Indian Resturants in Castle Hill, Bronx:0\n",
      "( 42 / 306 ) Indian Resturants in Olinville, Bronx:0\n",
      "( 43 / 306 ) Indian Resturants in Pelham Gardens, Bronx:0\n",
      "( 44 / 306 ) Indian Resturants in Concourse, Bronx:1\n",
      "( 45 / 306 ) Indian Resturants in Unionport, Bronx:2\n",
      "( 46 / 306 ) Indian Resturants in Edenwald, Bronx:0\n",
      "( 47 / 306 ) Indian Resturants in Bay Ridge, Brooklyn:1\n",
      "( 48 / 306 ) Indian Resturants in Bensonhurst, Brooklyn:0\n",
      "( 49 / 306 ) Indian Resturants in Sunset Park, Brooklyn:0\n",
      "( 50 / 306 ) Indian Resturants in Greenpoint, Brooklyn:0\n",
      "( 51 / 306 ) Indian Resturants in Gravesend, Brooklyn:0\n",
      "( 52 / 306 ) Indian Resturants in Brighton Beach, Brooklyn:1\n",
      "( 53 / 306 ) Indian Resturants in Sheepshead Bay, Brooklyn:0\n",
      "( 54 / 306 ) Indian Resturants in Manhattan Terrace, Brooklyn:0\n",
      "( 55 / 306 ) Indian Resturants in Flatbush, Brooklyn:2\n",
      "( 56 / 306 ) Indian Resturants in Crown Heights, Brooklyn:0\n",
      "( 57 / 306 ) Indian Resturants in East Flatbush, Brooklyn:1\n",
      "( 58 / 306 ) Indian Resturants in Kensington, Brooklyn:2\n",
      "( 59 / 306 ) Indian Resturants in Windsor Terrace, Brooklyn:0\n",
      "( 60 / 306 ) Indian Resturants in Prospect Heights, Brooklyn:0\n",
      "( 61 / 306 ) Indian Resturants in Brownsville, Brooklyn:0\n",
      "( 62 / 306 ) Indian Resturants in Williamsburg, Brooklyn:0\n",
      "( 63 / 306 ) Indian Resturants in Bushwick, Brooklyn:0\n",
      "( 64 / 306 ) Indian Resturants in Bedford Stuyvesant, Brooklyn:0\n",
      "( 65 / 306 ) Indian Resturants in Brooklyn Heights, Brooklyn:0\n",
      "( 66 / 306 ) Indian Resturants in Cobble Hill, Brooklyn:0\n",
      "( 67 / 306 ) Indian Resturants in Carroll Gardens, Brooklyn:0\n",
      "( 68 / 306 ) Indian Resturants in Red Hook, Brooklyn:0\n",
      "( 69 / 306 ) Indian Resturants in Gowanus, Brooklyn:1\n",
      "( 70 / 306 ) Indian Resturants in Fort Greene, Brooklyn:1\n",
      "( 71 / 306 ) Indian Resturants in Park Slope, Brooklyn:0\n",
      "( 72 / 306 ) Indian Resturants in Cypress Hills, Brooklyn:0\n",
      "( 73 / 306 ) Indian Resturants in East New York, Brooklyn:0\n",
      "( 74 / 306 ) Indian Resturants in Starrett City, Brooklyn:0\n",
      "( 75 / 306 ) Indian Resturants in Canarsie, Brooklyn:0\n",
      "( 76 / 306 ) Indian Resturants in Flatlands, Brooklyn:0\n",
      "( 77 / 306 ) Indian Resturants in Mill Island, Brooklyn:0\n",
      "( 78 / 306 ) Indian Resturants in Manhattan Beach, Brooklyn:0\n",
      "( 79 / 306 ) Indian Resturants in Coney Island, Brooklyn:0\n",
      "( 80 / 306 ) Indian Resturants in Bath Beach, Brooklyn:0\n",
      "( 81 / 306 ) Indian Resturants in Borough Park, Brooklyn:0\n",
      "( 82 / 306 ) Indian Resturants in Dyker Heights, Brooklyn:0\n",
      "( 83 / 306 ) Indian Resturants in Gerritsen Beach, Brooklyn:0\n",
      "( 84 / 306 ) Indian Resturants in Marine Park, Brooklyn:0\n",
      "( 85 / 306 ) Indian Resturants in Clinton Hill, Brooklyn:2\n",
      "( 86 / 306 ) Indian Resturants in Sea Gate, Brooklyn:0\n",
      "( 87 / 306 ) Indian Resturants in Downtown, Brooklyn:0\n",
      "( 88 / 306 ) Indian Resturants in Boerum Hill, Brooklyn:0\n",
      "( 89 / 306 ) Indian Resturants in Prospect Lefferts Gardens, Brooklyn:2\n",
      "( 90 / 306 ) Indian Resturants in Ocean Hill, Brooklyn:2\n",
      "( 91 / 306 ) Indian Resturants in City Line, Brooklyn:0\n",
      "( 92 / 306 ) Indian Resturants in Bergen Beach, Brooklyn:0\n",
      "( 93 / 306 ) Indian Resturants in Midwood, Brooklyn:0\n",
      "( 94 / 306 ) Indian Resturants in Prospect Park South, Brooklyn:2\n",
      "( 95 / 306 ) Indian Resturants in Georgetown, Brooklyn:0\n",
      "( 96 / 306 ) Indian Resturants in East Williamsburg, Brooklyn:0\n",
      "( 97 / 306 ) Indian Resturants in North Side, Brooklyn:1\n",
      "( 98 / 306 ) Indian Resturants in South Side, Brooklyn:1\n",
      "( 99 / 306 ) Indian Resturants in Ocean Parkway, Brooklyn:0\n",
      "( 100 / 306 ) Indian Resturants in Fort Hamilton, Brooklyn:0\n",
      "( 101 / 306 ) Indian Resturants in Chinatown, Manhattan:0\n",
      "( 102 / 306 ) Indian Resturants in Washington Heights, Manhattan:1\n",
      "( 103 / 306 ) Indian Resturants in Inwood, Manhattan:0\n",
      "( 104 / 306 ) Indian Resturants in Hamilton Heights, Manhattan:2\n",
      "( 105 / 306 ) Indian Resturants in Manhattanville, Manhattan:2\n",
      "( 106 / 306 ) Indian Resturants in Central Harlem, Manhattan:2\n",
      "( 107 / 306 ) Indian Resturants in East Harlem, Manhattan:1\n",
      "( 108 / 306 ) Indian Resturants in Upper East Side, Manhattan:0\n",
      "( 109 / 306 ) Indian Resturants in Yorkville, Manhattan:1\n",
      "( 110 / 306 ) Indian Resturants in Lenox Hill, Manhattan:0\n",
      "( 111 / 306 ) Indian Resturants in Roosevelt Island, Manhattan:1\n",
      "( 112 / 306 ) Indian Resturants in Upper West Side, Manhattan:2\n",
      "( 113 / 306 ) Indian Resturants in Lincoln Square, Manhattan:0\n",
      "( 114 / 306 ) Indian Resturants in Clinton, Manhattan:0\n",
      "( 115 / 306 ) Indian Resturants in Midtown, Manhattan:1\n",
      "( 116 / 306 ) Indian Resturants in Murray Hill, Manhattan:1\n",
      "( 117 / 306 ) Indian Resturants in Chelsea, Manhattan:1\n",
      "( 118 / 306 ) Indian Resturants in Greenwich Village, Manhattan:0\n",
      "( 119 / 306 ) Indian Resturants in East Village, Manhattan:0\n",
      "( 120 / 306 ) Indian Resturants in Lower East Side, Manhattan:0\n",
      "( 121 / 306 ) Indian Resturants in Tribeca, Manhattan:1\n",
      "( 122 / 306 ) Indian Resturants in Little Italy, Manhattan:0\n",
      "( 123 / 306 ) Indian Resturants in Soho, Manhattan:0\n",
      "( 124 / 306 ) Indian Resturants in West Village, Manhattan:2\n",
      "( 125 / 306 ) Indian Resturants in Manhattan Valley, Manhattan:5\n",
      "( 126 / 306 ) Indian Resturants in Morningside Heights, Manhattan:1\n",
      "( 127 / 306 ) Indian Resturants in Gramercy, Manhattan:3\n",
      "( 128 / 306 ) Indian Resturants in Battery Park City, Manhattan:0\n",
      "( 129 / 306 ) Indian Resturants in Financial District, Manhattan:0\n",
      "( 130 / 306 ) Indian Resturants in Astoria, Queens:1\n",
      "( 131 / 306 ) Indian Resturants in Woodside, Queens:8\n",
      "( 132 / 306 ) Indian Resturants in Jackson Heights, Queens:6\n",
      "( 133 / 306 ) Indian Resturants in Elmhurst, Queens:2\n",
      "( 134 / 306 ) Indian Resturants in Howard Beach, Queens:0\n",
      "( 135 / 306 ) Indian Resturants in Corona, Queens:0\n",
      "( 136 / 306 ) Indian Resturants in Forest Hills, Queens:0\n",
      "( 137 / 306 ) Indian Resturants in Kew Gardens, Queens:2\n",
      "( 138 / 306 ) Indian Resturants in Richmond Hill, Queens:6\n",
      "( 139 / 306 ) Indian Resturants in Flushing, Queens:0\n",
      "( 140 / 306 ) Indian Resturants in Long Island City, Queens:2\n",
      "( 141 / 306 ) Indian Resturants in Sunnyside, Queens:1\n",
      "( 142 / 306 ) Indian Resturants in East Elmhurst, Queens:0\n",
      "( 143 / 306 ) Indian Resturants in Maspeth, Queens:0\n",
      "( 144 / 306 ) Indian Resturants in Ridgewood, Queens:1\n",
      "( 145 / 306 ) Indian Resturants in Glendale, Queens:0\n",
      "( 146 / 306 ) Indian Resturants in Rego Park, Queens:1\n",
      "( 147 / 306 ) Indian Resturants in Woodhaven, Queens:0\n",
      "( 148 / 306 ) Indian Resturants in Ozone Park, Queens:1\n",
      "( 149 / 306 ) Indian Resturants in South Ozone Park, Queens:0\n",
      "( 150 / 306 ) Indian Resturants in College Point, Queens:0\n",
      "( 151 / 306 ) Indian Resturants in Whitestone, Queens:0\n",
      "( 152 / 306 ) Indian Resturants in Bayside, Queens:3\n",
      "( 153 / 306 ) Indian Resturants in Auburndale, Queens:0\n",
      "( 154 / 306 ) Indian Resturants in Little Neck, Queens:0\n",
      "( 155 / 306 ) Indian Resturants in Douglaston, Queens:0\n",
      "( 156 / 306 ) Indian Resturants in Glen Oaks, Queens:4\n",
      "( 157 / 306 ) Indian Resturants in Bellerose, Queens:2\n",
      "( 158 / 306 ) Indian Resturants in Kew Gardens Hills, Queens:1\n",
      "( 159 / 306 ) Indian Resturants in Fresh Meadows, Queens:0\n",
      "( 160 / 306 ) Indian Resturants in Briarwood, Queens:3\n",
      "( 161 / 306 ) Indian Resturants in Jamaica Center, Queens:3\n",
      "( 162 / 306 ) Indian Resturants in Oakland Gardens, Queens:0\n",
      "( 163 / 306 ) Indian Resturants in Queens Village, Queens:0\n",
      "( 164 / 306 ) Indian Resturants in Hollis, Queens:0\n",
      "( 165 / 306 ) Indian Resturants in South Jamaica, Queens:0\n",
      "( 166 / 306 ) Indian Resturants in St. Albans, Queens:0\n",
      "( 167 / 306 ) Indian Resturants in Rochdale, Queens:0\n",
      "( 168 / 306 ) Indian Resturants in Springfield Gardens, Queens:0\n",
      "( 169 / 306 ) Indian Resturants in Cambria Heights, Queens:0\n",
      "( 170 / 306 ) Indian Resturants in Rosedale, Queens:0\n",
      "( 171 / 306 ) Indian Resturants in Far Rockaway, Queens:0\n",
      "( 172 / 306 ) Indian Resturants in Broad Channel, Queens:0\n",
      "( 173 / 306 ) Indian Resturants in Breezy Point, Queens:0\n",
      "( 174 / 306 ) Indian Resturants in Steinway, Queens:1\n",
      "( 175 / 306 ) Indian Resturants in Beechhurst, Queens:0\n",
      "( 176 / 306 ) Indian Resturants in Bay Terrace, Queens:0\n",
      "( 177 / 306 ) Indian Resturants in Edgemere, Queens:0\n",
      "( 178 / 306 ) Indian Resturants in Arverne, Queens:0\n",
      "( 179 / 306 ) Indian Resturants in Rockaway Beach, Queens:0\n",
      "( 180 / 306 ) Indian Resturants in Neponsit, Queens:0\n",
      "( 181 / 306 ) Indian Resturants in Murray Hill, Queens:0\n",
      "( 182 / 306 ) Indian Resturants in Floral Park, Queens:11\n",
      "( 183 / 306 ) Indian Resturants in Holliswood, Queens:1\n",
      "( 184 / 306 ) Indian Resturants in Jamaica Estates, Queens:2\n",
      "( 185 / 306 ) Indian Resturants in Queensboro Hill, Queens:0\n",
      "( 186 / 306 ) Indian Resturants in Hillcrest, Queens:0\n",
      "( 187 / 306 ) Indian Resturants in Ravenswood, Queens:1\n",
      "( 188 / 306 ) Indian Resturants in Lindenwood, Queens:0\n",
      "( 189 / 306 ) Indian Resturants in Laurelton, Queens:0\n",
      "( 190 / 306 ) Indian Resturants in Lefrak City, Queens:0\n",
      "( 191 / 306 ) Indian Resturants in Belle Harbor, Queens:0\n",
      "( 192 / 306 ) Indian Resturants in Rockaway Park, Queens:0\n",
      "( 193 / 306 ) Indian Resturants in Somerville, Queens:0\n",
      "( 194 / 306 ) Indian Resturants in Brookville, Queens:0\n",
      "( 195 / 306 ) Indian Resturants in Bellaire, Queens:1\n",
      "( 196 / 306 ) Indian Resturants in North Corona, Queens:0\n",
      "( 197 / 306 ) Indian Resturants in Forest Hills Gardens, Queens:0\n",
      "( 198 / 306 ) Indian Resturants in St. George, Staten Island:0\n",
      "( 199 / 306 ) Indian Resturants in New Brighton, Staten Island:1\n",
      "( 200 / 306 ) Indian Resturants in Stapleton, Staten Island:0\n",
      "( 201 / 306 ) Indian Resturants in Rosebank, Staten Island:0\n",
      "( 202 / 306 ) Indian Resturants in West Brighton, Staten Island:0\n",
      "( 203 / 306 ) Indian Resturants in Grymes Hill, Staten Island:0\n",
      "( 204 / 306 ) Indian Resturants in Todt Hill, Staten Island:0\n",
      "( 205 / 306 ) Indian Resturants in South Beach, Staten Island:0\n",
      "( 206 / 306 ) Indian Resturants in Port Richmond, Staten Island:0\n",
      "( 207 / 306 ) Indian Resturants in Mariner's Harbor, Staten Island:0\n",
      "( 208 / 306 ) Indian Resturants in Port Ivory, Staten Island:0\n",
      "( 209 / 306 ) Indian Resturants in Castleton Corners, Staten Island:0\n",
      "( 210 / 306 ) Indian Resturants in New Springville, Staten Island:0\n",
      "( 211 / 306 ) Indian Resturants in Travis, Staten Island:0\n",
      "( 212 / 306 ) Indian Resturants in New Dorp, Staten Island:1\n",
      "( 213 / 306 ) Indian Resturants in Oakwood, Staten Island:0\n",
      "( 214 / 306 ) Indian Resturants in Great Kills, Staten Island:0\n",
      "( 215 / 306 ) Indian Resturants in Eltingville, Staten Island:0\n",
      "( 216 / 306 ) Indian Resturants in Annadale, Staten Island:0\n",
      "( 217 / 306 ) Indian Resturants in Woodrow, Staten Island:0\n",
      "( 218 / 306 ) Indian Resturants in Tottenville, Staten Island:0\n",
      "( 219 / 306 ) Indian Resturants in Tompkinsville, Staten Island:1\n",
      "( 220 / 306 ) Indian Resturants in Silver Lake, Staten Island:0\n",
      "( 221 / 306 ) Indian Resturants in Sunnyside, Staten Island:1\n",
      "( 222 / 306 ) Indian Resturants in Ditmas Park, Brooklyn:3\n",
      "( 223 / 306 ) Indian Resturants in Wingate, Brooklyn:0\n",
      "( 224 / 306 ) Indian Resturants in Rugby, Brooklyn:0\n",
      "( 225 / 306 ) Indian Resturants in Park Hill, Staten Island:1\n",
      "( 226 / 306 ) Indian Resturants in Westerleigh, Staten Island:0\n",
      "( 227 / 306 ) Indian Resturants in Graniteville, Staten Island:0\n",
      "( 228 / 306 ) Indian Resturants in Arlington, Staten Island:0\n",
      "( 229 / 306 ) Indian Resturants in Arrochar, Staten Island:0\n",
      "( 230 / 306 ) Indian Resturants in Grasmere, Staten Island:0\n",
      "( 231 / 306 ) Indian Resturants in Old Town, Staten Island:0\n",
      "( 232 / 306 ) Indian Resturants in Dongan Hills, Staten Island:0\n",
      "( 233 / 306 ) Indian Resturants in Midland Beach, Staten Island:0\n",
      "( 234 / 306 ) Indian Resturants in Grant City, Staten Island:1\n",
      "( 235 / 306 ) Indian Resturants in New Dorp Beach, Staten Island:0\n",
      "( 236 / 306 ) Indian Resturants in Bay Terrace, Staten Island:0\n",
      "( 237 / 306 ) Indian Resturants in Huguenot, Staten Island:0\n",
      "( 238 / 306 ) Indian Resturants in Pleasant Plains, Staten Island:0\n",
      "( 239 / 306 ) Indian Resturants in Butler Manor, Staten Island:0\n",
      "( 240 / 306 ) Indian Resturants in Charleston, Staten Island:0\n",
      "( 241 / 306 ) Indian Resturants in Rossville, Staten Island:0\n",
      "( 242 / 306 ) Indian Resturants in Arden Heights, Staten Island:0\n",
      "( 243 / 306 ) Indian Resturants in Greenridge, Staten Island:0\n",
      "( 244 / 306 ) Indian Resturants in Heartland Village, Staten Island:0\n",
      "( 245 / 306 ) Indian Resturants in Chelsea, Staten Island:0\n",
      "( 246 / 306 ) Indian Resturants in Bloomfield, Staten Island:0\n",
      "( 247 / 306 ) Indian Resturants in Bulls Head, Staten Island:0\n",
      "( 248 / 306 ) Indian Resturants in Carnegie Hill, Manhattan:3\n",
      "( 249 / 306 ) Indian Resturants in Noho, Manhattan:0\n",
      "( 250 / 306 ) Indian Resturants in Civic Center, Manhattan:1\n",
      "( 251 / 306 ) Indian Resturants in Midtown South, Manhattan:1\n",
      "( 252 / 306 ) Indian Resturants in Richmond Town, Staten Island:0\n",
      "( 253 / 306 ) Indian Resturants in Shore Acres, Staten Island:0\n",
      "( 254 / 306 ) Indian Resturants in Clifton, Staten Island:0\n",
      "( 255 / 306 ) Indian Resturants in Concord, Staten Island:1\n",
      "( 256 / 306 ) Indian Resturants in Emerson Hill, Staten Island:1\n",
      "( 257 / 306 ) Indian Resturants in Randall Manor, Staten Island:0\n",
      "( 258 / 306 ) Indian Resturants in Howland Hook, Staten Island:0\n",
      "( 259 / 306 ) Indian Resturants in Elm Park, Staten Island:0\n",
      "( 260 / 306 ) Indian Resturants in Remsen Village, Brooklyn:0\n",
      "( 261 / 306 ) Indian Resturants in New Lots, Brooklyn:0\n",
      "( 262 / 306 ) Indian Resturants in Paerdegat Basin, Brooklyn:0\n",
      "( 263 / 306 ) Indian Resturants in Mill Basin, Brooklyn:0\n",
      "( 264 / 306 ) Indian Resturants in Jamaica Hills, Queens:3\n",
      "( 265 / 306 ) Indian Resturants in Utopia, Queens:0\n",
      "( 266 / 306 ) Indian Resturants in Pomonok, Queens:0\n",
      "( 267 / 306 ) Indian Resturants in Astoria Heights, Queens:0\n",
      "( 268 / 306 ) Indian Resturants in Claremont Village, Bronx:0\n",
      "( 269 / 306 ) Indian Resturants in Concourse Village, Bronx:1\n",
      "( 270 / 306 ) Indian Resturants in Mount Eden, Bronx:0\n",
      "( 271 / 306 ) Indian Resturants in Mount Hope, Bronx:0\n",
      "( 272 / 306 ) Indian Resturants in Sutton Place, Manhattan:3\n",
      "( 273 / 306 ) Indian Resturants in Hunters Point, Queens:0\n",
      "( 274 / 306 ) Indian Resturants in Turtle Bay, Manhattan:3\n",
      "( 275 / 306 ) Indian Resturants in Tudor City, Manhattan:2\n",
      "( 276 / 306 ) Indian Resturants in Stuyvesant Town, Manhattan:0\n",
      "( 277 / 306 ) Indian Resturants in Flatiron, Manhattan:0\n",
      "( 278 / 306 ) Indian Resturants in Sunnyside Gardens, Queens:1\n",
      "( 279 / 306 ) Indian Resturants in Blissville, Queens:1\n",
      "( 280 / 306 ) Indian Resturants in Fulton Ferry, Brooklyn:0\n",
      "( 281 / 306 ) Indian Resturants in Vinegar Hill, Brooklyn:0\n",
      "( 282 / 306 ) Indian Resturants in Weeksville, Brooklyn:0\n",
      "( 283 / 306 ) Indian Resturants in Broadway Junction, Brooklyn:1\n",
      "( 284 / 306 ) Indian Resturants in Dumbo, Brooklyn:0\n",
      "( 285 / 306 ) Indian Resturants in Manor Heights, Staten Island:0\n",
      "( 286 / 306 ) Indian Resturants in Willowbrook, Staten Island:0\n",
      "( 287 / 306 ) Indian Resturants in Sandy Ground, Staten Island:0\n",
      "( 288 / 306 ) Indian Resturants in Egbertville, Staten Island:0\n",
      "( 289 / 306 ) Indian Resturants in Roxbury, Queens:0\n",
      "( 290 / 306 ) Indian Resturants in Homecrest, Brooklyn:0\n",
      "( 291 / 306 ) Indian Resturants in Middle Village, Queens:0\n",
      "( 292 / 306 ) Indian Resturants in Prince's Bay, Staten Island:0\n",
      "( 293 / 306 ) Indian Resturants in Lighthouse Hill, Staten Island:0\n",
      "( 294 / 306 ) Indian Resturants in Richmond Valley, Staten Island:0\n",
      "( 295 / 306 ) Indian Resturants in Malba, Queens:0\n",
      "( 296 / 306 ) Indian Resturants in Highland Park, Brooklyn:0\n",
      "( 297 / 306 ) Indian Resturants in Madison, Brooklyn:0\n",
      "( 298 / 306 ) Indian Resturants in Bronxdale, Bronx:0\n",
      "( 299 / 306 ) Indian Resturants in Allerton, Bronx:0\n",
      "( 300 / 306 ) Indian Resturants in Kingsbridge Heights, Bronx:0\n",
      "( 301 / 306 ) Indian Resturants in Erasmus, Brooklyn:1\n",
      "( 302 / 306 ) Indian Resturants in Hudson Yards, Manhattan:0\n",
      "( 303 / 306 ) Indian Resturants in Hammels, Queens:0\n",
      "( 304 / 306 ) Indian Resturants in Bayswater, Queens:0\n",
      "( 305 / 306 ) Indian Resturants in Queensbridge, Queens:2\n",
      "( 306 / 306 ) Indian Resturants in Fox Hills, Staten Island:1\n"
     ]
    }
   ],
   "source": [
    "# prepare neighborhood list that contains indian resturants\n",
    "column_names=['Borough', 'Neighborhood', 'ID','Name']\n",
    "indian_rest_ny=pd.DataFrame(columns=column_names)\n",
    "count=1\n",
    "for row in new_york_data.values.tolist():\n",
    "    Borough, Neighborhood, Latitude, Longitude=row\n",
    "    venues = get_venues(Latitude,Longitude)\n",
    "    indian_resturants=venues[venues['Category']=='Indian Restaurant']   \n",
    "    print('(',count,'/',len(new_york_data),')','Indian Resturants in '+Neighborhood+', '+Borough+':'+str(len(indian_resturants)))\n",
    "    for resturant_detail in indian_resturants.values.tolist():\n",
    "        id, name , category=resturant_detail\n",
    "        indian_rest_ny = indian_rest_ny.append({'Borough': Borough,\n",
    "                                                'Neighborhood': Neighborhood, \n",
    "                                                'ID': id,\n",
    "                                                'Name' : name\n",
    "                                               }, ignore_index=True)\n",
    "    count+=1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that we have got all the indian resturants in new york city , we will analyze it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Borough</th>\n",
       "      <th>Neighborhood</th>\n",
       "      <th>ID</th>\n",
       "      <th>Name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Woodlawn</td>\n",
       "      <td>4c0448d9310fc9b6bf1dc761</td>\n",
       "      <td>Curry Spot</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Parkchester</td>\n",
       "      <td>4c194631838020a13e78e561</td>\n",
       "      <td>Melanies Roti Bar And Grill</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Spuyten Duyvil</td>\n",
       "      <td>4c04544df423a593ac83d116</td>\n",
       "      <td>Cumin Indian Cuisine</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Concourse</td>\n",
       "      <td>551b7f75498e86c00a0ed2e1</td>\n",
       "      <td>Hungry Bird</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Unionport</td>\n",
       "      <td>4c194631838020a13e78e561</td>\n",
       "      <td>Melanies Roti Bar And Grill</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Borough    Neighborhood                        ID  \\\n",
       "0   Bronx        Woodlawn  4c0448d9310fc9b6bf1dc761   \n",
       "1   Bronx     Parkchester  4c194631838020a13e78e561   \n",
       "2   Bronx  Spuyten Duyvil  4c04544df423a593ac83d116   \n",
       "3   Bronx       Concourse  551b7f75498e86c00a0ed2e1   \n",
       "4   Bronx       Unionport  4c194631838020a13e78e561   \n",
       "\n",
       "                          Name  \n",
       "0                   Curry Spot  \n",
       "1  Melanies Roti Bar And Grill  \n",
       "2         Cumin Indian Cuisine  \n",
       "3                  Hungry Bird  \n",
       "4  Melanies Roti Bar And Grill  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "indian_rest_ny.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(151, 4)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "indian_rest_ny.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### From the above result, we see that there are 151 Indian Resturants across New York City."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let create a BAR PLOT to show Number of Indian Resturants for each Borough in New York City."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAwIAAAIgCAYAAAA2r94xAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD+naQAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8li6FKAAAgAElEQVR4nOzdebgcVZn48e9LgEggELYYVDYVUVFQAQcZFZRlcMQVR5RRE8UN1AFRWfJziTMyIKPIKKKMisF9XBhGRZDNgLLN4AYoCAJBIiRhGdaEAOH9/XGqodLpm/St230X+vt5nnr69qnTVW9XV/ett845VZGZSJIkSRosa4x1AJIkSZJGn4mAJEmSNIBMBCRJkqQBZCIgSZIkDSATAUmSJGkAmQhIkiRJA8hEQJIkSRpAJgKSJEnSADIRkCRJkgaQiYB6JiJmRURGxAMRsWWH+fMi4qoxim33KrY3jMX6hysitoqIMyLiziruE1ZRd35E/LTH658bEfPbyjIi5vRyPV3G0vrsWtPyiLgtIn4SETv1ed0HRMSh/VxHr0XE7Ih4bY+XuUdEXB4R91efQU+XPx5U+/x9I3j9vLb99KHqu/m1Tr+HE1ntt77R9y8i5kRE9jim1nY/ssO8EcXbCxHx04i4KyI27zBvo4i4NSIuioieHJdFxHur9/ycESxjm4j4UkRcFxFLI2JJRFwZEZ+MiBm1et+LiGvaXvvxiNh3JO9Bo8NEQP0wGfjUWAcxwX0O+BvgHcCLqudj7UXAV8dw/bOrGHYH/gXYFbggIrbp4zoPACZUIkDZTj07UI+IAL4PPAS8mvIZXNCr5T/O3EDZPi8C9gCOA/YFfhkRU8YysHHmq5Rt1A9HRsRGfVr2SLwTeJjOv6EnAlOBmZn5yKhGNYSIeD3we2Bv4EvAK4FXAacAbwD+q1b9o8D+bYv4OGXf1zi35lgHoMels4ADIuIzmfn7sQ5mNEXEOsADmTnSs13PAf4nM0/vQVg9kZmXjnEI19Vi+GVE3AWcCrwF+MTYhTV8ETElM5eMdRxdehKwEfBfmXleLxbYw+/JeLO07XtyYUQ8AHwNeDFw9khX8HjYdpm5AFjQh0WfSzlR8P+AD/Vh+Y1l5sKIOBj4z4h4T2aeDBARrwPeDBycmX8e6XoiYm1g+QiX8QzgW8CVwJ6ZeW9t9nkR8e/UTjb0Im6NHVsE1A/HAXcAn15Vpar7S0bErA7zVuiG0mpKjojtI+IHEXF31W3m+IhYMyK2jYizIuLeqjn+8CFW+4TqNQurps4LIuL5Hda/U0T8uFrHAxHx24h4Y1udVnPz3hFxSkTcBiyhtIgM9Z63iIhvRcTiiFgWEVdHxIdazcGtbjDA04FX1Jq7t1rVtmxbR2u7fjgiDouIGyPivoi4JCJ26VB/VkT8qRbP24ZYbvtnsmlEnBQRf6yWvzgizo+Il4wknmG4vHp8YodY94yI8yLinqo5+6KI2KOtzqYR8R8RcXP13m+r6u1ZzZ9HOQu2Ze1zyGpeq7vS7kO811m1srnV+31uRJwdEfcC51Xz9oqI/46IBdV+9ueIODkiNmlbbmv/3y4ivlvt/4uq/W6DWr0E1gVm1mKeV82bEhGfqbb/A9W+fXlEvHmoDVx93q0Dtk9Xy5tfm//iajvfW23niyPilW3LaPI9Wb8W64MR8deIOCEi1m2r976IuLDa9+6P0m3h8IhYq8My96livbuK9eqIOKpDvadHxM+qz+zmiPhsRAwZaxfurh4falvPiLddl8vo2A2ntuytamWTq/e7sFrehRGxY5Tf1Lkd3tvUKF1Hbo+IOyLitIh40uo2SKeYqnX8tPqcfhPl9/maiHjH6pZX8ydK0vW+6KI7Vqzmd77aDx+OiI/UyjaJiEeq/WjNWvnno/yGxFDry8zvA98DPhPlt2Jj4MvAOZn5pbbYdojHuhMtrbbJAW119qk+w/2r9d8KPACs1P2oqr95RFxR7ftbr2LTfARYB3hvWxLQeh+PZOZpteU+2jUoIp5QfbaTgPfEY79DZ0XEM6pt98EOse1d1XvVKuJSH5gIqB/upXQN+ruIeHmPl/19SnPlfsBXgA9Sus2cDpwBvA44n3LQ8voOr/9X4KmUZtp3Us52zouIp7YqRMTLgIuAacB7gdcAv6OcyZnVYZmnUP7Jv5XSZPpQhzpExKbAxZSm1o9RulmcC3yG0jQM8BtKk/nCKoZWN4NbV7VRhvA+YC9K15Z/pBwg/ixWPHCcBXwduJqyTT9VxdbN59Zqfv8k5YD57ZSuEfOi7QC523iGqfWP7Np6YUS8hXLm9R5gJvBG4E7g57FiMvBNylmtf6Z8Ju+kfB4bV/MPpnwGC3nsc2janWFt4MeUffM1PNaC8TTgEuCgKoZ/pnQJ+1Wng1ngR9X73Q84ltJ1qd5t7EXAUuBntXgPruYdX63n88A+lP31B7X328lXgdb36AvV8l4HEBG7Ve9nA+BAylnNe4GfRER7NwHo/nsyhdL1aGYV6ysoJxVmAT9uO9B6GvCdapn7Ug4CPwKc3LbMA6ttsgblO/2qatlPaVv9WpTP6TzK53QK5TfmiE6xDhH/mtU0JSJeSOkicQPlu9+qM+Jt12AZ3fg65fv5dcr7/xGlC8i0Iep/tYrrAOBwytn4bzVcN8AOwGcp+/RrgCuAr0XES4exjDmUM+L/sqpK3fzOZ+Y9wP8Ce9ZeugewjNKV54W18j2B87toqXkf5XM6BTiJ8tuwQrITEc+tYtumqv8G4Hrg2xHxTx2W+VlgE8pv2GuA/+vwfp8PXFrN2zUzb1xFjHsDN2Xmb1fzXjpZRvmdWE7Zd1q/Q4dm5rWUHgMHd0iY3g/Mp/wf12jKTCennkyUf9QJ7ET5cbue8iMa1fx5wFW1+ltV9Wd1WFYCc2rP51Rlh7XV+21V/rpa2ZrAYuBHtbLdq3q/bsVTlW8JPAh8pVZ2NeWAfM22df0EuAVYo+39ntrl9jmmqv/CtvKTgEeAZ9TK5gM/7XK5K9StbdcrgEm18p2r8jdVz9cA/rqKbTJ/VZ9JhzgmVdv+XOC04caziuW2Prs3VstfhzI+4BrgD8C0Wt0plNaoH7ctYw3KP/nLamX3Ap9bzbp/2r4d2mLava18pX0amFuVvX0164rq/W1R1X91h/3/I22v+SLlwL/++d0HzO2w/Csp3XuG+71uvacPt5VfAiwC1mvbB64Ebuax7/0shvc9OZJyELFTW/l+1XJeMcTr1qi231spfbE3rMrXo5yV/2V9O3V4fetz+oe28jOAa7qIe171+vbpT8Aze73thrGMOUB2eH1r2VtVz59dPT+2rd6bqvK5HV77xba6H6nKZ6xmW60UE+V3bCmwRa3sCZTv85e72P4JnFj9/alqH9q+Ld6davW7/Z3/F6pWmOr5V4AzKSekPl6VPala/ru63MdfUds/3tJh/n8B97dvR0qCejewbvV8n2oZP++wjPdW854D/D3l9+7bwNqriS2qbfeLbt5L9Zrv0fYdoXwHV/rcajHvUyvbqlrn4d2u06l3ky0C6ovMfJAygGgnygFcr7RfHedqyo/KmbV1Pwz8mXJA2+47Wf3yVHVvopypexmUbgHAMyk/mPWze2tSzihuBmzbtswfdRn7y4E/Zub/tJXPpfz49rr15IzMrPcVvaJ6bG2XbSn/wIbaJqsV5coUv4nSD/phytnBPYBnNYhndf6zWv4Sytmy9YFXZuZdtTq7UloqTm377NagnInaOR7rXvI/wKyI+GhE7DLEGfheWmk/iYjpEfHliLiZx7bfTdXsTtvwx23Pr6AcLE3vYv3/Q+ludmyUrk3rdB/6SnGvS2m5+GFmPnqlnerz/SblTHvT78m+wFXA79o+w59TJV+1OJ5fde24g3Ig8RDwDcoB8TOqartS9pWT6vv5EJJyIFh3Bd3vo9dTEtydKWdBD6Ac3J4X1aD2Xmy7hstYnd2qx++3lf+Qsm920ml/hO63V7vfZeZfWk8y8wFKC9hwl3ccpRWwY/fUYf7On8djJx+gnPk/h3LCY69aGVXZamXmmZSz89dlZqcWlJcDZ2XmwrbyUyn78s5t5av6br2b8jl9gZJ0PNhNjH30c8pJnPfVyg6mnHz62phENOBMBNRP36OccTm6hwdZd7Y9fxBYUv3DaC9/QofXt/+wtspa3SNa/c0/QzmoqE8nVfNW6L9N9912Nh6i7i21+b10R/1JZi6r/mwdALbWN9Q2WaWIOIxyNYnLKGdrd6H8gzqrto7hxLM6R1TL3w04mvJZnR4r9t9ufX4/ZOXP7whKwtXq0rQ/5R/rOylnV++MiG9E7bJ4PbQkSzeDR0UZF3I2pevNcZQE6oWU7QhdbENKM/xQddv9E+XA6LXALyjv9/RodtWlDSnbcjj7c7ffkycC27Py53dvtc5NoIy3oZzlfzJwCPASyv7ROsBobZNNq8duBqd2+i1ZRuffkk4eyMzLq+nSzPwu5ezvZpRuX9CbbddkGavTqr+oXlidWGnf71pGsj92s7zWMoe1vOq79ilgn6oLULvh/M5fTDn5sGeVQGzFY4nA30TEepRE4IZcdXebdsso/6dWEBGTKAf7vfpuvZnSivD1LhJhqjoLeKzrZU9Vy/8C8PcRsXVEPIHSNeq7mTnUfqY+8qpB6pvMzIg4gvKj+e4OVVr/cFcYiFcNoOqXTgd5M3jsH9Dt1eMxwGkd6kJp6q9b7Y9r5Q7KAUG71uC62zvM66fWex5qm6zOW4B5mXlQvTAipo40sCHckJmtAcIXRsRSyj/7D1D+ocNj2/ADlDNunSwCyMzbKf2hD60OKl9N6Xc/ndJ8vSod911WThJbOu0jz6H0iZ6Vmae2CquDjZ7LzPspYxM+ERFPpBygHks5A/7MYS7u/yjd2YazP3f7PbmdchZ9qEGireW+ljLO5PVVKxYAEfG8tvq3VY/t4wFGRWbeGhG3Uz5r6M22G84yHoAyELiWfMPK+2rr9+CJlC6DVK9bk96fpBgNX6IkiJ+u/q7r+nc+Mx+MiF9RDvYXAAsz88qIuKGqtzslie/JvVwyc3lE3EPvvltvpIwPujAi9srMbu7l83PgXRHxvMz8XRf1h+tUyni9gyitAxtTujlqDNgioL7KzHMpicDHKX116xZR/klt31b+mj6G9Ob6IKUoV5bYldK/l8z8E3AdsEPtzF77tNJVFLp0HvDsiHhBW/nbKD/kv2i43Kb+RDmTNNQ2WZ3ksTOArdduT/+uD97uOEoXsCNrycdFwF3As1fx+a10Fi4z/5KZJ1L21frnM9TZyPnVY/u+++phxN/6572srfw9w1hGJ6s9g5qZizJzLvBdYNsY5jXuq6TiMuD19S5GVSvHWygHTNcO8fLV+SllEPAdQ3x+81thVI+Pbr9qP35X2/IuppwRfW+HAYp9FxFPoRx0L4bebLthLmN+9di+r7ZfneXC6rF9oPEbmIAnDWvdU3cG/qFt3nB/588FdqS0fJ5bLeN+ysmGD1AO0LvqFtSl8ygX29i0rfxtlIsgXL7yS4Z0G6Xr642UCzns2MVrPkNJxr/c6cROFKu7V8mQv0PVtvsaJdk/BLg0M3/dRVzqgwn35daEdARlQOp0yuBO4NEWg28B74iI6ymDr15I6VfbL9OB/4qIr1CutvFJSjJyTK3Oe4AzI+LnlP77f6V0J3kW8ILMXOGfyjB8jvJDfkZEfJzSF/yVlP6RX8pyRYVRk5mPRMTHKFf+aG2TaZSBfKvtGkQ5YPtYRHyScpWXbSkJ342Mwm9LZj4UEbMpfZoPAT6VmfdFxAcoYwQ2onQRWkzpHrIDsGlmHhTlSkW/oFxx5hpKt5OdKS0B9TOEV1IOtg6i7MOPVAcJCyPiXOCoiPg/yme5B49dYacb11D6lB9bHaDeSTk422uVr1q9K4Hdo1yG71bg3sz8U0RcRvnMrqCcUX4WZWDtJdnsngZHURKnX0TEZyjdHA6mtHS8uZtuCEM4gXLAdWFEfK6Kdw3KIOq9gc9m5mXVuh8EvhsRx1G67xxE6TbzqGqf+BBlPz+32s8XUS7Ru0Nmvr9hnJ2sE49dEncSpXtF61LG9buD92LbdbuMn1H2ra9VvzsPUwbPrnCJycz8Q0R8F/hQRCynXJFoO8r1+O+mtEBMNN8FPkxp/Wo3nN/58yif5x6Uq1m1nEv5H5KU7dUrn6Ds6/Mi4mjKyY2Z1foPqQ6ku5aZd0XEXlRXLouIv8/Mi1ZR/9ooV1/7NmWszomUiy0EZf96J2Uw86ruc3MlpTvVKynft7sz87ra/BMpLbIbU5JXjZUcByOWnR4fEx2uzFCb9+1q3lVt5etTrsKwkHK1kx9TBoYlna8atEnb6+cC93VY3zxWvELR7tXr3wL8O+Xg8AHKWbAdO7x+e8rg1EWUf7C3Uv4ZvKeb97uKbbRFtS1ur5Z7DeUf1Rpt9eYz8qsGfbhD3RW2a1V2IOXs4TJKK8Hbq+06f1WvpVwZ6t8oZx+XUg6UX9P+2uHG06FO67N7wxDzL6Uc6GxQK3sp5aD3jmo7L6iev6GaP5nSXeD3lIOcJdVnMQeYUlvOhpRLbLa6YmRt3oxq3h2Uf9TfpJw1TFa+atBK+2g171k8dqnTOylJzeYdtvUcOu//rX1wq1rZDsCvKP+ok9J9C0qy+7/Veh6gJCHHAxuvZvuv6vN7MeV7cV+1DS8B9u32d2EV61yXcrWWa6r98i5KQnA88MRavX0pByhLq8/4OB67Ksnubct8BeV34b5q2/yB2lVKhvqcGOKqOx3qzWPFqwUtpxxc/gzYrR/brptlVPV2prSW3VdtpzmU7337vjOZcinKRdU2vYQyZuUu4PjVxcUQV9PqZpsyxG9etV3ndbH9k+qqQW3le9U+k/Z4V/s7X9ULypn1BJ5UK9+1Kvt1t/t22/u6ahXzn0e5YtXdlO/rb4B/bKvT2tc7feaPXjWoVvYESlfA+yk3CltdjNtQ7nNwfRXDEsoB/nHA5rV6na4atFO1/yyp4jirw/IvofzvX+WVjJz6O7UuLyZJkrSCiNiVkkT8Y2Z+Z6zj0eNDRDyZ0np8bGZ+fKzjGWQmApIkiar7yIsorXtLKa1LR1LOSm+fK19RSRqWiNicclPP2ZR97emZuXhsoxpsjhGQJElQuqjtTem7PZXShfFM4CiTAPXI+yjjZq6njGUxCRhjtghIkiRJA8jLh0qSJEkDyERAkiRJGkAmApIkSdIAGtjBwtUNfJ5EuZGQJEmS9HgyFbglVzEgeGATAUoSsGCsg5AkSZL65CmUmxt2NMiJwL0AN998M+uvv/5YxyJJkiT1xD333MPmm28Oq+n5MsiJAADrr7++iYAkSZIGjoOFJUmSpAFkIiBJkiQNIBMBSZIkaQAN/BgBSZIkTVzLly/noYceGuswRtVaa63FpEmTRrwcEwFJkiRNOJnJwoULueuuu8Y6lDExbdo0ZsyYQbk1VjMmApIkSZpwWknA9OnTmTJlyogOiCeSzGTJkiUsXrwYgM0226zxskwEJEmSNKEsX7780SRg4403HutwRt0666wDwOLFi5k+fXrjbkIOFpYkSdKE0hoTMGXKlDGOZOy03vtIxkeYCEiSJGlCGpTuQJ304r2bCEiSJEkDyERAkiRJGkAOFpYkSdLjwlZHnjGq65t/7CuH/ZpZs2Zx1113cfrppzNr1ixOPfVUANZcc0022mgjtt9+e9785jcza9Ys1lijv+fsbRGQJEmSxsg+++zDrbfeyvz58znzzDN52ctexiGHHMK+++7Lww8/3Nd12yIgSZIkjZHJkyczY8YMAJ785Cfzghe8gF122YU99tiDuXPn8s53vrNv67ZFQJIkSRpHXv7yl7PDDjtw2mmn9XU9tghIkqRR71s9UTTpAy71wjOf+UyuuOKKvq5jXLYIRMT8iMgO0xer+RERcyLilohYGhHzImK7sY5bkiRJ6oXM7Pt9EsZlIgDsDGxWm/aqyn9QPR4OHAa8v6q7EDgnIqaOcpySJElSz1199dVsvfXWfV3HuEwEMvO2zFzYmoB9geuBC6KkRocCR2fmaZl5FTATmAIcMHZRS5IkSSN3/vnnc+WVV7Lffvv1dT3jfoxARKwNvAU4PjMzIp4KzADObtXJzGURcQGwK3DyEMuZDEyuFdl6IEmSpDG1bNkyFi5cyPLly1m0aBFnnXUWxxxzDPvuuy9ve9vb+rrucZ8IAK8FpgFzq+czqsdFbfUWAVuuYjlHAZ/oaWSSJEkaNybi4O6zzjqLzTbbjDXXXJMNN9yQHXbYgc9//vPMnDmz7zcUmwiJwIHAmZl5S1t5tj2PDmV1xwDH155PBRaMPDxJkiSpO3Pnzl3h7/rz0TauE4GI2BLYE3h9rXhh9TgDuLVWPp2VWwkelZnLgGW1ZfcuUEmSJGmCGZeDhWveDiwG6hc3vpGSDLSuJNQaR7AbcPGoRidJkiRNUOO2RSAi1qAkAqdm5sOt8mrA8AnA7Ii4DrgOmA0sAb4zJsFKkiRJE8y4TQQoXYK2AE7pMO84YB3gJGBD4DJg78y8d/TCkyRJkiaucZsIZObZlAHAneYlMKeaJEmSNIDKIeFg6sV7H+9jBCRJkqQVrLXWWgAsWbJkjCMZO6333toWTYzbFgFJkiSpk0mTJjFt2jQWL14MwJQpUwbmipCZyZIlS1i8eDHTpk1j0qRJjZdlIiBJkqQJZ8aMco/ZVjIwaKZNm/boNmjKRECSJEkTTkSw2WabMX36dB566KGxDmdUrbXWWiNqCWgxEZAkSdKENWnSpJ4cFA8iBwtLkiRJA8hEQJIkSRpAJgKSJEnSADIRkCRJkgaQiYAkSZI0gEwEJEmSpAFkIiBJkiQNIBMBSZIkaQCZCEiSJEkDyERAkiRJGkAmApIkSdIAMhGQJEmSBpCJgCRJkjSATAQkSZKkAWQiIEmSJA0gEwFJkiRpAJkISJIkSQPIRECSJEkaQCYCkiRJ0gAyEZAkSZIGkImAJEmSNIBMBCRJkqQBZCIgSZIkDSATAUmSJGkAmQhIkiRJA8hEQJIkSRpAJgKSJEnSADIRkCRJkgaQiYAkSZI0gEwEJEmSpAFkIiBJkiQNIBMBSZIkaQCZCEiSJEkDyERAkiRJGkCNEoGI2CYi3hYRW7eVvzAiLomI+yLiDxHxmt6EKUmSJKmXmrYIfAg4BXi4VRARmwJnA38DrAM8C/hBROzQZAUR8eSI+FZE3BERSyLidxGxY21+RMSciLglIpZGxLyI2K7h+5EkSZIGStNE4MXAFZl5c63sHcD6wGcpicDrgEmUpGFYImJD4CLgIeAVwLOr5dxVq3Y4cBjwfmBnYCFwTkRMHe76JEmSpEGzZsPXbQZc2Fb2CmAZ8MnMfBD474i4FNilwfKPAG7OzLfXyua3/oiIAA4Fjs7M06qymcAi4ADg5AbrlCRJkgZG0xaBJwAPtJ5ExCRgJ+DSzLyvVm8+8OQGy381cHlE/CAiFkfEbyPiXbX5WwMzKF2RAMjMZcAFwK6dFhgRkyNi/dYE2HIgSZKkgdU0EbgZeGbt+UuAKcAv2uqtA9zfYPlPBQ4CrgP+Dvgy8PmIeFs1f0b1uKjtdYtq89odBdxdmxY0iEuSJEl6XGiaCJwHbB8Rh0TE9sCngAT+u63ecylJQ5O4fpOZszPzt5l5MvAVSnJQl23Po0NZyzHABrXpKQ3ikiRJkh4XmiYCxwB3AscDv6V0x/l+Zv6+VaG6gs/TKIN+h+tW4I9tZVcDW1R/L6we28/+T2flVgKgdB3KzHtaE3Bvg7gkSZKkx4VGg4Uzc0FEPA94F7Ap8Gtgblu151NaCL7fYBUXAdu2lT0DuKn6+0ZKMrAXJREhItYGdqMMNJYkSZK0Ck2vGkRm/hWYs4r53wK+1XDxnwMujojZlETihcC7q4nMzIg4AZgdEddRxhLMBpYA32m4TkmSJGlgNL2z8CkR8Y4u6s2KiFOGu/zM/F/KfQjeDFwFfAw4NDO/Xat2HHACcBJwOeXqRHtnpl1+JEmSpNVo2iIwq3pc3UH+3wIzKTcbG5bM/Cnw01XMT0qLxJzhLluSJEkadE0HC3drbWB5n9chSZIkaZj6lghUd/99AXBbv9YhSZIkqZmuuwZFxPltRft0KKsv92mUy3t+s2FskiRJkvpkOGMEdq/9nZSD/KHu4gvwEKWP/4eHH5YkSZKkfhpOIrB19RjADcAPgY8MUfdB4PbMfGgEsUmSJEnqk64Tgcxs3cyLiPgk8Nt6mSRJkqSJo+mdhT/Z60AkSZIkjZ7GdxZuiYgtgM2AyUPVycwLR7oeSZIkSb3TOBGo7iz8MWCLLqpParoeSZIkSb3XKBGIiLcDX62eXglcC9zXq6AkSZIk9VfTFoHDgIeB/TLzJz2MR5IkSdIoaHpn4W2AC00CJEmSpImpaSJwJ3YFkiRJkiasponAfwMvjIh1ehmMJEmSpNHRNBGYDdwDzI2IaT2MR5IkSdIoaDpY+LPAH4E3AHtHxOXAAiA71M3MPLDheiRJkiT1QdNEYFbt7w2APVZRNwETAUmSJGkcaZoIvKynUUiSJEkaVY0Sgcy8oNeBSJIkSRo9TQcLS5IkSZrATAQkSZKkAdQ4EYiIKRHx0Yj434i4KyKWDzE93MuAJUmSJI1cozECEbEB8EtgO2A58CAQwK3AjOpvgJt6EKMkSZKkHmvaInAk8BzgP4D1gR9S7hfwZGBdyuVFFwKXAU8deZiSJEmSeqlpIvBa4BbgnzLzAWo3EsvMBzLzG8CewOuAD484SkmSJEk91TQR2BL4TWY+VD1/BCAi1mpVyMw/AhcAM0cUoSRJkqSea5oIPAAsqz2/p3qc0VbvTmDrhuuQJEmS1CdNE4GbKa0CLddUj7u1CiJiTWBn4I6G65AkSZLUJ00TgV8Cz6muHgTwE+Ah4PMRcVBEvIoygHgrSvcgSZIkSeNI00Tge8DvgRcBZOYtwGxgGnAicDrwamARcMTIw5QkSZLUS43uI5CZv6JKAmplx0fERZQrBW0IXAt8PTPvHHGUkiRJknqq6Q3F1qfcN+DeenlmXka5d4AkSZKkcaxp16C7gLN7GYgkSZKk0dM0EbgbuKGXgUiSJEkaPU0Tgd8CT+tlIJIkSZJGT9NE4NPAzhHxhl4GI4GQyuUAACAASURBVEmSJGl0NBosDCwFvgr8Z0T8lHIfgb9Q7ji8ksy8sOF6JEmSJPVB00RgHpBAAK8C9l1N/UkN1yNJkiSpD5omAt+gJAKSJEmSJqCmNxSb1eM4VhARc4BPtBUvyswZ1fyo5r+bcvOyy4D3ZeYf+hmXJEmS9HjRdLDwaPgDsFltem5t3uHAYcD7gZ2BhcA5ETF1tIOUJEmSJqKmXYNGw8OZubC9sGoNOBQ4OjNPq8pmAouAA4CTRzVKSZIkaQJqlAhExCnDqJ6ZeWCD1WwTEbcAyyhdf2Zn5g3A1sAManc2zsxlEXEBsCtDJAIRMRmYXCuy9UCSJEkDq2mLwKwu6rSuKpTAcBOBy4C3AdcCTwQ+ClwcEdtRkgAoLQB1i4AtV7HMo1h53IEkSZI0kJomAi8bonwNYHPg74D9gc9R7jEwLJl5Zu3plRFxCXA9MBO4tFWt7WXRoazuGOD42vOpwILhxiZJkiQ9HjS9atAFq6nyjYg4EzgF+HGTdbSt7/6IuBLYBji9Kp4B3FqrNp2VWwnqy1hG6WYEQBlqIEmSJA2mvl01KDO/Rbnyz5yRLqvq3/8syoH/jZSrBO1Vm782sBtw8UjXJUmSJA2Cfl8+9Dpgp+G+KCI+ExG7RcTWEfE3wA+B9YFTMzOBE4DZEfG6iHgOMBdYAnynd6FLkiRJj199u3xoRKwBbA880uDlTwG+C2wC3EYZF7BLZt5UzT8OWAc4icduKLZ3Zt470rglSZKkQdDzRCAipgDPoFylZxvgp8NdRma+aTXzk9LlaM7wI5QkSZLU9D4Cy7upRjmb/5Em65AkSZLUP01bBG5m6Et1PkgZ1HsB8MXMXNxwHZIkSZL6pOnlQ7fqcRySJEmSRlG/rxokSZIkaRxqlAhExA0R8eku6h0TEdc3WYckSZKk/mnaIrAVsGkX9Tap6kqSJEkaR/rdNWhd4KE+r0OSJEnSMPXlhmLVzcS2BV4G/KUf65AkSZLUXNeJQId7B8yMiJmrexnwH8OOSpIkSVJfDadFoH7vgC2AJcDtQ9R9ELgF+DHw+cbRSZIkSeqLrhOB+r0DIuIR4AeZ+Y5+BCVJkiSpv5qOEXgZsLCXgUiSJEkaPU3vLHzBUPMiYn3gGcCCzDRZkCRJksahpjcU2zsiTomI57eVHwQsAi4DFkTEZ3oQoyRJkqQea3ofgXcC+wN/bhVExLOBLwCTgEuBe4APRsSrRhqkJEmSpN5qmgi8APhtZt5bK3s75XKhszLzb4HnA8uAg0cWoiRJkqRea5oIPBFY0Fa2J3AX8D2AzLwJuBDYrnF0kiRJkvqiaSLwMLB260lErAc8B/hlZj5Sq3cbsGnz8CRJkiT1Q9NEYD6wY+35KyljA85pq7cxcEfDdUiSJEnqk6aJwPeAzSPiRxHxT8BnKXcTPr1VISKCkizcMOIoJUmSJPVU00TgC8AlwOuAE4AZwJGZ+ddanZdTugX9YkQRSpIkSeq5pjcUWxIRLwFeAkwHfpeZ17VVWw58EPjJyEKUJEmS1GuNEgGAalDwkHcYzsx5wLymy5ckSZLUP40TgbqI2AbYBLgjM6/txTIlSZIk9U/TMQJExDoR8emIuAO4BvgVcGRt/tsj4jcR8bwexClJkiSphxolAhGxLqVb0Icpdw8+g3JX4boLgecB+48kQEmSJEm917RF4AhgJ+ArwNaZ+er2Cpl5PaWlYM/m4UmSJEnqh6aJwP6Um4q9LzOXraLeTcBTGq5DkiRJUp80TQS2AH6dmctXU+8eYMOG65AkSZLUJ00TgfspVwlana2BOxquQ5IkSVKfNE0Efg28MCI2H6pCRGwHPJ9yB2JJkiRJ40jTROBEYB3gtIh4evvMiNgS+Ea1/BObhydJkiSpHxolApn5E+BzwI7AnyLiKiCBvSPicuA6SmvAcdUdhiVJkiSNI41vKJaZHwLeBFwJPJtyH4EnAS8ArgfemplH9SJISZIkSb215khenJnfB74fEZsCWwKTgAWZ+ddeBCdJkiSpP0aUCLRk5m3Abb1YliRJkqT+a9w1qBsR8aqIuLSf65AkSZI0fD1pEaiLiKDcefgo4Dm9Xr4kSZKkkeu6RSAiNouI/4iImyJiafX45Yh4Yq3OfsDVwLeB5wK3Aof0PGpJkiRJI9JVi0BEbAJcBjyZcnUggM2BdwO7R8TOlPsFvKWavxA4Fjg5M5f1OmhJkiRJI9Nti8CRwFOAayiXDH0usCvwL8AWwC+AtwLLgNnAUzPz871IAiLiqIjIiDihVhYRMScibqlaJ+ZVdzKWJEmS1IVuxwi8ArgbeHlmLqqVXxoRtwGfp9xQbJ/MvLBXwVUtDe8GrmibdThwGDALuBb4KHBORGybmff2av2SJEnS41W3LQJbApe2JQEtP6weL+lxErAeZazBu4D/q5UHcChwdGaelplXATOBKcABvVq/JEmS9HjWbSIwhTLwdyWZubD684aeRPSYLwJnZOa5beVbAzOAs2sxLAMuoHRX6igiJkfE+q0JmNrjeCVJkqQJo5eXD324VwuKiDcBOwI7dZg9o3psb51YRGm5GMpRwCdGHp0kTRxbHXnGWIcwLs0/9pVjHYIkjbnhJAIzIuKlTeYPp8tQRGwO/Duwd2Y+sIqq2f7SDmV1xwDH155PBRZ0G5ckSZL0eDKcRODvqmm483OY69kRmA78ugwHAGAS8NKIeD+wbVU2gxW7K01n5VaCx4Io3YcevYpRbdmSJEnSwOn2AP1CVn22vZfOo1yetO7rlEuXfpoyFmEhsBfwW4CIWBvYDThilGKUJEmSJrSuEoHM3L3PcdTXdS9wVb0sIu4H7qiuEER1T4HZEXEdcB3l3gVLgO+MVpySJEnSRNbLwcKj6ThgHeAkYEPKXY/39h4CkiRJUncmRCLQ3iKRmQnMqSZJkiRJw9TtfQQkSZIkPY6YCEiSJEkDyERAkiRJGkAmApIkSdIAMhGQJEmSBpCJgCRJkjSATAQkSZKkAdT4PgIRMR04GHgpsBkweYiqmZlPa7oeSZIkSb3XKBGIiGcBFwAbA9HTiCRJkiT1XdOuQf8GbAKcBuwITM3MNYaaehatJEmSpJ5o2jXoJcCfgDdmZvYwHkmSJEmjoOnZ+gCuNAmQJEmSJqamicDlwNN7GYgkSZKk0dM0EZgDPDci3tjDWCRJkiSNksaXDwX+Hfh2RPw9cA6wAOjYVSgzLxzBeiRJkiT1WNNEYB7loD+AtwFvXU39SQ3XI0mSJKkPmiYC32CIs/+SJEmSxr9GiUBmzupxHJIkSZJGkTf7kiRJkgaQiYAkSZI0gEZy1SAiYgvgVcA2wFTK4OF2mZkHjmQ9kiRJknqrcSIQER8HPsaKrQqtRCBrzxMwEZAkSZLGkUZdgyJif8pNxW4G3k25jwDA3wEHARdQkoDjgZePOEpJkiRJPdW0ReBg4EHgZZl5U0S8GCAzWwnByRHxQeA44PSRhylJkiSpl5oOFt4euDgzb6qeJ0BEPDpGIDM/B/wJ+OiIIpQkSZLUc00TgcnAwtrzB6rHaW31fg/s3HAdkiRJkvqkaSJwKzCj9vyv1eN2bfWeAkxquA5JkiRJfdI0EbgSeGbt+TzK4OB/joj1ACLijcBLgD+MJEBJkiRJvdc0EfgJMCMi9gTIzIuAXwC7A3dGxB3AdyljB/6lB3FKkiRJ6qGmicC3gGcBv6mVvQ74D+BOYD3gj8BbM/OsEUUoSZIkqecaXT40M5dRrghUL7sHeG81SZIkSRrHmrYISJIkSZrATAQkSZKkAdRV16CIOJ8y8HdmZi6onncrM3OPRtFJkiRJ6otuxwjsTkkEptSedyuHUVeSJEnSKOg2Edi6evxr23NJkiRJE1BXiUBm3rSq55IkSZImFgcLS5IkSQPIRECSJEkaQF0lAhGxfATTw8MNKiIOiogrIuKearokIl5Rmx8RMScibomIpRExLyK2G+56JEmSpEHV7WDhm1n56j8BbFF7flf1OK1W9pcOr+vGAuBI4M/V85nAf0fE8zPzD8DhwGHALOBa4KPAORGxbWbe22B9kiRJ0kDpqkUgM7fKzK1bE/AM4ErKAft7gPUzc6PM3AhYvyq7uarzjOEGlZk/ycyfZea11fT/gPuAXSIigEOBozPztMy8ipIoTAEOGO66JEmSpEHUdIzAxyj3EnhJZn4lM+9rzcjM+zLzK8BLqzqfGEmAETEpIt4ErAtcQrl06Qzg7No6lwEXALuOZF2SJEnSoGiaCPwjcO6qLiNazTuXhmfpI+K5EXEfsAz4MvC6zPwjJQkAWNT2kkW1eZ2WNzki1m9NwNQmcUmSJEmPB00TgSfRXd//BDZruI4/Ac8DdgG+BJwaEc9uW3ZdrCamo4C7a9OChnFJkiRJE17TROBmYI+IWNUZ+BnAHjQ84M7MBzPzz5l5eWYeBfweOARYWFVpX/d0Vm4lqDsG2KA2PaVJXJIkSdLjQdNE4OuUrjUXRsT+EfHo1YciYs2I2J/SZ3894GsjD7MsGpgM3EhJBvaqrXNtYDfg4qFenJnLMvOe1gR4dSFJkiQNrG4vH9ruOOAFwH7Ad4BHImIRpWvODEqCEcB/Af823IVHxL8CZ1JaHqYCb6IMPN4nMzMiTgBmR8R1wHXAbGBJFYskSZKk1WiUCGTmcuAfIuLNwEHACynjBgAepFzd5+TM/HbDuJ4IfJMyvuBu4ApKEnBONf84YB3gJGBD4DJgb+8hIEmSJHWnaYsAAJn5XeC7VdegjSmtALdn5rDvJty23ANXMz+BOdUkSZIkaZhGlAi0VAf+qxqoK0mSJGkcaTpYWJIkSdIE1jgRiIhnR8TciLghIpZGxPIhphF1E5IkSZLUe426BkXEiyh3DV6nKroDuK9XQUmSJEnqr6ZjBI6hJAEnAJ/KzDt7F5IkSZKkfmuaCOwE/C4zD+tlMJIkSZJGR9MxAg8Cf+5lIJIkSZJGT9NE4FfAc3sZiCRJkqTR0zQRmA1sHhEf6mUwkiRJkkZH0zECLwC+DhwXEa8CzgEWANmpcmZ+o+F6JEmSJPVB00RgLuWgP4CXAi8Zol5U9UwEJEmSpHGkaSLwzwxx9l+SJEnS+NcoEcjMOT2OQ5IkSdIoajpYWJIkSdIEZiIgSZIkDaCuugZFxCkjWEdm5oEjeL0kSZKkHut2jMCsEawjARMBSZIkaRzpNhF4e1+jkCRJkjSqukoEMvPUfgciSZIkafQ4WFiSJEkaQCYCkiRJ0gAyEZAkSZIGkImAJEmSNIBMBCRJkqQB1O3lQyWNE1sdecZYhzAuzT/2lWMdgiRJE0pXLQIR8baI2LXfwUiSJEkaHd12DZoLvLP1JCJuiIhP9yUiSZIkSX3XbSLwCCt2I9oK2LTn0UiSJEkaFd0mAouB5/YzEEmSJEmjp9vBwucCb4mI64GbqrJ9IuL8Ll6bmblHo+gkSZIk9UW3icBhwDTgFcDWQAIzqml1sllokiRJkvqlq0QgM28HXh0RawGbAfOBHwIf6V9okiRJkvplWPcRyMyHgL9ExF+A+Zl50+peI0mSJGn8aXRDsczcqsdxSJIkSRpFI76zcERsBuwKPIkyHuBW4OLMvHWky5YkSZLUH40TgYjYFPgCsB8rX4b0kYj4EfCBzLxtBPFJkiRJ6oNGiUBEbABcCGwLLAXOpgwgBtgS2Bt4I7BDROySmXePPFRJkiRJvdK0ReBIShLwA+D97Wf9I2IT4ERKMnAEMHskQUqSJEnqrW7vLNzudcDNwFs6df2pLjf61qrOfs3DkyRJktQPTROBLYGLqsuJdlTNuwjYouE6JEmSJPVJ00RgKbBJF/U2qeoOS0QcFRH/GxH3RsTiiDg9IrZtqxMRMScibomIpRExLyK2G+66JEmSpEHUNBH4NbBbROw4VIVq3u7A5Q2WvxvwRWAXYC/KWIazI2LdWp3DgcOA9wM7AwuBcyJiaoP1SZIkSQOlaSLwOWAt4LyI+EREbBMRa1fTNhExBzgXmFTVHZbM3Ccz52bmHzLz98DbKV2MdoTSGgAcChydmadl5lXATGAKcEDD9yRJkiQNjEaJQGb+DPh/wHrAx4FrgCXVdA3wMWAq8NHMPLMHcW5QPd5ZPW4NzKBctrQV0zLgAsrNzVYSEZMjYv3WVMUnSZIkDaSmLQJk5jGUrjvfotxD4KFqmg98E3hRVWdEqrP/xwO/qs78Q0kCABa1VV9Um9fuKODu2rRgpLFJkiRJE1XjOwsDZObllC45/XQisD3w4k4htD2PDmUtx1ASipapmAxIkiRpQI0oEei3iPgC8GrgpZlZP2hfWD3OAG6tlU9n5VYC4NGuQ8tqy+5tsJIkSdIE0rhrUD9VlwY9EXg98PLMvLGtyo2UZGCv2mvWplxt6OJRC1SSJEmaoPrWIhARRwObAZmZBw7z5V+kXP3nNcC9EdHq9393Zi7NzIyIE4DZEXEdcB0wmzJY+Tu9eQeSJEnS41c/uwa9HtiW0md/uInAQdXjvLbytwNzq7+PA9YBTgI2BC4D9s7MexvEKkmSJA2UfiYCJ9Ld3YdXkpmr7cCfmQnMqSZJkiRJw9C3RCAzv9ivZUuSJEkamXE5WFiSJElSf/UsEYiIqRGxXq+WJ0mSJKl/RpQIRMQ+EfGziLgbuAu4OyLuiYgzImKf3oQoSZIkqdcaJwIRcTxwBrAP5S6991TTesArgDOqOpIkSZLGmUaJQETsDxwK3Ab8E7BhZm6YmRsC04APAIuBQyLijb0KVpIkSVJvNG0ROBh4AHhpZp6YmXe3ZmTmPdUVg3YDllV1JUmSJI0jTROBHYDzM/PaoSpU884HntdwHZIkSZL6pGkisDZwfxf17q/qSpIkSRpHmiYC1wO7RcSUoSpU83ar6kqSJEkaR5omAt8HpgOnRcRT22dGxNOA04BNgf9sHp4kSZKkfliz4es+A7wG2Bv4U0T8DzAfSGBr4IXAJOBy4LMjD1OSJElSLzVKBDJzaUTsDhwDvAN4UTW1LAVOAY7KzKUjDVKSJElSbzVtESAz7wM+EBFHADsCT6pm3QL8OjOX9CA+SZIkSX3QOBFoqQ74f9mDWCRJkiSNkqaDhSVJkiRNYF21CETE4SNZSWYeN5LXS5IkSeqtbrsGHUu5IlA3onqs1zcRkCRJksaRbhOBf6b7RADgicBMYJ1hvk6SJEnSKOgqEcjMOd3Ui4iNgSOAt1KSgPuBLzYNTpIkSVJ/jPiqQQARsRHwEeB9wLqU+wh8BjguM2/vxTokSZIk9c6IEoGI2BD4MPB+YColAfgc8OnMvG3k4UmSJEnqh0aJQERMAz4EfICSACwDTqAkAIt6F54kSZKkfhhWIhARGwCHAYfwWALwBeDYzFzY+/AkSZIk9UO39xFYH/ggcCiwASUB+CJwTGbe2r/wJEmSJPVDty0C8ykJwIOUBOBfTQAkSZKkiavbRGAa5X4AawIHAgdGxKpf8ZjMzHUbxCZJkiSpT4YzRiCASdUkSZIkaQLr9oZia/Q7EEmSJEmjxwN8SZIkaQCZCEiSJEkDyERAkiRJGkAmApIkSdIAMhGQJEmSBpCJgCRJkjSATAQkSZKkAWQiIEmSJA0gEwFJkiRpAJkISJIkSQPIRECSJEkaQOMyEYiIl0bETyLilojIiHht2/yIiDnV/KURMS8ithureCVJkqSJZlwmAsC6wO+B9w8x/3DgsGr+zsBC4JyImDo64UmSJEkT25pjHUAnmXkmcCZARKwwL0rBocDRmXlaVTYTWAQcAJw8qsFKkiRJE9B4bRFYla2BGcDZrYLMXAZcAOw61IsiYnJErN+aAFsPJEmSNLAmYiIwo3pc1Fa+qDavk6OAu2vTgt6HJkmSJE0MEzERaMm259GhrO4YYIPa9JQ+xSVJkiSNe+NyjMBqLKweZwC31sqns3IrwaOq7kPLWs/bxx5IkiRJg2QitgjcSEkG9moVRMTawG7AxWMVlCRJkjSRjMsWgYhYD3h6rWjriHgecGdm/iUiTgBmR8R1wHXAbGAJ8J3Rj1aSJEmaeMZlIgDsBPyi9vz46vFUYBZwHLAOcBKwIXAZsHdm3juKMUqSJA2krY48Y6xDGJfmH/vKsQ5hWMZlIpCZ8yiDf4ean8CcapIkSZI0TBNxjIAkSZKkETIRkCRJkgaQiYAkSZI0gEwEJEmSpAFkIiBJkiQNIBMBSZIkaQCZCEiSJEkDyERAkiRJGkDj8oZig8g79HU20e7QJ0mSNFHYIiBJkiQNIBMBSZIkaQCZCEiSJEkDyERAkiRJGkAmApIkSdIAMhGQJEmSBpCJgCRJkjSATAQkSZKkAWQiIEmSJA0gEwFJkiRpAJkISJIkSQPIRECSJEkaQCYCkiRJ0gAyEZAkSZIGkImAJEmSNIBMBCRJkqQBZCIgSZIkDSATAUmSJGkAmQhIkiRJA8hEQJIkSRpAJgKSJEnSADIRkCRJkgaQiYAkSZI0gEwEJEmSpAFkIiBJkiQNIBMBSZIkaQCZCEiSJEkDyERAkiRJGkAmApIkSdIAMhGQJEmSBtCETgQi4uCIuDEiHoiIX0fES8Y6JkmSJGkimLCJQETsD5wAHA08H/glcGZEbDGmgUmSJEkTwIRNBIDDgK9l5lcz8+rMPBS4GThojOOSJEmSxr01xzqAJiJibWBH4Ni2WWcDuw7xmsnA5FrRVIB77rmnHyEO2yPLlox1COPSePl8xhP3lc7cVzpzf+nM/WVl7iudua905v7S2XjZX7qNIzKzz6H0XkQ8Cfgr8LeZeXGtfDYwMzO37fCaOcAnRi1ISZIkaWw9JTP/OtTMCdkiUNOexUSHspZjgOPbyjYC7ux1UBPcVGAB/P/27jxKrrLO//j7QzSRzQUQASFsAuoQFJBNEBgQUBEOYBQRZVFAGUEBx4XRn7I4I4tMBBSYBZRFjqjDJiKggCiyCAKCRlFICCprIAghMwnL5/fHc5tUKtVJNwl97+36vM7p01XPvVX9Iaform/d5/k+rAo8VXOWaLa8VmI48nqJocprJYYjr5fBLQs8sKAT2loITAeeA1bqGl8ReLjXA2zPBmZ3DTfj+k2DSBq4+ZTt/PvEoPJaieHI6yWGKq+VGI68XhZoof8erVwsbHsO8Btgh65DOwA3zP+IiIiIiIjo1NYrAlCm+Zwr6VbgRuAgYDxwRq2pIiIiIiJaoLWFgO0LJC0PfBlYGfgd8B7b0+pN1nqzgaOZfxpVRLe8VmI48nqJocprJYYjr5dF0MquQRERERERsWhauUYgIiIiIiIWTQqBiIiIiIg+lEIgIiIiIqIPpRCIiIiIiOhDKQQiIiIiIvpQCoGIiIiIiD7U2n0EYvGRtKTt/x3k2Mq2HxzpTBER0V8kvQuYafv66v4ngQOBycAnbc+oM1/UR9IMYEj97m0v9xLHGVWyj0Ag6Y/Ah2zf1jU+ETjd9mvrSRZNJWkJ4A3AinRdWbT9i1pCRUSrSboL+LztyyVNAG4B/h3YDviD7f1rDRi1kbRvx93lgS8BVwI3VmNbADsBx9qeNMLxWi2FQCDpVMqnLkcBxwNLA98E3g98wfap9aWLppG0OXA+sDqgrsO2PWbkU0UTSXod8HVge0rROM/rJa+V6CRpJrC+7fskHVXdnihpI+By2yvVmzCaQNL/ANfa/mbX+CHAO23vVk+ydsrUoMD2oZJ+DHwb2BlYBXgS2MT25FrDRROdAdxKea08yBAv10Zf+g4wHjiWvFZi4eYAS1W33wmcU91+HHhlLYmiiXYCPt9j/ErguBHO0nopBGLAVcCFwMHAs8AuKQJiEOsAE23fU3eQaLytgHfYvqPuINEK1wP/LulXwKbAntX4usBfa0sVTfMYsDtwYtf4btWxGIYUAoGktSlTPVaiVNrbAJdIOgX4ou1n6swXjXMzZX1ACoFYmL8w//SxiMEcApwGTAQOtv23avzdwBW1pYqm+QpwpqRtmbtGYHPgXcABdYVqq6wRCCQ9BfwY+ITtJ6qxt1Muyz5le8M680WzSNod+Crl05i7gHkKRdt31pErmkfSjsBngI/bvq/mOBExSkjaDPgU8CbKhw2TgVNs31xrsBZKIRBI+ojtc3uMLwt8w/bHaogVDSXp+R7DpvwyzmLheEHV8m8pytXnWcxfNKbNX8wjHckiRlYKgYgYFkmrL+i47WkjlSWaravl33xsnz1SWaL50pEshioF4+KTQiAAkLQusC3z/09l28fWEioaSdLStp+uO0dEjC6S7gD+RJkDPl+XKdt/ryNXNEsKxsUrhUAg6UDgdGA68BDz/vK17Y1qCRaNVPX6/j5w1sAOoBELI2lJ4OWdY7afrClONJCkp4G3pCNZLEgKxsUrhUAgaRpwmu3j684SzSdpF2A/4L3ANOAs4BzbD9SZK5pH0tKUTQo/QNkNdB755C46SboGOMF2OgTFoFIwLl5LLPyU6AOvAX5Qd4hoB9s/sv0+ysZzpwN7AdMkXSZpD0lpSxwDTgC2A/4JmE1p7fcV4AFgnxpzRTOdCpwkaT9JG0vaoPOr7nDRGAMtrGMxyBWBQNKZwC22z6g7S7STpEMp7UTHUqaYnQEcZ3tWrcGiVpLuB/ax/XNJTwIb2b5H0keAvWy/p+aI0SDpSBZDkRbWi1c+uQsoG0MdWy3A6fU/1Sm1pIpGk7QS5VPd/YHxwA+BMylXCr5A2eBlx9oCRhMsB0ytbj9Z3Yeyg+zptSSKJluz7gDRCv9TfT+rY+yFghFIwTgMKQQC4CBgJmVH4W26jhlIIRAvkLQH5c3/TpRNXL4FnDewGV11zh3A7fUkjAaZAqxBWUsymbJW4NfALsATgz8s+lFaD8cQpWBcjDI1KCKGRdLfge8B/237lkHOWRL4nO2jRzRcNIqkw4HnbJ8i6R8pO5iPoXwIdYTtk2sNGI1TTRv7BOXN3ha2p0k6DJhq+5J600WMPikEYh6SBGUyZt1ZopkkLZW5//FiSBoPvA241/Zv684TzSLpYOAY+pi62QAAFU9JREFU4BvAF4H1bU+RtB+wr+1/rDNfNIukN1OmpY7tHLd9aT2J2imFQAAgaR/gs8A61dCfgBNtn1tfqmgKSa8c6rnpDR8Dqt8rF9ie3TU+Fvig7XPqSRZNJGky8C+2L5b0FKVF5BRJ6wM/t71CzRGjASStBVwETGDu2gCq22lLPExpHxpIOoKycO9yyhzePYErgDOqS/sRTwAzFvI1cE7EgG8Dr+oxvmx1LKLTmvReWzQbWHqEs0RznUxpQvA6YBbwD8DWwK3AtvXFaqcsFg6AQ4GDuz6du0TS74GjgEm1pIomySX5eDEGunh0WxXI7p/RbSrwVsri8k7vpiw2jwDYAtjO9qNVy9nnbV8v6UhKc5MN643XLikEAmBl4IYe4zdUx6LP2b5u4Laksbbn9DpPUi7dB5JupxQABq6W9GzH4TGUT36ze2x0OxH4lqRXUIrITSXtBRxJ2YwuAsrvkJnV7emUltV3UwrI9eoK1VYpBALKPgIfAP6ta3xP4M8jHyca7vuS9rA9z+Y/kl4HXA2sX0+saJCLq+9vBa5k7h9tgDnAfcztBR4BgO1vVzuTnwAsBZwP/A34tO3v1RoumuR3wAaU9sQ3A5+TNIfSCn1KncHaKIuFA0nvAy4Afgb8ivIp3lbA9sAHbF9UY7xoGEk3A5Nt798xtjJwDfB72xNrCxeNImlf4Hvdi4UjFqa6uriE7UfqzhLNImknYGnbF1YLhy8D3gg8Buxp+5paA7ZMCoEAQNLGwOHAmyiXZCcDJ9nOplAxD0nLA78ArrJ9uKTXU4qA31I6wTy/wCeIviFpCrCJ7ce6xl8N3GZ7rXqSRVNVVwS2BdYGzrf9lKRVgCdtz1zgg6NvSVoOmJHW58OXQqDPVb909wautP1Q3XmiHSStClxPaeG2M3AbsLft52oNFo1SLeRbqftT3Woa2f22x9WTLJpI0uqUtSPjgXHAulX70G8Ar7D9iVoDRoxCWSPQ52w/K+l0ypWAiCGx/VdJO1CKgZ8CH8knMTFA0q4dd3eqdqMeMIYy7fC+EQ0VbXAypQXkWyjTPAZcBPx3LYmiESRdONRzbe/xUmYZbVIIBJTFNhsyf8u2CAAkzaB3G8ilgF2Ax6pNqbG93AhGi2YaWCxs4OyuY89QioDPjGSgaIWtgC1tzxn4fVKZBry+nkjREGk3/BJJIRAApwEnVdM9fgM83XnQ9p21pIomOazuANEetpcAkDSVskZges2Roh2WoFwx6rYq8NQIZ4kG6WxOEYtX1gjEwDzewTjbdUdExEtN0gXA320fJOkpSovIR4FLKGtK8mYwkLQk5f3rrOr+6sDulG52V9UaroVSCMTA/0SDsp0pQzEPSWOA3ShrS0zpMnVpFgtHN0lLA9tQFoCO7Txm+5RaQkUjVd2BrgWeA9ahrBdYh7Jp1NZpJRoAkq4CLrR9RtWB7G7K/iQrAEfYPr3WgC2TQiCQtPxAez9JqwEHAktS3tj9stZw0TiS3gBcTpmzezel3ey6wF+AnW3fW2O8aBBJG1JeK0sBSwOPU/5YzwIeSfvQ6FZ92rsXsBFlqtBtwHdt/2+twaIxJE0HtrH9e0kHAIdS1jm+DzjGdpqfDEMKgT4maQLwI2A1yg7CH6S0blsaeL76PtH2xYM+SfQdSZdT3vzvbfvxamx54Dzgeds715kvmkPSz4E/AQcDT1C6wTxDea2cbHvInUAiIgAkzQLeaPt+Sd+nbGR5dPVB5t22l6o5YqukEOhjkn4CPAscD3wYeC9wFXBAdcqpwMa2N68nYTSRpKeBzW3f1TX+FuBXtpepJ1k0jaQngM1s313d3sL2HyRtBpxt+401R4wGkbTPgo7bPmekskRzSbqT0k72IuB3wLts31htjPpj2yvVGrBl0jWov20CbGf7Tkl3AAcBpw3sDCvpVOCmOgNGI80Glu0xvgxlnmbEgGeY23b2Yco6gT9QWgGOrytUNNbJXfdfTplWNocynSyFQAAcA5wPTAKutn1jNb4jcHttqVoqhUB/Ww54CMD2zOqT3sc7js+g9xu+6G+XAf8p6WPAr6uxzYAzgEtrSxVNdDvwNsr0oGuBYyStAHwEuGtBD4z+Y/s13WOS1gFOB04c+UTRRLZ/KOl6YGXgtx2HrqZcJYhhyNSgPla1DX2d7Uer+08BG9ieWt1/HfBA2odGp6pLw9mUjcSeqYZfRikC9rOdjV8CAElvA5a1fa2k11JeN1sB9wD72/7tAp8gghdeR+dlKlnE4pdCoI9VhcBPKFM9oLyxu4a5G4qNo8y9SyEQ86k+qRvozjDZ9j115omI0anqPnWd7VfWnSXqI2lIzQVs7/FSZxlNMjWov53ddf+8HudkTmb0ZPvPku6pbucThYhYJJJ27R6iTP84BPjVyCeKhsnV5pdArghExLBV3T0+S9nsB8oc8BNtn1tfqmiaanrh14HtgRUpb+xekKuN0anHLvem7Cx8DfAZ2w+OfKqI0S1XBCJiWCQdARwLfJPyKZ2ALYEzJK1ge1Kd+aJRvkPpDnQs8CBzOwhFzMf2EgDVepI5WW8U8dLLFYGIGBZJU4GvdPf0lrQvcJTtNetJFk1TNSB4h+076s4SzVY1IfhXYE9goHvQo8C3gWNtz6orW8RolisCETFcKwM39Bi/oToWMeAvdE0HiugmaTngRuD1wHcpe02I0ozgUGAHSVtRdqbezPYpdWWNGG2WqDtARLTOPcAHeozvCfx5hLNEsx0GHCdpjZpzRLN9mbJp2Nq2P277G7Yn2T4IeAMwFjiXsvN9pgtFLEaZGhQRwyLpfcAFwM8oawRM6Q2/PfAB29nQpY9JmsG8awGWplx9nsXcfScAsL3cCEaLhpJ0H/Bx21cOcvxdwOXA0baPHslsEaNdCoGIGDZJGwOHUy7dC5gMnGQ727v3uWqtyJDY7m5hHH1I0mzK1YC/DnJ8VeA+25nOHABIWhfYltKNbJ7ZLbaPqSNTW6UQiIghk/QyYG/gStsP1Z0nItpP0t+APW1fP8jxdwAX2F5lZJNFE0k6EDgdmA48xLxXIG17o1qCtVQKgYgYFkmzgDfZnlZ3lmg+SUtQ5nn3+uTuF7WEikaRdCblNbKD7Tldx8YBVwJTbH+0jnzRLJKmAafZPr7uLKNBCoGIGBZJ1wIn27647izRbJI2B84HVmf+7kHOhmIBL0z9uRWYDXwL+GN16M3APwHjgE1s319PwmgSSU8Cb7U9pe4so0EKgYgYFknvB44DJgG/AZ7uPG77zjpyRfNIuoOy6/RX6LGhWDaMigGS1gROA3ZkbtFo4KfAIbbvqStbNEt1BekW22fUnWU0SCEQEcMi6fkFHM6nvPECSU8Db8mbuBgqSa8B1qnu3mP78TrzRPNIOhI4AvgxcBfzdyPLPhPDkEIgIoZF0uoLOp61AzFA0jXACbavqDtLRIwO1e72g7HttUYszCiQVlwRMVwzbT8GIGk14EBgSeBS27+sNVk0zanASZJWovcnd5lGFhHDYnvNujOMJrkiEBFDImkC8CNgNcoOwh8ErqBsGPV89X1iFhHHgEGmkZkyBzzTyCLiRZM0FlgTuNf2s3XnaasUAhExJJJ+AjwLHA98GHgvcBVwQHXKqcDGtjevJ2E0TaaRRcTiJmkpyt+bgc0L17U9RdIpwAO2j6svXfukEIiIIZE0HdjO9p2SlgGeBDa1fWt1/I3ATbZfXWfOiIgYvSSdDGwJHEa5Kr1BVQjsChxte8NaA7ZM1ghExFAtR9nFEdszq44wnR09ZgDL1hEsmk3Sm4HxwNjOcduX1pMoIlpsN8pO1DdJ6vw0ezKwdk2ZWiuFQEQMR/clxFxSjEFJWgu4CJjA3LUBMPd1kzUCETFcrwUe6TG+NPmbNGwpBCJiOL4jaXZ1+xXAGdWVASi7f0Z0OhmYCrwTmAJsCiwPnAT8c425IqK9bgF2pqwTgLlv/g8EbqwlUYulEIiIoTq76/55Pc45ZySCRGtsQVlX8mjVQeh529dXGwKdAmQub0QM15HAFdWUw5cBn5b0D5TfN9vUmqyFUghExJDY3r/uDNE6Y4CZ1e3pwCrA3cA0YL26QkVEe9m+QdKWlKuK9wI7ArcBW9i+q9ZwLZRCICIiXiq/AzagTAu6GficpDnAQdVYRMSwVW/4913oibFQS9QdICIiRq2vMvfvzJeA1YFfAu8BPl1XqIhoL0nPSVqxx/jykp6rI1ObZR+BiIgYMZKWA2Y4f3wi4kWo1hutZPuRrvFVKLsML1lPsnbK1KCIiFisJJ01hHOw/dGRyBMR7SfpU9VNAwdImtlxeAywNfDHEQ/WcrkiEBERi1X1id004Hbm7h0wH9u7j1ioiGg1SVOrm6sDfwU6pwHNAe4Dvmz75hGO1mopBCIiYrGSdBrwQeB+4CzgPNuPL/hRERELJ+laYA/bM+rOMhqkEIiIiMVO0jhgD+CjwNuBHwNnAldlfUBERDOkEIiIiJeUpNWB/YB9gJcDb7Y9c4EPiogYhKRVgV2B8cDYzmO2j6glVEtlsXBERLzUXH2JtK2OiEUgaXvgUmAqZWPC3wFrUH6/3FZfsnbKL+SIiFjsJI2TtJekn1J2E54AHAKMz9WAiFgEXwNOsr0+8H/A+4DVgOuAH9QZrI0yNSgiIharrsXC36YsFn6s3lQRMRpIegp4q+17Jc0AtrL9e0lvAS6xvUa9CdslU4MiImJx+wSlCJgKbANsI83fRdT2HiOcKyLa72lgXHX7AWBt4PfV/RVqSdRiKQQiImJxO4eyJiAiYnG7CdgSmEzpRnaSpAmULmU31RmsjTI1KCIiIiJaQdJawDK275S0FPB1YCvgHuBw29NqDdgyKQQiIiIiIvpQugZFRERERCtImiJp+R7jr5Y0pY5MbZZCICIiIiLaYg1gTI/xccDrRzZK+2WxcEREREQ0mqRdO+7uJOnvHffHANsD941oqFEgawQiIiIiotEkPV/dHNilvNMzlCLgM7YvG8lcbZdCICIiIiJaQdJUYBPb0+vOMhqkEIiIiIiI6ENZLBwRERERjSZpM0nv7hrbR9JUSY9I+k9J4wZ7fPSWQiAiIiIimu4oYIOBO9VuwmcCPwOOA3YBjqwlWYtlalBERERENJqkB4FdbN9a3f9XYBvbW1X33w8cbfvNNcZsnVwRiIiIiIimew3wcMf9bYArOu7fAqw2oolGgRQCEREREdF0DwNrAkgaC2wE3NhxfFlKG9EYhhQCEREREdF0VwDHSXoH8DVgFvDLjuMbAPfWEazNsrNwRERERDTdl4ALgeuAmcC+tud0HP8ocFUdwdosi4UjIiIiohUkvQqYafu5rvHlqvE5vR8ZvaQQiIiIiIjoQ1kjEBERERHRh1IIRERERET0oRQCERERERF9KIVARETLSXKPrzmS/iLpu5Im1J2xCSQdVf3b7Fd3loiIJkj70IiI0ePsjtuvAjYGPgRMlPQu29fWEysiIpoohUBExChhe7/O+5JeDpwJfAQ4mbLhTkREBJCpQRERo5btZ4CjqrsTJL26xjgREdEwKQQiIka3hztuz3cVWNJqkv5D0jRJsyU9IulCSZv0OHeNao79zyW9UtJJkqZKekbSNzrOe5mkQyX9RtLM6uvXkg6WNKbH894nqeemNpK2rX7md3ocW1HSf0l6WNIsSbdJ+lBnzsH+USRNkHSppBmSnpZ0naS3D3Z+RMRolEIgImJ027j6Pt329M4D1SLi24CDgFnAhcCfgd2BGyS9f5DnXBK4DtgfuAO4FJhRPecY4BLgFOANwM+qrzcCpwE/kLTIf3skrQDcABwAzK4y/B04Fzh8IQ9/G3ATsB5wNeW/eWvgaknrL2q2iIi2yBqBiIhRSNKrgE2Bb1ZD/9Z1XMB3gRWArwFfdLXVvKSJwAXAmZJ+YbvzqgLV894IrGX7ia5jhwHvAe4C3mn7keo5VwaupRQZn6AUBYviOGBt4CJgL9uzq5+zPXD5Qh77SeDztk8YGJA0qcr+OWCfRcwWEdEKuSIQETFKdLYPBZ4ArgJeDXzI9qSu07cFJgBTgf83UAQA2P4hcDGwLOVT/14+1aMIAPhU9f2wgSKges4Hgc92nfOiSFoG2Bt4Fvj0QBFQ/Zyrge8t5Cmu7ywCKl+tvm+9KNkiItokhUBExOhxdsfX9yif2q8AnCBpm65z31F9v8D2cz2e69yu8zo9aPvW7kFJ44HxwEO2r+nxuMsoBcp6kl67sP+YBdgIeAVwk+2/9Dj+g4U8/qruAduPAY8BKy9CroiIVsnUoIiIUaK7fSiApA0p8/mvlPQm21OrQ6tU3+8b5OkGxlfpcez+QR6zwOe0bUnTKFcpVgEeHeR5Fmbg5/QqAhaUb8BfBxmfCSz/ohJFRLRQrghERIxitm8H/gMYBxzS65SFPUWPsf97EY95MefAgv9ODfYcWkw/OyJiVEshEBEx+g1cBVivY+yB6vuagzxm9er7g8P4OQt7TihTh7qfdw68MPe/22o9xgYeO77HscEeExERXVIIRESMfmtV35/uGPtl9X3PXr39gQ93nbdQtu+nTMtZSdJ23ccl7Qy8Brjbdue0oIE39uv2eNode4zdRmkZurmkVXscnzjUzBER/SyFQETEKFatETioutvZVvPnlBafawLHVO1EBx6zG7AHZc78d4b5I0+tvk/qXBAsaSXgxK5zBlxXfT+ysyiR9GHgg90/wPZTwPmUdW6TJI3teMy2wF7DzBwR0ZeyWDgiYpTo2n13LGV6z+aUD31+xNxOQAMLd/em9Pb/F2B3SXdQpttsSWnN+VHbDw0zxiRgO+DdwJ8lXUOZs789pR3pxcDpXY/5FmVvgYnAZEl3AusA6wMn03uDsC9QWqBOBDaVdAOwYjV2GmU9xJxhZo+I6Cu5IhARMXrs2/G1J2U3318AHwN2s/1858m276K04vwvYBnKm+r1KG/Wt7S9sDac86lake4KfBqYAuxEmd5zN2Ujr4k9cjxM6d9/GaV957spuwTvQNkxuNfPeQTYAjiLstPxbpSOP/szdx+Bx4abPyKin6hjD5mIiIjWk/R5ys7DX7B9fN15IiKaKlcEIiKilSRt1GNsa8pUp2eB7494qIiIFskagYiIaKsbJD0A/IHSEekNwIbVsS90bJ4WERE9ZGpQRES0kqSvADtT2qO+CngSuBX4pu0f1ZktIqINUghERERERPShrBGIiIiIiOhDKQQiIiIiIvpQCoGIiIiIiD6UQiAiIiIiog+lEIiIiIiI6EMpBCIiIiIi+lAKgYiIiIiIPpRCICIiIiKiD6UQiIiIiIjoQ/8fXrhBk5XjwS4AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 900x500 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(9,5), dpi = 100)\n",
    "# title\n",
    "plt.title('Number of Indian Resturants for each Borough in New York City')\n",
    "#On x-axis\n",
    "plt.xlabel('Borough', fontsize = 15)\n",
    "#On y-axis\n",
    "plt.ylabel('No.of Indian Resturants', fontsize=15)\n",
    "#giving a bar plot\n",
    "indian_rest_ny.groupby('Borough')['ID'].count().plot(kind='bar')\n",
    "#legend\n",
    "plt.legend()\n",
    "#displays the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### From the above Bar Plot, we can see that Queens has highest number of Indian resturants."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 900x500 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(9,5), dpi = 100)\n",
    "# title\n",
    "plt.title('Number of Indian Resturants for each Neighborhood in New York City')\n",
    "#On x-axis\n",
    "plt.xlabel('Neighborhood', fontsize = 15)\n",
    "#On y-axis\n",
    "plt.ylabel('No.of Indian Resturants', fontsize=15)\n",
    "#giving a bar plot\n",
    "indian_rest_ny.groupby('Neighborhood')['ID'].count().nlargest(5).plot(kind='bar')\n",
    "#legend\n",
    "plt.legend()\n",
    "#displays the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Borough</th>\n",
       "      <th>Neighborhood</th>\n",
       "      <th>ID</th>\n",
       "      <th>Name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>100</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Floral Park</td>\n",
       "      <td>527ffc0811d2d329d5e49abd</td>\n",
       "      <td>Jackson Diner</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>101</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Floral Park</td>\n",
       "      <td>4b647b56f964a520c4b62ae3</td>\n",
       "      <td>Usha Foods &amp; Usha Sweets</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>102</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Floral Park</td>\n",
       "      <td>4e4e3e22bd4101d0d7a5c2d1</td>\n",
       "      <td>Kerala Kitchen</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>103</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Floral Park</td>\n",
       "      <td>4b787c49f964a5209cd12ee3</td>\n",
       "      <td>Santoor Indian Restaurant</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>104</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Floral Park</td>\n",
       "      <td>4c0c01e0bbc676b00d6b4cd5</td>\n",
       "      <td>Mumbai Xpress</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>105</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Floral Park</td>\n",
       "      <td>4c76ff35a5676dcb72671721</td>\n",
       "      <td>Flavor Of India</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>106</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Floral Park</td>\n",
       "      <td>4df0f39dd4c04d0392c853ea</td>\n",
       "      <td>Sagar Chinese</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>107</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Floral Park</td>\n",
       "      <td>4c953a7672dd224bd8d1a191</td>\n",
       "      <td>Real Usha Sweets &amp; Snacks Inc.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>108</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Floral Park</td>\n",
       "      <td>4cc642ed306e224b5bf2a76c</td>\n",
       "      <td>Shahi Darbar</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>109</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Floral Park</td>\n",
       "      <td>51d84192498ea979a3c4f13d</td>\n",
       "      <td>Sunshine Grill &amp; Restaurant</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>110</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Floral Park</td>\n",
       "      <td>4e6bfe1c7d8b2c711b17bbe5</td>\n",
       "      <td>Surya sweets and snacks</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Borough Neighborhood                        ID  \\\n",
       "100  Queens  Floral Park  527ffc0811d2d329d5e49abd   \n",
       "101  Queens  Floral Park  4b647b56f964a520c4b62ae3   \n",
       "102  Queens  Floral Park  4e4e3e22bd4101d0d7a5c2d1   \n",
       "103  Queens  Floral Park  4b787c49f964a5209cd12ee3   \n",
       "104  Queens  Floral Park  4c0c01e0bbc676b00d6b4cd5   \n",
       "105  Queens  Floral Park  4c76ff35a5676dcb72671721   \n",
       "106  Queens  Floral Park  4df0f39dd4c04d0392c853ea   \n",
       "107  Queens  Floral Park  4c953a7672dd224bd8d1a191   \n",
       "108  Queens  Floral Park  4cc642ed306e224b5bf2a76c   \n",
       "109  Queens  Floral Park  51d84192498ea979a3c4f13d   \n",
       "110  Queens  Floral Park  4e6bfe1c7d8b2c711b17bbe5   \n",
       "\n",
       "                               Name  \n",
       "100                   Jackson Diner  \n",
       "101        Usha Foods & Usha Sweets  \n",
       "102                  Kerala Kitchen  \n",
       "103       Santoor Indian Restaurant  \n",
       "104                   Mumbai Xpress  \n",
       "105                 Flavor Of India  \n",
       "106                   Sagar Chinese  \n",
       "107  Real Usha Sweets & Snacks Inc.  \n",
       "108                    Shahi Darbar  \n",
       "109     Sunshine Grill & Restaurant  \n",
       "110         Surya sweets and snacks  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "indian_rest_ny[indian_rest_ny['Neighborhood']=='Floral Park']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### We can see that, Floral Park in Queens has the highest number of Indian Resturants with a total count of 11."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we will get the ranking of each resturant for further analysis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                         ID        Name  Likes  Rating  Tips\n",
      "0  4c0448d9310fc9b6bf1dc761  Curry Spot      5     7.6    10\n",
      "( 1 / 151 ) processed\n",
      "                         ID                         Name  Likes  Rating  Tips\n",
      "0  4c194631838020a13e78e561  Melanies Roti Bar And Grill      3     5.8     2\n",
      "( 2 / 151 ) processed\n",
      "                         ID                  Name  Likes  Rating  Tips\n",
      "0  4c04544df423a593ac83d116  Cumin Indian Cuisine     13     6.1     9\n",
      "( 3 / 151 ) processed\n",
      "                         ID         Name  Likes  Rating  Tips\n",
      "0  551b7f75498e86c00a0ed2e1  Hungry Bird      8     6.9     3\n",
      "( 4 / 151 ) processed\n",
      "                         ID                         Name  Likes  Rating  Tips\n",
      "0  4c194631838020a13e78e561  Melanies Roti Bar And Grill      3     5.8     2\n",
      "( 5 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 55dfa36a498e164ef19bef7b\n",
      "( 6 / 151 ) processed\n",
      "                         ID       Name  Likes  Rating  Tips\n",
      "0  4b5a4dc8f964a520a2bb28e3  Taj Mahal     38     8.4    26\n",
      "( 7 / 151 ) processed\n",
      "                         ID          Name  Likes  Rating  Tips\n",
      "0  4af0d31bf964a5207ddf21e3  Pak Nasheman      9     7.5     4\n",
      "( 8 / 151 ) processed\n",
      "                         ID          Name  Likes  Rating  Tips\n",
      "0  52213c4211d295d4c57a607c  Ashoka Grill      8     7.0    14\n",
      "( 9 / 151 ) processed\n",
      "                         ID                Name  Likes  Rating  Tips\n",
      "0  564d283d498e6e851df79d87  Great Indian Curry      3     6.8     2\n",
      "( 10 / 151 ) processed\n",
      "                         ID          Name  Likes  Rating  Tips\n",
      "0  512a9ea9e4b004fb8eeb84e5  Silver Krust     12     8.1     3\n",
      "( 11 / 151 ) processed\n",
      "                         ID       Name  Likes  Rating  Tips\n",
      "0  4db0f4371e729fcc56497f20  Mashallah     19     7.5     7\n",
      "( 12 / 151 ) processed\n",
      "                         ID                          Name  Likes  Rating  Tips\n",
      "0  4b718914f964a520c04b2de3  Madina Restaurant and Sweets     17     6.5    12\n",
      "( 13 / 151 ) processed\n",
      "                         ID                       Name  Likes  Rating  Tips\n",
      "0  52f18573498ec2c34e830ffd  Kanan's Indian Restaurant     23     7.7     8\n",
      "( 14 / 151 ) processed\n",
      "                         ID         Name  Likes  Rating  Tips\n",
      "0  57596dad498e732300496b23  Dosa Royale     75     8.7    22\n",
      "( 15 / 151 ) processed\n",
      "                         ID         Name  Likes  Rating  Tips\n",
      "0  57596dad498e732300496b23  Dosa Royale     75     8.7    22\n",
      "( 16 / 151 ) processed\n",
      "                         ID           Name  Likes  Rating  Tips\n",
      "0  568d3902498e619efcbc3f58  Spice & Grill     19     7.6     6\n",
      "( 17 / 151 ) processed\n",
      "                         ID                        Name  Likes  Rating  Tips\n",
      "0  4bb93b70cf2fc9b6fe64a002  Gandhi Fine Indian Cuisine     81     8.5    47\n",
      "( 18 / 151 ) processed\n",
      "                         ID             Name  Likes  Rating  Tips\n",
      "0  4afdf78bf964a520862c22e3  King of Tandoor     25     7.3    23\n",
      "( 19 / 151 ) processed\n",
      "                         ID             Name  Likes  Rating  Tips\n",
      "0  5539753f498edbace4746b67  Tandoori Masala     12     7.7     2\n",
      "( 20 / 151 ) processed\n",
      "                         ID           Name  Likes  Rating  Tips\n",
      "0  4f6cae2ee4b0d4a5afcef5c0  Delhi Heights     22     7.9     8\n",
      "( 21 / 151 ) processed\n",
      "                         ID                     Name  Likes  Rating  Tips\n",
      "0  519ff6c8498e1300ddcbd45c  Anarkali Indian Cuisine     14     7.8     8\n",
      "( 22 / 151 ) processed\n",
      "                         ID       Name  Likes  Rating  Tips\n",
      "0  4db0f4371e729fcc56497f20  Mashallah     19     7.5     7\n",
      "( 23 / 151 ) processed\n",
      "                         ID                Name  Likes  Rating  Tips\n",
      "0  5631511b498e3d6d7e0a4df0  Tikka Indian Grill     95     8.5    29\n",
      "( 24 / 151 ) processed\n",
      "                         ID                Name  Likes  Rating  Tips\n",
      "0  5631511b498e3d6d7e0a4df0  Tikka Indian Grill     95     8.5    29\n",
      "( 25 / 151 ) processed\n",
      "                         ID                      Name  Likes  Rating  Tips\n",
      "0  4ae7876ef964a5201eac21e3  Kismat Indian Restaurant     45     7.7    25\n",
      "( 26 / 151 ) processed\n",
      "                         ID                           Name  Likes  Rating  \\\n",
      "0  54c2bd96498eaf5142e3fe92  Clove Indian Restaurant & Bar     32     7.4   \n",
      "\n",
      "   Tips  \n",
      "0    16  \n",
      "( 27 / 151 ) processed\n",
      "                         ID           Name  Likes  Rating  Tips\n",
      "0  5914ff32b23dfa207eca38de  Mumbai Masala     14     7.3     7\n",
      "( 28 / 151 ) processed\n",
      "                         ID                 Name  Likes  Rating  Tips\n",
      "0  529d382a11d2dd5ef107e641  Chapati House - NYC     73     7.8    18\n",
      "( 29 / 151 ) processed\n",
      "                         ID                           Name  Likes  Rating  \\\n",
      "0  54c2bd96498eaf5142e3fe92  Clove Indian Restaurant & Bar     32     7.4   \n",
      "\n",
      "   Tips  \n",
      "0    16  \n",
      "( 30 / 151 ) processed\n",
      "                         ID          Name  Likes  Rating  Tips\n",
      "0  56d87f3d498ee215abee5724  Delhi Masala     13     8.7     3\n",
      "( 31 / 151 ) processed\n",
      "                         ID                           Name  Likes  Rating  \\\n",
      "0  54c2bd96498eaf5142e3fe92  Clove Indian Restaurant & Bar     32     7.4   \n",
      "\n",
      "   Tips  \n",
      "0    16  \n",
      "( 32 / 151 ) processed\n",
      "                         ID      Name  Likes  Rating  Tips\n",
      "0  519fe6f5498e30595d370c44  Bawarchi      9     7.4     4\n",
      "( 33 / 151 ) processed\n",
      "                         ID            Name  Likes  Rating  Tips\n",
      "0  5272ca4511d22488f6895caf  Drunken Munkey    208     8.6    61\n",
      "( 34 / 151 ) processed\n",
      "                         ID              Name  Likes  Rating  Tips\n",
      "0  4fe4fb50c2eee335e4fea69d  Moti Mahal Delux    185     8.4    82\n",
      "( 35 / 151 ) processed\n",
      "                         ID    Name  Likes  Rating  Tips\n",
      "0  42489a80f964a5208b201fe3  Swagat    105     8.4    38\n",
      "( 36 / 151 ) processed\n",
      "                         ID           Name  Likes  Rating  Tips\n",
      "0  4b0dec08f964a520ae5223e3  Alachi Masala     18     7.7    17\n",
      "( 37 / 151 ) processed\n",
      "                         ID                   Name  Likes  Rating  Tips\n",
      "0  49d91c12f964a520015e1fe3  The Kati Roll Company    837     8.8   260\n",
      "( 38 / 151 ) processed\n",
      "                         ID                   Name  Likes  Rating  Tips\n",
      "0  59fcd48c464d6567ed2f5e37  The Kati Roll Company     18     8.6     2\n",
      "( 39 / 151 ) processed\n",
      "                         ID               Name  Likes  Rating  Tips\n",
      "0  4b4aab62f964a520978c26e3  Dil-e Punjab Deli    106     8.7    43\n",
      "( 40 / 151 ) processed\n",
      "                         ID              Name  Likes  Rating  Tips\n",
      "0  4bbb9dbded7776b0e1ad3e51  Tamarind TriBeCa    589     9.1   146\n",
      "( 41 / 151 ) processed\n",
      "                         ID                Name  Likes  Rating  Tips\n",
      "0  5b5a2c9e66f3cd002ca0aab5  The Drunken Munkey     26     8.8     4\n",
      "( 42 / 151 ) processed\n",
      "                         ID  Name  Likes  Rating  Tips\n",
      "0  591794df2be42556988e4a8e  Rahi    106     8.8    19\n",
      "( 43 / 151 ) processed\n",
      "                         ID        Name  Likes  Rating  Tips\n",
      "0  4d24b812836f5481518645f7  Doaba Deli     41     7.5    13\n",
      "( 44 / 151 ) processed\n",
      "                         ID              Name  Likes  Rating  Tips\n",
      "0  424de080f964a520ae201fe3  Manhattan Valley     42     7.9    30\n",
      "( 45 / 151 ) processed\n",
      "                         ID   Name  Likes  Rating  Tips\n",
      "0  538ba1f2498e279098e4210a  Awadh     51     8.0    13\n",
      "( 46 / 151 ) processed\n",
      "                         ID       Name  Likes  Rating  Tips\n",
      "0  49c5ad0af964a5201b571fe3  Roti Roll    114     7.9    58\n",
      "( 47 / 151 ) processed\n",
      "                         ID    Name  Likes  Rating  Tips\n",
      "0  4ad12c9df964a52040dd20e3  Aangan     35     7.4    14\n",
      "( 48 / 151 ) processed\n",
      "                         ID       Name  Likes  Rating  Tips\n",
      "0  49c5ad0af964a5201b571fe3  Roti Roll    114     7.9    58\n",
      "( 49 / 151 ) processed\n",
      "                         ID                 Name  Likes  Rating  Tips\n",
      "0  4a70a75bf964a52016d81fe3  Bhatti Indian Grill    416     8.7   159\n",
      "( 50 / 151 ) processed\n",
      "                         ID   Name  Likes  Rating  Tips\n",
      "0  57f7cbbe498edf8f07c7ba83  Sahib     59     8.8    13\n",
      "( 51 / 151 ) processed\n",
      "                         ID     Name  Likes  Rating  Tips\n",
      "0  523b2b42498e1dfabcc8ab15  Pippali    303     8.7    77\n",
      "( 52 / 151 ) processed\n",
      "                         ID                 Name  Likes  Rating  Tips\n",
      "0  4aa56c81f964a5204e4820e3  Seva Indian Cuisine    238     9.0   131\n",
      "( 53 / 151 ) processed\n",
      "                         ID            Name  Likes  Rating  Tips\n",
      "0  4afdcf29f964a520162b22e3  Rajbhog Sweets     37     8.4    24\n",
      "( 54 / 151 ) processed\n",
      "                         ID      Name  Likes  Rating  Tips\n",
      "0  4c7060e734443704ca0e245f  Kababish     30     7.7    17\n",
      "( 55 / 151 ) processed\n",
      "                         ID                      Name  Likes  Rating  Tips\n",
      "0  4b998d3ff964a520fc8235e3  Maharaja Sweets & Snacks     52     8.1    24\n",
      "( 56 / 151 ) processed\n",
      "                         ID                     Name  Likes  Rating  Tips\n",
      "0  5da4fbf091a08400078be19d  Angel Indian Restaurant      3     8.1     1\n",
      "( 57 / 151 ) processed\n",
      "                         ID           Name  Likes  Rating  Tips\n",
      "0  3fd66200f964a52009f11ee3  Jackson Diner    141     7.9    77\n",
      "( 58 / 151 ) processed\n",
      "                         ID           Name  Likes  Rating  Tips\n",
      "0  49ebb18ff964a52016671fe3  Delhi Heights     34     7.9    22\n",
      "( 59 / 151 ) processed\n",
      "                         ID  Name  Likes  Rating  Tips\n",
      "0  4b189424f964a52043d423e3  Dera     47     7.4    19\n",
      "( 60 / 151 ) processed\n",
      "                         ID                         Name  Likes  Rating  Tips\n",
      "0  4e334b7bb0fb17f64f81a8b2  Premium Sweets & Restaurant     11     7.4     5\n",
      "( 61 / 151 ) processed\n",
      "                         ID     Name  Likes  Rating  Tips\n",
      "0  527d9cbc498edf0db10bde6b  Samudra     48     8.5    16\n",
      "( 62 / 151 ) processed\n",
      "                         ID            Name  Likes  Rating  Tips\n",
      "0  4afdcf29f964a520162b22e3  Rajbhog Sweets     37     8.4    24\n",
      "( 63 / 151 ) processed\n",
      "                         ID                      Name  Likes  Rating  Tips\n",
      "0  4b998d3ff964a520fc8235e3  Maharaja Sweets & Snacks     52     8.1    24\n",
      "( 64 / 151 ) processed\n",
      "                         ID                     Name  Likes  Rating  Tips\n",
      "0  5da4fbf091a08400078be19d  Angel Indian Restaurant      3     8.1     1\n",
      "( 65 / 151 ) processed\n",
      "                         ID           Name  Likes  Rating  Tips\n",
      "0  3fd66200f964a52009f11ee3  Jackson Diner    141     7.9    77\n",
      "( 66 / 151 ) processed\n",
      "                         ID           Name  Likes  Rating  Tips\n",
      "0  49ebb18ff964a52016671fe3  Delhi Heights     34     7.9    22\n",
      "( 67 / 151 ) processed\n",
      "                         ID     Name  Likes  Rating  Tips\n",
      "0  527d9cbc498edf0db10bde6b  Samudra     48     8.5    16\n",
      "( 68 / 151 ) processed\n",
      "                         ID                     Name  Likes  Rating  Tips\n",
      "0  5da4fbf091a08400078be19d  Angel Indian Restaurant      3     8.1     1\n",
      "( 69 / 151 ) processed\n",
      "                         ID                Name  Likes  Rating  Tips\n",
      "0  5782c9ce498edde587f5aa14  Tikka Indian Grill     10     7.8     2\n",
      "( 70 / 151 ) processed\n",
      "                         ID                   Name  Likes  Rating  Tips\n",
      "0  4bbe78bfba9776b070cefdc8  Mehak Mughlai Cuisine      8     7.7    10\n",
      "( 71 / 151 ) processed\n",
      "                         ID          Name  Likes  Rating  Tips\n",
      "0  4b522029f964a520f26927e3  Sohna Punjab      8     7.7     2\n",
      "( 72 / 151 ) processed\n",
      "                         ID                Name  Likes  Rating  Tips\n",
      "0  5782c9ce498edde587f5aa14  Tikka Indian Grill     10     7.8     2\n",
      "( 73 / 151 ) processed\n",
      "                         ID        Name  Likes  Rating  Tips\n",
      "0  4f1b77d7e4b044fd359e6d21  India Cafe      6     7.1     3\n",
      "( 74 / 151 ) processed\n",
      "                         ID                 Name  Likes  Rating  Tips\n",
      "0  4adbaef0f964a520ff2921e3  Punjabi Kabab House      7     6.0     7\n",
      "( 75 / 151 ) processed\n",
      "                         ID                Name  Likes  Rating  Tips\n",
      "0  4babc24ef964a5200ac73ae3  Royal India Palace      7     5.9     3\n",
      "( 76 / 151 ) processed\n",
      "                         ID          Name  Likes  Rating  Tips\n",
      "0  4bb2bc48a32876b02e0b01fe  Tandoori Hut      6     5.9    15\n",
      "( 77 / 151 ) processed\n",
      "                         ID  Name  Likes  Rating  Tips\n",
      "0  5b931ea69d7468002c3b1382  Adda    113     9.0    34\n",
      "( 78 / 151 ) processed\n",
      "                         ID                  Name  Likes  Rating  Tips\n",
      "0  50a287a7e4b0033f830f06db  Raj's Indian Kitchen     22     7.3     9\n",
      "( 79 / 151 ) processed\n",
      "                         ID  Name  Likes  Rating  Tips\n",
      "0  5b931ea69d7468002c3b1382  Adda    113     9.0    34\n",
      "( 80 / 151 ) processed\n",
      "                         ID                        Name  Likes  Rating  Tips\n",
      "0  50e1c9708aca7ff2b3e50353  Nepalese Indian Restaurant     55     8.3    18\n",
      "( 81 / 151 ) processed\n",
      "                         ID               Name  Likes  Rating  Tips\n",
      "0  5625af69498ebbc62b61a382  Aaheli Restaurant     12     7.8     6\n",
      "( 82 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 572d7c21498e098658a0edd7\n",
      "( 83 / 151 ) processed\n",
      "                         ID                         Name  Likes  Rating  Tips\n",
      "0  4f1f4996e4b01ff351a7a50c  Ayna Agra Indian Restaurant     39     8.2    12\n",
      "( 84 / 151 ) processed\n",
      "                         ID        Name  Likes  Rating  Tips\n",
      "0  539a4ff0498e79c6745baba9  Masala Box      9     8.0     2\n",
      "( 85 / 151 ) processed\n",
      "                         ID       Name  Likes  Rating  Tips\n",
      "0  539e27b0498e2eba582085ee  masalabox      7     6.5     2\n",
      "( 86 / 151 ) processed\n",
      "                         ID                       Name  Likes  Rating  Tips\n",
      "0  4b787c49f964a5209cd12ee3  Santoor Indian Restaurant     37     7.6    18\n",
      "( 87 / 151 ) processed\n",
      "                         ID             Name  Likes  Rating  Tips\n",
      "0  4b9030abf964a520397b33e3  Taste of Cochin      9     6.9     4\n",
      "( 88 / 151 ) processed\n",
      "                         ID           Name  Likes  Rating  Tips\n",
      "0  4df0f39dd4c04d0392c853ea  Sagar Chinese      7     6.0     6\n",
      "( 89 / 151 ) processed\n",
      "                         ID          Name  Likes  Rating  Tips\n",
      "0  4c0e256ab1b676b06589e186  Sohna Punjab      3     5.9     3\n",
      "( 90 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4e6bfe1c7d8b2c711b17bbe5\n",
      "( 91 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4dc0aaedae606fe8b71c226b\n",
      "( 92 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4b96926df964a520abd534e3\n",
      "( 93 / 151 ) processed\n",
      "                         ID          Name  Likes  Rating  Tips\n",
      "0  4bad49a0f964a52041423be3  Annam Brahma     15     8.0     3\n",
      "( 94 / 151 ) processed\n",
      "                         ID                               Name  Likes  Rating  \\\n",
      "0  4be334312fc7d13a7a81083a  Taj Mahal Restaurant & Party Hall     24     7.4   \n",
      "\n",
      "   Tips  \n",
      "0     5  \n",
      "( 95 / 151 ) processed\n",
      "                         ID            Name  Likes  Rating  Tips\n",
      "0  4cc08b0900d83704ed474b5c  Sybil's Bakery      8     7.2     3\n",
      "( 96 / 151 ) processed\n",
      "                         ID              Name  Likes  Rating  Tips\n",
      "0  4c434b2bd691c9b6ef8f8f0a  Sagar Restaurant     10     7.5     6\n",
      "( 97 / 151 ) processed\n",
      "                         ID          Name  Likes  Rating  Tips\n",
      "0  4bad49a0f964a52041423be3  Annam Brahma     15     8.0     3\n",
      "( 98 / 151 ) processed\n",
      "                         ID            Name  Likes  Rating  Tips\n",
      "0  4cc08b0900d83704ed474b5c  Sybil's Bakery      8     7.2     3\n",
      "( 99 / 151 ) processed\n",
      "                         ID                    Name  Likes  Rating  Tips\n",
      "0  562035d9498e2abb4137c2c7  Yaar Indian Restaurant     31     8.6     7\n",
      "( 100 / 151 ) processed\n",
      "                         ID           Name  Likes  Rating  Tips\n",
      "0  527ffc0811d2d329d5e49abd  Jackson Diner      9     8.0     3\n",
      "( 101 / 151 ) processed\n",
      "                         ID                      Name  Likes  Rating  Tips\n",
      "0  4b647b56f964a520c4b62ae3  Usha Foods & Usha Sweets     33     7.9    10\n",
      "( 102 / 151 ) processed\n",
      "                         ID            Name  Likes  Rating  Tips\n",
      "0  4e4e3e22bd4101d0d7a5c2d1  Kerala Kitchen      5     8.0     6\n",
      "( 103 / 151 ) processed\n",
      "                         ID                       Name  Likes  Rating  Tips\n",
      "0  4b787c49f964a5209cd12ee3  Santoor Indian Restaurant     37     7.6    18\n",
      "( 104 / 151 ) processed\n",
      "                         ID           Name  Likes  Rating  Tips\n",
      "0  4c0c01e0bbc676b00d6b4cd5  Mumbai Xpress     16     6.6    18\n",
      "( 105 / 151 ) processed\n",
      "                         ID             Name  Likes  Rating  Tips\n",
      "0  4c76ff35a5676dcb72671721  Flavor Of India      6     6.1     6\n",
      "( 106 / 151 ) processed\n",
      "                         ID           Name  Likes  Rating  Tips\n",
      "0  4df0f39dd4c04d0392c853ea  Sagar Chinese      7     6.0     6\n",
      "( 107 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4c953a7672dd224bd8d1a191\n",
      "( 108 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4cc642ed306e224b5bf2a76c\n",
      "( 109 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 51d84192498ea979a3c4f13d\n",
      "( 110 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4e6bfe1c7d8b2c711b17bbe5\n",
      "( 111 / 151 ) processed\n",
      "                         ID                        Name  Likes  Rating  Tips\n",
      "0  4f580c1be4b0bdfd0e7e8102  Rajdhani Indian Restaurant     13     8.3     6\n",
      "( 112 / 151 ) processed\n",
      "                         ID              Name  Likes  Rating  Tips\n",
      "0  4c434b2bd691c9b6ef8f8f0a  Sagar Restaurant     10     7.5     6\n",
      "( 113 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4b8d5734f964a520b1f532e3\n",
      "( 114 / 151 ) processed\n",
      "                         ID                  Name  Likes  Rating  Tips\n",
      "0  5623f6f9498e5a44a08bfae8  Boishakhi Restaurant     17     7.9     7\n",
      "( 115 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4dc0aaedae606fe8b71c226b\n",
      "( 116 / 151 ) processed\n",
      "                         ID         Name  Likes  Rating  Tips\n",
      "0  4b9be038f964a520393036e3  Dosa Garden     18     7.8    17\n",
      "( 117 / 151 ) processed\n",
      "                         ID               Name  Likes  Rating  Tips\n",
      "0  4be74a502468c928505a0243  Taste Of India II     29     8.1    14\n",
      "( 118 / 151 ) processed\n",
      "                         ID         Name  Likes  Rating  Tips\n",
      "0  4b9be038f964a520393036e3  Dosa Garden     18     7.8    17\n",
      "( 119 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4b65f2e3f964a5206e0a2be3\n",
      "( 120 / 151 ) processed\n",
      "                         ID                     Name  Likes  Rating  Tips\n",
      "0  519ff6c8498e1300ddcbd45c  Anarkali Indian Cuisine     14     7.8     8\n",
      "( 121 / 151 ) processed\n",
      "                         ID       Name  Likes  Rating  Tips\n",
      "0  4db0f4371e729fcc56497f20  Mashallah     19     7.5     7\n",
      "( 122 / 151 ) processed\n",
      "                         ID                Name  Likes  Rating  Tips\n",
      "0  564d283d498e6e851df79d87  Great Indian Curry      3     6.8     2\n",
      "( 123 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4b65f2e3f964a5206e0a2be3\n",
      "( 124 / 151 ) processed\n",
      "                         ID               Name  Likes  Rating  Tips\n",
      "0  4be74a502468c928505a0243  Taste Of India II     29     8.1    14\n",
      "( 125 / 151 ) processed\n",
      "                         ID            Name  Likes  Rating  Tips\n",
      "0  5272ca4511d22488f6895caf  Drunken Munkey    208     8.6    61\n",
      "( 126 / 151 ) processed\n",
      "                         ID                    Name  Likes  Rating  Tips\n",
      "0  56ed855a498ef3bb022352c3  Mughlai Indian Cuisine     26     7.8     9\n",
      "( 127 / 151 ) processed\n",
      "                         ID              Name  Likes  Rating  Tips\n",
      "0  5b0c8e2d2f97ec002c67a428  Ashoka Fine Dine      9     7.8     5\n",
      "( 128 / 151 ) processed\n",
      "                         ID              Name  Likes  Rating  Tips\n",
      "0  4bbb9dbded7776b0e1ad3e51  Tamarind TriBeCa    589     9.1   146\n",
      "( 129 / 151 ) processed\n",
      "                         ID                   Name  Likes  Rating  Tips\n",
      "0  49d91c12f964a520015e1fe3  The Kati Roll Company    837     8.8   260\n",
      "( 130 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4b65f2e3f964a5206e0a2be3\n",
      "( 131 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4b65f2e3f964a5206e0a2be3\n",
      "( 132 / 151 ) processed\n",
      "                         ID          Name  Likes  Rating  Tips\n",
      "0  4bad49a0f964a52041423be3  Annam Brahma     15     8.0     3\n",
      "( 133 / 151 ) processed\n",
      "                         ID              Name  Likes  Rating  Tips\n",
      "0  4c434b2bd691c9b6ef8f8f0a  Sagar Restaurant     10     7.5     6\n",
      "( 134 / 151 ) processed\n",
      "                         ID            Name  Likes  Rating  Tips\n",
      "0  4cc08b0900d83704ed474b5c  Sybil's Bakery      8     7.2     3\n",
      "( 135 / 151 ) processed\n",
      "                         ID         Name  Likes  Rating  Tips\n",
      "0  551b7f75498e86c00a0ed2e1  Hungry Bird      8     6.9     3\n",
      "( 136 / 151 ) processed\n",
      "                         ID                           Name  Likes  Rating  \\\n",
      "0  4a63bfb4f964a520b3c51fe3  Chola Eclectic Indian Cuisine    153     8.3   \n",
      "\n",
      "   Tips  \n",
      "0    56  \n",
      "( 137 / 151 ) processed\n",
      "                         ID              Name  Likes  Rating  Tips\n",
      "0  4fe4fb50c2eee335e4fea69d  Moti Mahal Delux    185     8.4    82\n",
      "( 138 / 151 ) processed\n",
      "                         ID                   Name  Likes  Rating  Tips\n",
      "0  4f57f98fe4b0bd50f6bb8b31  The Kati Roll Company    182     8.2    55\n",
      "( 139 / 151 ) processed\n",
      "                         ID                   Name  Likes  Rating  Tips\n",
      "0  59fcd48c464d6567ed2f5e37  The Kati Roll Company     18     8.6     2\n",
      "( 140 / 151 ) processed\n",
      "                         ID   Name  Likes  Rating  Tips\n",
      "0  5ac3984ae57ca64be4dc6168  INDAY     33     8.1     9\n",
      "( 141 / 151 ) processed\n",
      "                         ID                   Name  Likes  Rating  Tips\n",
      "0  4f57f98fe4b0bd50f6bb8b31  The Kati Roll Company    182     8.2    55\n",
      "( 142 / 151 ) processed\n",
      "                         ID                   Name  Likes  Rating  Tips\n",
      "0  59fcd48c464d6567ed2f5e37  The Kati Roll Company     18     8.6     2\n",
      "( 143 / 151 ) processed\n",
      "                         ID   Name  Likes  Rating  Tips\n",
      "0  5ac3984ae57ca64be4dc6168  INDAY     33     8.1     9\n",
      "( 144 / 151 ) processed\n",
      "                         ID            Name  Likes  Rating  Tips\n",
      "0  4c48da9f3013a59356c5f0e1  Saffron Garden     17     7.5    16\n",
      "( 145 / 151 ) processed\n",
      "                         ID  Name  Likes  Rating  Tips\n",
      "0  5b931ea69d7468002c3b1382  Adda    113     9.0    34\n",
      "( 146 / 151 ) processed\n",
      "                         ID             Name  Likes  Rating  Tips\n",
      "0  5539753f498edbace4746b67  Tandoori Masala     12     7.7     2\n",
      "( 147 / 151 ) processed\n",
      "                         ID                Name  Likes  Rating  Tips\n",
      "0  564d283d498e6e851df79d87  Great Indian Curry      3     6.8     2\n",
      "( 148 / 151 ) processed\n",
      "                         ID               Name  Likes  Rating  Tips\n",
      "0  4b1b341bf964a5208af923e3  Five Star Banquet     30     7.1    31\n",
      "( 149 / 151 ) processed\n",
      "                         ID                  Name  Likes  Rating  Tips\n",
      "0  50a287a7e4b0033f830f06db  Raj's Indian Kitchen     22     7.3     9\n",
      "( 150 / 151 ) processed\n",
      "Empty DataFrame\n",
      "Columns: [ID, Name, Likes, Rating, Tips]\n",
      "Index: []\n",
      "No data available for id= 4b65f2e3f964a5206e0a2be3\n",
      "( 151 / 151 ) processed\n"
     ]
    }
   ],
   "source": [
    "# prepare neighborhood list that contains indian resturants\n",
    "column_names=['Borough', 'Neighborhood', 'ID','Name','Likes','Rating','Tips']\n",
    "indian_rest_stats_ny=pd.DataFrame(columns=column_names)\n",
    "count=1\n",
    "\n",
    "\n",
    "for row in indian_rest_ny.values.tolist():\n",
    "    Borough,Neighborhood,ID,Name=row\n",
    "    try:\n",
    "        venue_details=get_venue_details(ID)\n",
    "        print(venue_details)\n",
    "        id,name,likes,rating,tips=venue_details.values.tolist()[0]\n",
    "    except IndexError:\n",
    "        print('No data available for id=',ID)\n",
    "        # we will assign 0 value for these resturants as they may have been \n",
    "        #recently opened or details does not exist in FourSquare Database\n",
    "        id,name,likes,rating,tips=[0]*5\n",
    "    print('(',count,'/',len(indian_rest_ny),')','processed')\n",
    "    indian_rest_stats_ny = indian_rest_stats_ny.append({'Borough': Borough,\n",
    "                                                'Neighborhood': Neighborhood, \n",
    "                                                'ID': id,\n",
    "                                                'Name' : name,\n",
    "                                                'Likes' : likes,\n",
    "                                                'Rating' : rating,\n",
    "                                                'Tips' : tips\n",
    "                                               }, ignore_index=True)\n",
    "    count+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Borough</th>\n",
       "      <th>Neighborhood</th>\n",
       "      <th>ID</th>\n",
       "      <th>Name</th>\n",
       "      <th>Likes</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Tips</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Woodlawn</td>\n",
       "      <td>4c0448d9310fc9b6bf1dc761</td>\n",
       "      <td>Curry Spot</td>\n",
       "      <td>5</td>\n",
       "      <td>7.6</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Parkchester</td>\n",
       "      <td>4c194631838020a13e78e561</td>\n",
       "      <td>Melanies Roti Bar And Grill</td>\n",
       "      <td>3</td>\n",
       "      <td>5.8</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Spuyten Duyvil</td>\n",
       "      <td>4c04544df423a593ac83d116</td>\n",
       "      <td>Cumin Indian Cuisine</td>\n",
       "      <td>13</td>\n",
       "      <td>6.1</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Concourse</td>\n",
       "      <td>551b7f75498e86c00a0ed2e1</td>\n",
       "      <td>Hungry Bird</td>\n",
       "      <td>8</td>\n",
       "      <td>6.9</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Unionport</td>\n",
       "      <td>4c194631838020a13e78e561</td>\n",
       "      <td>Melanies Roti Bar And Grill</td>\n",
       "      <td>3</td>\n",
       "      <td>5.8</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Borough    Neighborhood                        ID  \\\n",
       "0   Bronx        Woodlawn  4c0448d9310fc9b6bf1dc761   \n",
       "1   Bronx     Parkchester  4c194631838020a13e78e561   \n",
       "2   Bronx  Spuyten Duyvil  4c04544df423a593ac83d116   \n",
       "3   Bronx       Concourse  551b7f75498e86c00a0ed2e1   \n",
       "4   Bronx       Unionport  4c194631838020a13e78e561   \n",
       "\n",
       "                          Name Likes  Rating Tips  \n",
       "0                   Curry Spot     5     7.6   10  \n",
       "1  Melanies Roti Bar And Grill     3     5.8    2  \n",
       "2         Cumin Indian Cuisine    13     6.1    9  \n",
       "3                  Hungry Bird     8     6.9    3  \n",
       "4  Melanies Roti Bar And Grill     3     5.8    2  "
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "indian_rest_stats_ny.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(151, 7)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "indian_rest_stats_ny.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(151, 4)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "indian_rest_ny.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that we got data for all resturants Now lets save this data to a csv sheet. In case we by mistake modify it. As the number of calls to get details for venue are premium call and have limit of 500 per day, we will refer to saved data sheet csv if required."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "indian_rest_stats_ny.to_csv('indian_rest_stats_ny.csv', index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lets verify the data from saved csv file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "indian_rest_stats_ny_csv=pd.read_csv('indian_rest_stats_ny.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(151, 7)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "indian_rest_stats_ny_csv.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Borough</th>\n",
       "      <th>Neighborhood</th>\n",
       "      <th>ID</th>\n",
       "      <th>Name</th>\n",
       "      <th>Likes</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Tips</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Woodlawn</td>\n",
       "      <td>4c0448d9310fc9b6bf1dc761</td>\n",
       "      <td>Curry Spot</td>\n",
       "      <td>5</td>\n",
       "      <td>7.6</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Parkchester</td>\n",
       "      <td>4c194631838020a13e78e561</td>\n",
       "      <td>Melanies Roti Bar And Grill</td>\n",
       "      <td>3</td>\n",
       "      <td>5.8</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Spuyten Duyvil</td>\n",
       "      <td>4c04544df423a593ac83d116</td>\n",
       "      <td>Cumin Indian Cuisine</td>\n",
       "      <td>13</td>\n",
       "      <td>6.1</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Concourse</td>\n",
       "      <td>551b7f75498e86c00a0ed2e1</td>\n",
       "      <td>Hungry Bird</td>\n",
       "      <td>8</td>\n",
       "      <td>6.9</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>Unionport</td>\n",
       "      <td>4c194631838020a13e78e561</td>\n",
       "      <td>Melanies Roti Bar And Grill</td>\n",
       "      <td>3</td>\n",
       "      <td>5.8</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Borough    Neighborhood                        ID  \\\n",
       "0   Bronx        Woodlawn  4c0448d9310fc9b6bf1dc761   \n",
       "1   Bronx     Parkchester  4c194631838020a13e78e561   \n",
       "2   Bronx  Spuyten Duyvil  4c04544df423a593ac83d116   \n",
       "3   Bronx       Concourse  551b7f75498e86c00a0ed2e1   \n",
       "4   Bronx       Unionport  4c194631838020a13e78e561   \n",
       "\n",
       "                          Name  Likes  Rating  Tips  \n",
       "0                   Curry Spot      5     7.6    10  \n",
       "1  Melanies Roti Bar And Grill      3     5.8     2  \n",
       "2         Cumin Indian Cuisine     13     6.1     9  \n",
       "3                  Hungry Bird      8     6.9     3  \n",
       "4  Melanies Roti Bar And Grill      3     5.8     2  "
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "indian_rest_stats_ny_csv.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 151 entries, 0 to 150\n",
      "Data columns (total 7 columns):\n",
      "Borough         151 non-null object\n",
      "Neighborhood    151 non-null object\n",
      "ID              151 non-null object\n",
      "Name            151 non-null object\n",
      "Likes           151 non-null object\n",
      "Rating          151 non-null float64\n",
      "Tips            151 non-null object\n",
      "dtypes: float64(1), object(6)\n",
      "memory usage: 4.8+ KB\n"
     ]
    }
   ],
   "source": [
    "indian_rest_stats_ny.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The Data type of 'Likes' and  'Tips' are of type 'String'. we will convert them into type 'Float' for further analysis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "indian_rest_stats_ny['Likes']=indian_rest_stats_ny['Likes'].astype('float64')\n",
    "indian_rest_stats_ny['Tips']=indian_rest_stats_ny['Tips'].astype('float64')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 151 entries, 0 to 150\n",
      "Data columns (total 7 columns):\n",
      "Borough         151 non-null object\n",
      "Neighborhood    151 non-null object\n",
      "ID              151 non-null object\n",
      "Name            151 non-null object\n",
      "Likes           151 non-null float64\n",
      "Rating          151 non-null float64\n",
      "Tips            151 non-null float64\n",
      "dtypes: float64(3), object(4)\n",
      "memory usage: 6.0+ KB\n"
     ]
    }
   ],
   "source": [
    "indian_rest_stats_ny.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we will find the Indian restuarants with Maximum Likes, Maximum Ratings and Maximum Tips."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Borough                        Manhattan\n",
       "Neighborhood                     Midtown\n",
       "ID              49d91c12f964a520015e1fe3\n",
       "Name               The Kati Roll Company\n",
       "Likes                                837\n",
       "Rating                               8.8\n",
       "Tips                                 260\n",
       "Name: 37, dtype: object"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Resturant with maximum Likes\n",
    "indian_rest_stats_ny.iloc[indian_rest_stats_ny['Likes'].idxmax()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Borough                        Manhattan\n",
       "Neighborhood                     Tribeca\n",
       "ID              4bbb9dbded7776b0e1ad3e51\n",
       "Name                    Tamarind TriBeCa\n",
       "Likes                                589\n",
       "Rating                               9.1\n",
       "Tips                                 146\n",
       "Name: 40, dtype: object"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Resturant with maximum Rating\n",
    "indian_rest_stats_ny.iloc[indian_rest_stats_ny['Rating'].idxmax()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Borough                        Manhattan\n",
       "Neighborhood                     Midtown\n",
       "ID              49d91c12f964a520015e1fe3\n",
       "Name               The Kati Roll Company\n",
       "Likes                                837\n",
       "Rating                               8.8\n",
       "Tips                                 260\n",
       "Name: 37, dtype: object"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Resturant with maximum Tips\n",
    "indian_rest_stats_ny.iloc[indian_rest_stats_ny['Tips'].idxmax()]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next lets visualize neighborhood with maximum average rating of resturants."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "ny_neighborhood_stats=indian_rest_stats_ny.groupby('Neighborhood',as_index=False).mean()[['Neighborhood','Rating']]\n",
    "ny_neighborhood_stats.columns=['Neighborhood','Average Rating']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Neighborhood</th>\n",
       "      <th>Average Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>12</td>\n",
       "      <td>Civic Center</td>\n",
       "      <td>9.100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>69</td>\n",
       "      <td>Tribeca</td>\n",
       "      <td>9.100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Astoria</td>\n",
       "      <td>9.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>Blissville</td>\n",
       "      <td>9.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>75</td>\n",
       "      <td>West Village</td>\n",
       "      <td>8.800000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>44</td>\n",
       "      <td>Midtown South</td>\n",
       "      <td>8.800000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>43</td>\n",
       "      <td>Midtown</td>\n",
       "      <td>8.800000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>29</td>\n",
       "      <td>Gramercy</td>\n",
       "      <td>8.733333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>25</td>\n",
       "      <td>Fort Greene</td>\n",
       "      <td>8.700000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>11</td>\n",
       "      <td>Chelsea</td>\n",
       "      <td>8.700000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Neighborhood  Average Rating\n",
       "12   Civic Center        9.100000\n",
       "69        Tribeca        9.100000\n",
       "0         Astoria        9.000000\n",
       "5      Blissville        9.000000\n",
       "75   West Village        8.800000\n",
       "44  Midtown South        8.800000\n",
       "43        Midtown        8.800000\n",
       "29       Gramercy        8.733333\n",
       "25    Fort Greene        8.700000\n",
       "11        Chelsea        8.700000"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ny_neighborhood_stats.sort_values(['Average Rating'],ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Above are the top neighborhoods with top average rating of Indian resturants."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Similarly we will find the average rating of Indian Resturants for each Borough."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "ny_borough_stats=indian_rest_stats_ny.groupby('Borough',as_index=False).mean()[['Borough','Rating']]\n",
    "ny_borough_stats.columns=['Borough','Average Rating']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Borough</th>\n",
       "      <th>Average Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Manhattan</td>\n",
       "      <td>8.210000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Brooklyn</td>\n",
       "      <td>7.700000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Queens</td>\n",
       "      <td>6.552113</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Bronx</td>\n",
       "      <td>5.585714</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>Staten Island</td>\n",
       "      <td>3.533333</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Borough  Average Rating\n",
       "2      Manhattan        8.210000\n",
       "1       Brooklyn        7.700000\n",
       "3         Queens        6.552113\n",
       "0          Bronx        5.585714\n",
       "4  Staten Island        3.533333"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ny_borough_stats.sort_values(['Average Rating'],ascending=False).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lets Visualize it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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66yzDj/72c9mi+VnP/sZ66yzDksttRRve9vbOOuss4iI+X6TMZN8SZIkNdadd97JL37xC5ZYYolZ8xZbbDFOPPFEbr75Zs466yx+/etf86UvfQmAzTbbjOOPP55ll12W+++/n/vvv58vfvGLw67/kEMOYccdd+TPf/4z2267LR/5yEeYMmUKAHfffTcf+MAH2H777bnxxhv59Kc/zQEHHDB/X3DFch1JWkgt6LrYhcVI63clNc+FF17IC1/4QmbOnMnTTz8NlN77Ifvss8+s39dee20OPfRQ9txzT04++WSWXHJJlltuOSKC8ePHz3Nbu+++OzvvvDMARxxxBCeddBLXXnst22yzDaeeeirrrrsuRx99NADrrrsuN998M4cffngvX25HJvmSJElqlLe97W2ccsopPPnkk5x22mncdttt7L333rOWX3755RxxxBHccsstTJs2jRkzZvD000/zxBNPjPjC2g022GDW70svvTTLLLMMkydPBuBvf/sbG2200WztN95441G8su5ZriNJkqRGWXrppXnFK17BBhtswIknnsj06dM55JBDALjnnnvYdtttee1rX8uPf/xjbrjhBr75zW8C9e4w21oGBKVO/7nnngMgM+e4sVVm1nlJI2aSL0mSpEY76KCD+PrXv86kSZO4/vrrmTFjBscccwybbLIJr3zlK5k0adJs7Zdccklmzpw56u2+6lWv4rrrrptt3vXXXz/q9XbDJF+SJEmNtuWWW/Ka17yGI444gpe//OXMmDGDk046iTvvvJPvfve7nHrqqbO1X2uttXj88ce57LLLePjhh3nyySdrbffTn/40t956K/vuuy+33XYb55xzDmeeeSbAHD38vTaQNfkRsThwMPARYDxwP3AmcFhmPte/yCRJkhZtC+vF7Z///OfZY4892HfffTn22GP56le/yoQJE9hiiy048sgj+ehHPzqr7WabbcZnPvMZdtppJx555BEOOuigWcNojsTaa6/Neeedxxe+8AVOOOEENt10Uw444AD23HNPxo4d28NXN6dYUHVBIxERBwD/AewG/AV4E3AGcGBmntDF85cFpk6dOpVll112vsYqSf3i6DqdLawJiDRInn76ae666y7WXnttXvCCF/Q7nEY5/PDDOfXUU7nvvvuGbTO3/T9t2jSWW245gOUyc9pw6xjInnxgU+D8zBz6D3Z3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\n",
      "text/plain": [
       "<Figure size 900x500 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(9,5), dpi = 100)\n",
    "# title\n",
    "plt.title('Average rating of Indian Resturants for each Borough')\n",
    "#On x-axis\n",
    "plt.xlabel('Borough', fontsize = 15)\n",
    "#On y-axis\n",
    "plt.ylabel('Average Rating', fontsize=15)\n",
    "#giving a bar plot\n",
    "indian_rest_stats_ny.groupby('Borough').mean()['Rating'].plot(kind='bar')\n",
    "#legend\n",
    "plt.legend()\n",
    "#displays the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will consider all the neighborhoods with average rating greater or equal 9.0 to visualize on map."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "ny_neighborhood_stats=ny_neighborhood_stats[ny_neighborhood_stats['Average Rating']>=9.0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Neighborhood</th>\n",
       "      <th>Average Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Astoria</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>Blissville</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>12</td>\n",
       "      <td>Civic Center</td>\n",
       "      <td>9.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>69</td>\n",
       "      <td>Tribeca</td>\n",
       "      <td>9.1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Neighborhood  Average Rating\n",
       "0        Astoria             9.0\n",
       "5     Blissville             9.0\n",
       "12  Civic Center             9.1\n",
       "69       Tribeca             9.1"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ny_neighborhood_stats"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will join this dataset to original new york data to get lonitude and latitude."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "ny_neighborhood_stats=pd.merge(ny_neighborhood_stats,new_york_data, on='Neighborhood')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "ny_neighborhood_stats=ny_neighborhood_stats[['Borough','Neighborhood','Latitude','Longitude','Average Rating']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Borough</th>\n",
       "      <th>Neighborhood</th>\n",
       "      <th>Latitude</th>\n",
       "      <th>Longitude</th>\n",
       "      <th>Average Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Astoria</td>\n",
       "      <td>40.768509</td>\n",
       "      <td>-73.915654</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Queens</td>\n",
       "      <td>Blissville</td>\n",
       "      <td>40.737251</td>\n",
       "      <td>-73.932442</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Manhattan</td>\n",
       "      <td>Civic Center</td>\n",
       "      <td>40.715229</td>\n",
       "      <td>-74.005415</td>\n",
       "      <td>9.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Manhattan</td>\n",
       "      <td>Tribeca</td>\n",
       "      <td>40.721522</td>\n",
       "      <td>-74.010683</td>\n",
       "      <td>9.1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Borough  Neighborhood   Latitude  Longitude  Average Rating\n",
       "0     Queens       Astoria  40.768509 -73.915654             9.0\n",
       "1     Queens    Blissville  40.737251 -73.932442             9.0\n",
       "2  Manhattan  Civic Center  40.715229 -74.005415             9.1\n",
       "3  Manhattan       Tribeca  40.721522 -74.010683             9.1"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ny_neighborhood_stats"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally, Let's show this data on a map."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "ny_map = folium.Map(location=geo_location('New York'), zoom_start=12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "# instantiate a feature group for the incidents in the dataframe\n",
    "incidents = folium.map.FeatureGroup()\n",
    "\n",
    "# loop through the neighborhood and add each to the feature group\n",
    "for lat, lng, in ny_neighborhood_stats[['Latitude','Longitude']].values:\n",
    "    incidents.add_child(\n",
    "        folium.CircleMarker(\n",
    "            [lat, lng],\n",
    "            radius=10, # define how big you want the circle markers to be\n",
    "            color='yellow',\n",
    "            fill=True,\n",
    "            fill_color='blue',\n",
    "            fill_opacity=0.6\n",
    "        )\n",
    "    )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lets add a new field to dataframe for labeling purpose."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "ny_neighborhood_stats['Label']=ny_neighborhood_stats['Neighborhood']+', '+ny_neighborhood_stats['Borough']+'('+ny_neighborhood_stats['Average Rating'].map(str)+')'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div style=\"width:100%;\"><div style=\"position:relative;width:100%;height:0;padding-bottom:60%;\"><iframe src=\"data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgCiAgICAgICAgPHNjcmlwdD4KICAgICAgICAgICAgTF9OT19UT1VDSCA9IGZhbHNlOwogICAgICAgICAgICBMX0RJU0FCTEVfM0QgPSBmYWxzZTsKICAgICAgICA8L3NjcmlwdD4KICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjUuMS9kaXN0L2xlYWZsZXQuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS0xLjEyLjQubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9qcy9ib290c3RyYXAubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5qcyI+PC9zY3JpcHQ+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjUuMS9kaXN0L2xlYWZsZXQuY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vYm9vdHN0cmFwLzMuMi4wL2Nzcy9ib290c3RyYXAubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9mb250LWF3ZXNvbWUvNC42LjMvY3NzL2ZvbnQtYXdlc29tZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL0xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLzIuMC4yL2xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhd2Nkbi5naXRoYWNrLmNvbS9weXRob24tdmlzdWFsaXphdGlvbi9mb2xpdW0vbWFzdGVyL2ZvbGl1bS90ZW1wbGF0ZXMvbGVhZmxldC5hd2Vzb21lLnJvdGF0ZS5jc3MiLz4KICAgIDxzdHlsZT5odG1sLCBib2R5IHt3aWR0aDogMTAwJTtoZWlnaHQ6IDEwMCU7bWFyZ2luOiAwO3BhZGRpbmc6IDA7fTwvc3R5bGU+CiAgICA8c3R5bGU+I21hcCB7cG9zaXRpb246YWJzb2x1dGU7dG9wOjA7Ym90dG9tOjA7cmlnaHQ6MDtsZWZ0OjA7fTwvc3R5bGU+CiAgICAKICAgICAgICAgICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwKICAgICAgICAgICAgICAgIGluaXRpYWwtc2NhbGU9MS4wLCBtYXhpbXVtLXNjYWxlPTEuMCwgdXNlci1zY2FsYWJsZT1ubyIgLz4KICAgICAgICAgICAgPHN0eWxlPgogICAgICAgICAgICAgICAgI21hcF9lMDg1MTQ0YjI5ZDM0ZTY5ODA1NTc1YmNlOGRmZDRlNyB7CiAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IHJlbGF0aXZlOwogICAgICAgICAgICAgICAgICAgIHdpZHRoOiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgbGVmdDogMC4wJTsKICAgICAgICAgICAgICAgICAgICB0b3A6IDAuMCU7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgCjwvaGVhZD4KPGJvZHk+ICAgIAogICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfZTA4NTE0NGIyOWQzNGU2OTgwNTU3NWJjZThkZmQ0ZTciID48L2Rpdj4KICAgICAgICAKPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFwX2UwODUxNDRiMjlkMzRlNjk4MDU1NzViY2U4ZGZkNGU3ID0gTC5tYXAoCiAgICAgICAgICAgICAgICAibWFwX2UwODUxNDRiMjlkMzRlNjk4MDU1NzViY2U4ZGZkNGU3IiwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBjZW50ZXI6IFs0MC43MTI3MjgxLCAtNzQuMDA2MDE1Ml0sCiAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NywKICAgICAgICAgICAgICAgICAgICB6b29tOiAxMiwKICAgICAgICAgICAgICAgICAgICB6b29tQ29udHJvbDogdHJ1ZSwKICAgICAgICAgICAgICAgICAgICBwcmVmZXJDYW52YXM6IGZhbHNlLAogICAgICAgICAgICAgICAgfQogICAgICAgICAgICApOwoKICAgICAgICAgICAgCgogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzMxZWMxOWQzMTE0OTQyODRiYjQwMzAwZWMzNTYyMWJjID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAiaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmciLAogICAgICAgICAgICAgICAgeyJhdHRyaWJ1dGlvbiI6ICJEYXRhIGJ5IFx1MDAyNmNvcHk7IFx1MDAzY2EgaHJlZj1cImh0dHA6Ly9vcGVuc3RyZWV0bWFwLm9yZ1wiXHUwMDNlT3BlblN0cmVldE1hcFx1MDAzYy9hXHUwMDNlLCB1bmRlciBcdTAwM2NhIGhyZWY9XCJodHRwOi8vd3d3Lm9wZW5zdHJlZXRtYXAub3JnL2NvcHlyaWdodFwiXHUwMDNlT0RiTFx1MDAzYy9hXHUwMDNlLiIsICJkZXRlY3RSZXRpbmEiOiBmYWxzZSwgIm1heE5hdGl2ZVpvb20iOiAxOCwgIm1heFpvb20iOiAxOCwgIm1pblpvb20iOiAwLCAibm9XcmFwIjogZmFsc2UsICJvcGFjaXR5IjogMSwgInN1YmRvbWFpbnMiOiAiYWJjIiwgInRtcyI6IGZhbHNlfQogICAgICAgICAgICApLmFkZFRvKG1hcF9lMDg1MTQ0YjI5ZDM0ZTY5ODA1NTc1YmNlOGRmZDRlNyk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIG1hcmtlcl80MWQyYmE1MmY4N2Y0ZTU1YTI5YzNhNThlZjI5ZmZjYiA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc2ODUwODU5MzM1NDkyLCAtNzMuOTE1NjUzNzQzMDQyMzRdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZTA4NTE0NGIyOWQzNGU2OTgwNTU3NWJjZThkZmQ0ZTcpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzE4ZmIwYzFjYzNjMDQ4Nzk4YzBjZDVkNDc1NmZlMDExID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9lYWE2MDQ5MjY3NmE0ZDAyYjlkZTdhMzBkMmNkNDk0OCA9ICQoYDxkaXYgaWQ9Imh0bWxfZWFhNjA0OTI2NzZhNGQwMmI5ZGU3YTMwZDJjZDQ5NDgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFzdG9yaWEsIFF1ZWVucyg5LjApPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzE4ZmIwYzFjYzNjMDQ4Nzk4YzBjZDVkNDc1NmZlMDExLnNldENvbnRlbnQoaHRtbF9lYWE2MDQ5MjY3NmE0ZDAyYjlkZTdhMzBkMmNkNDk0OCk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl80MWQyYmE1MmY4N2Y0ZTU1YTI5YzNhNThlZjI5ZmZjYi5iaW5kUG9wdXAocG9wdXBfMThmYjBjMWNjM2MwNDg3OThjMGNkNWQ0NzU2ZmUwMTEpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfMTIzMmVlYzg3ZTJjNDhiYTkyN2I1NDBkOGUzMmRiOGIgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MzcyNTA3MTY5NDQ5NywgLTczLjkzMjQ0MjM1MjYwMTc4XSwKICAgICAgICAgICAgICAgIHt9CiAgICAgICAgICAgICkuYWRkVG8obWFwX2UwODUxNDRiMjlkMzRlNjk4MDU1NzViY2U4ZGZkNGU3KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9lM2NhMzYzMTg4MjM0ZGQzYTg1ODhlODc3MmYwYzkzNCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfN2ZlN2FjNzM5ZWVlNGJiMThkNTI5MWYyYTQ2NTEzZDQgPSAkKGA8ZGl2IGlkPSJodG1sXzdmZTdhYzczOWVlZTRiYjE4ZDUyOTFmMmE0NjUxM2Q0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CbGlzc3ZpbGxlLCBRdWVlbnMoOS4wKTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9lM2NhMzYzMTg4MjM0ZGQzYTg1ODhlODc3MmYwYzkzNC5zZXRDb250ZW50KGh0bWxfN2ZlN2FjNzM5ZWVlNGJiMThkNTI5MWYyYTQ2NTEzZDQpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfMTIzMmVlYzg3ZTJjNDhiYTkyN2I1NDBkOGUzMmRiOGIuYmluZFBvcHVwKHBvcHVwX2UzY2EzNjMxODgyMzRkZDNhODU4OGU4NzcyZjBjOTM0KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyXzVlMTJiZWNmYzc2MDRjZmRiNDFhYTY4NzdmYmZhZDVlID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzE1MjI4OTIwNDYyODIsIC03NC4wMDU0MTUyOTg3MzM1NV0sCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcF9lMDg1MTQ0YjI5ZDM0ZTY5ODA1NTc1YmNlOGRmZDRlNyk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNjBkY2U2MDFhMTY0NGRiNzhhNDhiNDNhMmJjNTQzOTggPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzdkNGY2YTVlNWY1ZTRiYWQ5NWNjMDBlMTJkNjI0ZjBhID0gJChgPGRpdiBpZD0iaHRtbF83ZDRmNmE1ZTVmNWU0YmFkOTVjYzAwZTEyZDYyNGYwYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2l2aWMgQ2VudGVyLCBNYW5oYXR0YW4oOS4xKTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF82MGRjZTYwMWExNjQ0ZGI3OGE0OGI0M2EyYmM1NDM5OC5zZXRDb250ZW50KGh0bWxfN2Q0ZjZhNWU1ZjVlNGJhZDk1Y2MwMGUxMmQ2MjRmMGEpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfNWUxMmJlY2ZjNzYwNGNmZGI0MWFhNjg3N2ZiZmFkNWUuYmluZFBvcHVwKHBvcHVwXzYwZGNlNjAxYTE2NDRkYjc4YTQ4YjQzYTJiYzU0Mzk4KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyXzE5MTVjNzAxYzIyYTRiY2NhYzc2YWI2MTEyZjkwMWMzID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzIxNTIxOTY3NDQzMjE2LCAtNzQuMDEwNjgzMjg1NTkwODddLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZTA4NTE0NGIyOWQzNGU2OTgwNTU3NWJjZThkZmQ0ZTcpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2NhOTU5MWU0MTMwOTRhNDQ5NDFlMTA0NDVmOTNiZDU4ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF84MmFhZDVhNjY2NmU0NWE2ODU2YzkyYjkwMmZiMGI3YSA9ICQoYDxkaXYgaWQ9Imh0bWxfODJhYWQ1YTY2NjZlNDVhNjg1NmM5MmI5MDJmYjBiN2EiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRyaWJlY2EsIE1hbmhhdHRhbig5LjEpPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2NhOTU5MWU0MTMwOTRhNDQ5NDFlMTA0NDVmOTNiZDU4LnNldENvbnRlbnQoaHRtbF84MmFhZDVhNjY2NmU0NWE2ODU2YzkyYjkwMmZiMGI3YSk7CiAgICAgICAgCgogICAgICAgIG1hcmtlcl8xOTE1YzcwMWMyMmE0YmNjYWM3NmFiNjExMmY5MDFjMy5iaW5kUG9wdXAocG9wdXBfY2E5NTkxZTQxMzA5NGE0NDk0MWUxMDQ0NWY5M2JkNTgpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBmZWF0dXJlX2dyb3VwXzBmMWMzYzNlY2E4NzRhMDRhZWNlNWMwZGMzN2YwY2FjID0gTC5mZWF0dXJlR3JvdXAoCiAgICAgICAgICAgICAgICB7fQogICAgICAgICAgICApLmFkZFRvKG1hcF9lMDg1MTQ0YjI5ZDM0ZTY5ODA1NTc1YmNlOGRmZDRlNyk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTY4OGZlNGFhY2QyNDkwYWI3MmJlMzc3YTRlMjliNDEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43Njg1MDg1OTMzNTQ5MiwgLTczLjkxNTY1Mzc0MzA0MjM0XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJ5ZWxsb3ciLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYmx1ZSIsICJmaWxsT3BhY2l0eSI6IDAuNiwgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhmZWF0dXJlX2dyb3VwXzBmMWMzYzNlY2E4NzRhMDRhZWNlNWMwZGMzN2YwY2FjKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wNWM0YjViZGUyYjI0MTZiYTIzYjc1OTQzMzU1ZGM1ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczNzI1MDcxNjk0NDk3LCAtNzMuOTMyNDQyMzUyNjAxNzhdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInllbGxvdyIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJibHVlIiwgImZpbGxPcGFjaXR5IjogMC42LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAxMCwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKGZlYXR1cmVfZ3JvdXBfMGYxYzNjM2VjYTg3NGEwNGFlY2U1YzBkYzM3ZjBjYWMpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q4YjExMWY5MDc3NDQ3ZDg5MTQ4OGUyYzAzZDMzOTU0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzE1MjI4OTIwNDYyODIsIC03NC4wMDU0MTUyOTg3MzM1NV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAieWVsbG93IiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImJsdWUiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8oZmVhdHVyZV9ncm91cF8wZjFjM2MzZWNhODc0YTA0YWVjZTVjMGRjMzdmMGNhYyk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGIzNzAxN2E1ZDMwNDViN2FiYmEyZThkNDU4NDZmMGUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjE1MjE5Njc0NDMyMTYsIC03NC4wMTA2ODMyODU1OTA4N10sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAieWVsbG93IiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImJsdWUiLCAiZmlsbE9wYWNpdHkiOiAwLjYsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8oZmVhdHVyZV9ncm91cF8wZjFjM2MzZWNhODc0YTA0YWVjZTVjMGRjMzdmMGNhYyk7CiAgICAgICAgCjwvc2NyaXB0Pg==\" style=\"position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;\" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>"
      ],
      "text/plain": [
       "<folium.folium.Map at 0x57db610>"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# add pop-up text to each marker on the map\n",
    "for lat, lng, label in ny_neighborhood_stats[['Latitude','Longitude','Label']].values:\n",
    "    folium.Marker([lat, lng], popup=label).add_to(ny_map)        \n",
    "# add incidents to map\n",
    "ny_map.add_child(incidents)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that we have visualized the Neighborhoods.\n",
    "Lets Visualize Boroughs based on average Rating."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "ny_map = folium.Map(location=geo_location('New York'), zoom_start=12)\n",
    "ny_geo = r'Borough_Boundaries.geojson'\n",
    "\n",
    "map = ny_map.choropleth(\n",
    "    geo_data=ny_geo,\n",
    "    data=ny_borough_stats,\n",
    "    columns=['Borough', 'Average Rating'],\n",
    "    key_on='feature.properties.boro_name',\n",
    "    fill_color='YlOrRd', \n",
    "    fill_opacity=0.7, \n",
    "    line_opacity=0.2,\n",
    "    legend_name='Average Rating'\n",
    ")\n",
    "\n",
    "# display map\n",
    "# as this is huge map data , we will save it to a file\n",
    "ny_map.save('borough_rating.html')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Conclusion:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### So now we can answer the questions asked above in the Questions section of the notebook.\n",
    "### From our anaysis the answers to the above questions are:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### A1) Astoria(Queens), Blissville(Queens), Civic Center(Manhattan) are some of the best neighborhoods for Indian cuisine.\n",
    "#### A2) Manhattan have potential Indian Resturant Market.\n",
    "#### A3) Staten Island ranks last in average rating of Indian Resturants.\n",
    "#### A4) Manhattan is the best place to stay if you prefer Indian Cuisine."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
