from flask import render_template
from flaskapp.views.main.graphs import graphs
import matplotlib
matplotlib.use('Agg') # Avoids "UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail."
import matplotlib.pyplot as plt
import io
import base64



@graphs.route('/test_plot')
def build_plot():
    
    img = io.BytesIO()
    y = [1,2,3,4,5]
    x = [0,2,1,3,4]
    plt.plot(x,y)
    plt.savefig(img, format='png')
    
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()
    src = f"data:image/png;base64,{plot_url}"
    return render_template('test.html', src=src)