from flask import Flask, render_template
import pandas as pd
import azure.cosmos.cosmos_client as cosmos_client

app = Flask(__name__)

# Initialize Cosmos DB Client
client = cosmos_client.CosmosClient("YourCosmosDBEndpoint", {"masterKey": "YourPrimaryKey"})

@app.route('/')
def dashboard():
    query = "SELECT * FROM c"
    items = list(client.QueryItems("YourDatabaseId", {"query": query}, enable_cross_partition_query=True))
    data = pd.DataFrame(items)
    return render_template('dashboard.html', data=data.to_html())

if __name__ == '__main__':
    app.run(debug=True)

