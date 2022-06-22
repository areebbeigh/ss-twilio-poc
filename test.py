from flask import Flask, jsonify, request

from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant

account_sid = "ACb1f23dfae89bcf58784ed42fd9dacd14"

api_secret = "gxgtY4sjAW9M2QUIaSJpiYX7zrsLRoqv"
api_sid = "SKd17d65c3e7f34da8dd11abe1c08fc980"


app = Flask(__name__)


@app.route('esign/u/twilio/createRoom/test/<string:identity>/', methods=['POST'])
def home(identity):
    token = AccessToken(account_sid, api_sid,
                        api_secret, identity=identity)
    chat_grant = VideoGrant(room="*")
    token.add_grant(chat_grant)
    return token.to_jwt()


if __name__ == '__main__':
    app.run(debug=True, port=9090)
