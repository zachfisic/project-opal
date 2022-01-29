import pandas as pd
from flask import render_template
from flaskapp.components.auth.func import authorize
from flaskapp.components.user.graphs import graphs
from flaskapp.components.user.graphs.func import create_top_artists_dataframe, create_related_artists_dataframe

@graphs.route('/favorite_artists')
@authorize
def favorite_artists(spotify):

    # Gather top artists
    artists = create_top_artists_dataframe(spotify, time_range="all", limit=2)
    network_lists, edges = [artists], []

    for i in range(len(artists)):
        temp = []
        favorite_artist_id = artists.iloc[i]['id']
        related_artists = create_related_artists_dataframe(spotify, favorite_artist_id)

        for j in range(len(related_artists)):
            if related_artists.iloc[j]['name'].isnumeric():
                continue
            else:
                # only create an edge between artists with names and not numeric identifiers
                temp.append((artists.iloc[i]['name'], related_artists.iloc[j]['name']))

        network_lists.append(related_artists)
        edges.append(temp)

    # Remove duplicates and concatenate the top artists dataframe with the related artists
    network = pd.concat(network_lists).drop_duplicates(subset=['id']).reset_index(drop=True)

    # Remove any duplicated artists by name and reset the dataframe's index
    network = network.sort_values(by=['name'])
    network = network[network.name.isin([name for name in network.name if not name.isnumeric()])]
    network = network.drop_duplicates(subset=['name'])
    network.reset_index(drop=True, inplace=True)

    # Get the smallest profile image url for each artist
    images = []
    for i in range(len(network)):
        try:
            images.append(network.iloc[i]['images'][2]['url'])
        except:
            images.append(None)

    # Create graph
    graph_edges = sum(edges, [])
    graph = nx.Graph()
    graph.add_edges_from(graph_edges)
    size = [i[1] for i in sorted(dict(graph.degree).items())]
    g = Network(height="100%", width="100%", notebook=False)
    g.inherit_edge_colors(True)
    nodes = [i[0] for i in sorted(dict(graph.degree).items())] 
    g.barnes_hut()

    for idx,i in enumerate(nodes):
        g.add_node(i, value=size[idx], label=' ', title=i, shape='circularImage', image=images[idx])
        
    g.add_edges(graph.edges)
    #g.show_buttons(filter_=True)

    g.set_options('''
    var options = {
        "nodes": {
            "shape": "diamond",
            
            "size": 100
        },
        "color": {
            "highlight": {
                "border": "rgba(48,103,84,1)",
                "background": "rgba(188,233,84,1)"
            }
        },
        "edges": {
            "color": {
                "highlight": "rgba(65,163,23,1)",
                "inherit": true,
                "opacity": 0.25
            },
            "shadow": {
                "enabled": true
            },
            "smooth": {
                "type": "continuous",
                "forceDirection": "none"
            }
        },
        "physics": {
            "forceAtlas2Based": {
                "springLength": 100
            },
            "minVelocity": 0.75,
            "solver": "forceAtlas2Based"
        }
    }
    ''')
    g.write_html('flaskapp/templates/network.html')
    return render_template('network.html')
    
    