import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
py.sign_in('ronaklakhwani', 'c6hv1155p9')
tls.set_credentials_file(username="ronaklakhwani", api_key="c6hv1155p9")

tokens = ["8nkkf6evch"]

trace1 = Scatter(
        x=[],
        y=[],
        stream=dict(token="8nkkf6evch")
    )

trace2 = Scatter(
        x=[],
        y=[],
        stream=dict(token="j7zoksx3c0")
    )

data = Data([trace1,trace2])
py.plot(data)
s = py.Stream("8nkkf6evch")
s.open()
s.write(dict(x=1, y=2))



s1 = py.Stream("j7zoksx3c0")
s1.open()
s1.write(dict(x=2, y=1))
s1.close()

s.close()
