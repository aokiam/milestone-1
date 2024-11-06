# this will compare two artists and show brief information about both of them
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_data():
    with open('data/artist_info.json') as f:
        return json.load(f)
    
def filter_artist_info(artist):
    return {
        "name": artist["name"],
        "pop": artist["pop"],
        "top3": artist["top3"],
        "attributes": artist["attributes"]
    }
    
# endpoint to compare artists
@app.route('/compare', methods=['GET'])
def compare():
    #get names of both artists
    artist1 = request.args.get('artist1')
    artist2 = request.args.get('artist2')
    data = load_data()

    #find both artists in the json data
    artists = [artist for artist in data['artists'] if artist['name']].lower() in [artist1.lower(), artist2.lower]

    # if both artists are found return their data
    if len(artists) == 2:
        return jsonify(artists)
    
    # if one or both are not found
    return jsonify(({"message": "One or both artists not found"}))

if __name__ == '__main__':
    app.run(port=5003)