import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
py.sign_in('raunaklakhwani', 'n7qx3a5vcn')
tls.set_credentials_file(username="raunaklakhwani", api_key="n7qx3a5vcn")

tokens = ["5iv4ntu3x1","n5zislq74h","vii6b36zch","j5fmnabw7y","tofp3ckjh2","bgkhw0u0uf","txik5etrd5","vdp3m8uagb","kk9r8fbr07","j0c1f31t87","9tja95kvy9","dnseotxru0","pdgfij8xcf"]
for temp in tokens:
    try:
        print(temp)
        trace1 = Scatter(
                x=[],
                y=[],
                stream=dict(token=temp)
            )
        
        data = Data([trace1])
        py.plot(data)
        s = py.Stream(temp)
        s.open()
        s.write(dict(x=1, y=2))
        s.close()
    except :
        pass