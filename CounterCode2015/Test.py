__author__ = "Ronak Lakhwani"
__copyright__ = "2015 Cisco Systems, Inc."

__about__ = '''
This sample code is meant to track the history of single mac address using CMX.
To run this code you need to make certain environment changes. The configuration changes are listed below in the configuration
section such as mse_ip, macs, username, password.
mse_ip is the IP of the MSE() in the CMX
mac is the mac addresses which is to be tracked
username/password are the credentials to access the apis of the CMX
you don't need to change url_prefix and url_suffix but still just verify them according to your environment.
If you have any issues in running this code
you can issue a bug in the github repository giving all the details of your environment
'''

# General Imports 
from datetime import datetime

# Imports for calling the CMX Rest API 
import urllib2
from urllib2 import URLError

# Imports for reading the xml response
from bs4 import BeautifulSoup

# Imports for reading the json response
import json


# Imports for plotting the graph
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import Layout, Marker, Scatter, XAxis, YAxis, Data, Figure

# Imports for certificate fail error
# The below two lines should be uncommented if you are getting [SSL: CERTIFICATE_VERIFY_FAILED] Error. This depends on the browser
# and on the environment depending on whether you have the certificate installed or not.
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



# CONFIGURATION STARTS
# Change it according to your local environment.
version = "MSE8.0"
url_prefix = "https://"
mse_ip = "128.107.125.15"
url_suffix = "/api/contextaware/v1/location/history/clients/"
mac = "3c:a9:f4:33:66:40"
username = "learning"
password = "learning"
response_format = "xml"  # Could be xml or json
# CONFIGURATION ENDS


def get_response(URL, username, password, response_format):
    '''
     Returns the response in the form of dict where keys are isError and others.
     if isError is True then dict contains the other keys such as data which contains the description of the message
     if isError is False then dict contains the other keys such as width,length,data.
    '''
    response_dict = {}
    try :
        p = urllib2.HTTPPasswordMgrWithDefaultRealm()
        p.add_password(None, URL, username, password)
        handler = urllib2.HTTPBasicAuthHandler(p)
        opener = urllib2.build_opener(handler)
        opener.addheaders = [('Accept', 'application/' + response_format)]
        urllib2.install_opener(opener)
        page = urllib2.urlopen(URL).read()
        
        if response_format == "xml" :
            data_dict = get_useful_data_from_XML(page)
        elif response_format == "json":
            data_dict = get_useful_data_from_json(page)
        data_dict['isError'] = False
        return data_dict
    except URLError, e:
        response_dict['data'] = e
        response_dict['isError'] = True
        return response_dict
    
    

def parse_date(string_date):
    '''
    Gets the date in the string format 2015-03-17T00:27:33.437+0000 and converts it into 2015-03-17 00:27:33 and then returns the date_object
    '''
    string_date = string_date[0:10] + " " + string_date[11:19]
    date_object = datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S")
    return date_object

def get_useful_data_from_json(json_response):
    '''
    Parses the json_response and returns the dict with keys as width, length and the data 
    1. width contains the value of the width
    2. length contains the value of the length
    3. data contains the list of tuples where tuples are in the format (lastlocatedtime,x,y)
    All the above three are returned only when you get location from the json_response otherwise an empty dict is returned
    
    '''
    data = []
    json_dict = json.loads(json_response)
    if len(json_dict['Locations']['entries']) > 0:
        width = json_dict['Locations']['entries'][0]['MapInfo']['Dimension']['width']
        length = json_dict['Locations']['entries'][0]['MapInfo']['Dimension']['length']
        
        for wirelessclientlocation in json_dict['Locations']['entries']:
            x = wirelessclientlocation["MapCoordinate"]["x"]
            y = wirelessclientlocation["MapCoordinate"]["y"]
            lastlocatedtime = parse_date(wirelessclientlocation["Statistics"]["lastLocatedTime"])
            data.append((lastlocatedtime, x, y))
        return {"width" : width, "length":length, "data":data}
    else :
        return {}

def get_useful_data_from_XML(xml):
    '''
    Parses the xml and returns the dict with keys as width, length and the data 
    1. width contains the value of the width
    2. length contains the value of the length
    3. data contains the list of tuples where tuples are in the format (lastlocatedtime,x,y)
    All the above three are returned only when you get location from the jsonResponse otherwise an empty dict is returned
    
    '''
    data = []
    xml_format = BeautifulSoup(xml)
    wirelessclientlocations = xml_format.find_all("wirelessclientlocation")
    if len(wirelessclientlocations) > 0:
        width = xml_format.locations.wirelessclientlocation.mapinfo.dimension['width']
        length = xml_format.locations.wirelessclientlocation.mapinfo.dimension['length']
        for wirelessclientlocation in wirelessclientlocations:
            x = wirelessclientlocation.mapcoordinate['x']
            y = wirelessclientlocation.mapcoordinate['y']
            lastlocatedtime = parse_date(wirelessclientlocation.statistics['lastlocatedtime'])
            data.append((lastlocatedtime, x, y))
        return {"width" : width, "length":length, "data":data}
    else:
        return {}



def plotData(data_dict):
    '''
    Plots the data on the Plotly Framework.
    '''
    pData = data_dict['data']
    pData = sorted(pData, key=lambda x:x[0])
    
    
    processed_data = Scatter(
        x=[x[1] for x in pData],
        y=[y[2] for y in pData],
        mode='lines + text',
        text=range(1, len(pData) + 1),
        name=mac,
        marker=Marker(color="red")
    )
    
    
    # The below two lines are using the plotly interface account details.
    # username is raunaklakhwani and the 'n7qx3a5vcn' is the api key to use the plotly.
    # User can create their new account on plotly and get the new api key and change the username and apikey over here.
    # Can also use already created username and key
    py.sign_in('raunaklakhwani', 'n7qx3a5vcn')
    tls.set_credentials_file(username="raunaklakhwani",
                                 api_key="n7qx3a5vcn")
    
    layout = Layout(
                showlegend=True,
                autosize=True,
                height=800,
                width=800,
                title="MAP",
                xaxis=XAxis(
                    zerolinewidth=4,
                    gridwidth=1,
                    showgrid=True,
                    zerolinecolor="#969696",
                    gridcolor="#bdbdbd",
                    linecolor="#636363",
                    mirror=True,
                    zeroline=False,
                    showline=True,
                    linewidth=6,
                    type="linear",
                    range=[0, data_dict["length"]],
                    autorange=False,
                    autotick=False,
                    dtick=15,
                    tickangle=-45,
                    title="X co-ordinate"
                    ),
                yaxis=YAxis(
                    zerolinewidth=4,
                    gridwidth=1,
                    showgrid=True,
                    zerolinecolor="#969696",
                    gridcolor="#bdbdbd",
                    linecolor="#636363",
                    mirror=True,
                    zeroline=False,
                    showline=True,
                    linewidth=6,
                    type="linear",
                    range=[data_dict["width"], 0],
                    autorange=False,
                    autotick=False,
                    dtick=15,
                    tickangle=-45,
                    title="Y co-ordinate"    
                    )
                )
    data = Data([processed_data])
    fig = Figure(data=data, layout=layout)
    py.plot(fig, filename='Sample Code For History Of Clients ')
    
    
    

if __name__ == '__main__':
    URL = url_prefix + mse_ip + url_suffix + mac
    data_dict = get_response(URL, username, password, response_format)
    if data_dict['isError'] == False:
        if len(data_dict['data']) > 0:
            plotData(data_dict)
        else:
            print 'No clients found'
    else:
        print "Error = ", data_dict['data']