#!/usr/bin/env python3

import os
import flask_s3

from web_app import app

FLASKS3_FORCE_MIMETYPE = True

print(app.config['FLASKS3_REGION'])

flask_s3.create_all(
    app,
    user=os.getenv('AWS_ACCESS_KEY_ID'),
    password=os.getenv('AWS_SECRET_ACCESS_KEY'),
    location=app.config['FLASKS3_REGION']
)
print("Uploaded.")