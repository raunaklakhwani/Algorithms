from _collections import defaultdict
__author__ = "Ronak Lakhwani"
__copyright__ = "2015 Cisco Systems, Inc."

# General Imports
from datetime import datetime

# configuration
import configparser

# Imports for calling the CMX Rest API
from urllib.request import *
from urllib.error import URLError

# Imports for reading the xml response
from bs4 import BeautifulSoup

# Imports for reading the json response
import json

# Imports for plotting the graph
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import Layout, Marker, Scatter, XAxis, YAxis, Data, Figure, Stream

# Imports for certificate fail error
# The below two lines should be uncommented if you are getting [SSL: CERTIFICATE_VERIFY_FAILED] Error. This depends on the browser
# and on the environment depending on whether you have the certificate installed or not.
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Read config Starts
config = configparser.ConfigParser()
config.read("config.ini")
mse_ip = config.get('mse', 'mse_ip')
username = config.get('mse', 'username')
password = config.get('mse', 'password')
url_suffix = config.get('mse', 'url_suffix')
mac = config.get('local', 'mac')
response_format = config.get('local', 'response_format')
plotly_username = config.get('plotly', 'plotly_username')
plotly_api_key = config.get('plotly', 'plotly_api_key')
# Read config Ends

# Constant
url_prefix = "https://"

'''
Below method is used to return the response from the CMX API
whose end point is in the URL variable.
Username and Password are used to access the CMX API.
'''
def get_response(URL, username, password, response_format):
    '''
     Returns the response in the form of dict where keys are isError and others.
     if isError is True then dict contains the other keys such as data which contains the description of the message
     if isError is False then dict contains the other keys such as width,length,data.
    '''
    print (URL)
    response_dict = {}
    try :
        conn = HTTPPasswordMgrWithDefaultRealm()
        conn.add_password(None, URL, username, password)
        handler = HTTPBasicAuthHandler(conn)
        opener = build_opener(handler)
        opener.addheaders = [('Accept', 'application/' + response_format)]
        install_opener(opener)
        page = urlopen(URL).read()
        if len(page):
            page = page.decode('utf-8')
            if response_format == "xml" :
                data_dict = get_useful_data_from_XML(page)
            elif response_format == "json":
                data_dict = get_useful_data_from_json(page)
            data_dict['isError'] = False
            return data_dict
        else:
            response_dict['data'] = mac + " MAC NOT FOUND"
            response_dict['isError'] = True
            return response_dict
    except URLError as e:
        response_dict['data'] = "Either URL is malformed or " + mac + " address is not found in the CMX environment"
        response_dict['isError'] = True
        return response_dict

'''
Gets the date in the string format 2015-03-17T00:27:33.437+0000 and converts it into 2015-03-17 00:27:33 and then returns the date_object
'''
def parse_date(string_date):
    string_date = string_date[0:10] + " " + string_date[11:19]
    date_object = datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S")
    return date_object

'''
Extracts the useful data from the json response(in case response format in config is json) and returns the dict.
'''
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
        totalPages = json_dict['Locations']["totalPages"]
        width = json_dict['Locations']['entries'][0]['MapInfo']['Dimension']['width']
        length = json_dict['Locations']['entries'][0]['MapInfo']['Dimension']['length']

        for wirelessclientlocation in json_dict['Locations']['entries']:
            x = wirelessclientlocation["MapCoordinate"]["x"]
            y = wirelessclientlocation["MapCoordinate"]["y"]
            lastlocatedtime = parse_date(wirelessclientlocation["Statistics"]["lastLocatedTime"])
            data.append((lastlocatedtime, x, y))
        return {"width" : width, "length":length, "data":data,"totalPages":totalPages}
    else :
        return {}

'''
Extracts the useful data from the json response(in case response format in config is xml) and returns the dict.
'''
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

'''
Method which reads the dict and renders the response on to the Plotly framework.
'''
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
        text=list(range(1, len(pData) + 1)),
        name=mac,
        marker=Marker(color="red"),
        opacity="0.5",
        legendgroup = mac,
    )
    
    startAndEndData = Scatter(
        x=[pData[0][1], pData[-1][1]],
        y=[pData[0][2], pData[-1][2]],
        mode='markers',
        marker=Marker(color="red", size="6"),
        showlegend=False,
        name = mac,
        text=["Start point", "End point"],
        legendgroup = mac,
    )

    py.sign_in(plotly_username, plotly_api_key)
    tls.set_credentials_file(username=plotly_username,
                                 api_key=plotly_api_key)
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
    data = Data([processed_data,startAndEndData])
    fig = Figure(data=data, layout=layout)
    py.plot(fig, filename='Sample Code For History Of Clients ')
    


start = 0
interval = 50
totalpages = None
c = 0
response_format = "json"
mainDict = defaultdict(list)
while True:
    print("Called",totalpages,start)
    if totalpages is not None and start > totalpages:
        break
    else:
        URL = url_prefix + mse_ip + url_suffix + mac + "?/page=" + str(start) + "&pageSize=" + str(interval)
        c += 1
        start = c * interval + 1
    
    conn = HTTPPasswordMgrWithDefaultRealm()
    conn.add_password(None, URL, username, password)
    handler = HTTPBasicAuthHandler(conn)
    opener = build_opener(handler)
    opener.addheaders = [('Accept', 'application/' + response_format)]
    install_opener(opener)
    page = urlopen(URL).read()
    page = page.decode('utf-8')
    data_dict = get_useful_data_from_json(page)
    mainDict["data"].extend(data_dict["data"])
    if totalpages is None:
        totalpages = data_dict.get("totalPages")
        py.sign_in(plotly_username, plotly_api_key)
        tls.set_credentials_file(username=plotly_username,
                                     api_key=plotly_api_key)
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
        
        tls.set_credentials_file(stream_ids=[
            "kk9r8fbr07",
            "5iv4ntu3x1"
        ])
        stream_ids = tls.get_credentials_file()['stream_ids']
        stream_id = stream_ids[0]
        stream = Stream(
            token=stream_id  # (!) link stream id to 'token' key
        )
        
        processed_data = Scatter(
        x=[],
        y=[],
        mode='lines + text',
        text=[],
        name=mac,
        marker=Marker(color="red"),
        opacity="0.5",
        legendgroup = mac,
        stream = stream
        )
        
        data = Data([processed_data])
        fig = Figure(data=data, layout=layout)
        plot_url = py.plot(fig, filename='Demo')
        writeStream = py.Stream(stream_id)
        writeStream.open()
    
    
    x = [x[1] for x in mainDict["data"]]
    y = [y[2] for y in mainDict["data"]]
    
    scatter = Scatter(x = x,y = y)
    writeStream.write(scatter)
        
        
    
    
    
        
    
    
