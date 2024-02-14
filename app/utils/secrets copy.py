import os

def getSecrets():
    secrets = {
        'MONGO_HOST':"mongodb+srv://jfohler33:jfohler33@fohler33.wfo86iu.mongodb.net/JacobPractice?retryWrites=true&w=majority",
        'MONGO_DB_NAME':"JacobPractice",
        'GOOGLE_CLIENT_ID': "296103977700-j0pimk9ih2fjj8gl753ttu4chqp9r3co.apps.googleusercontent.com",
        'GOOGLE_CLIENT_SECRET':"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",
        'GOOGLE_DISCOVERY_URL':"https://accounts.google.com/.well-known/openid-configuration",
        'MY_EMAIL_ADDRESS':"s_jacob.fohler@ousd.org"
        }
    return secrets