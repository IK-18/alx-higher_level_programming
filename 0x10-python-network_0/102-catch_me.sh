#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
curl -s --location-trusted -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
