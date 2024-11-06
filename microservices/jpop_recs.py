# this will give a user a jpop recommendation based on their kpop likes
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_data():
    with open('data/artist_info.json') as f:
        return json.load(f)
    
# endpoint to recommend jpop artists
@app.route('/recommend_jpop', methods=['GET'])
def recommend_jpop():
    # get names of kpop artist from the request
    kpop_artist = request.args.get('kpop_artist')
    data = load_data()

    # find kpop artist in the json and get their attributes
    for artist in data['artists']:
        if artist['pop'] == 'kpop' and artist['name'].lower() == kpop_artist.lower():
            # find jpop artist with at least one matching attribute
            matching_jpop = [
                jpop for jpop in data['artists']
                if jpop['pop'] == 'kpop' and set(artist['attributes']).intersection(jpop['attributes'])
            ]
            if matching_jpop:
                return jsonify(matching_jpop)
            else:
                {"message": "No matching J-pop artist found."}

    # if j-pop artist not found
    return jsonify({"message": "K-pop artist not found."})

if __name__ == '__main__':
    app.run(port=5001)
