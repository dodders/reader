#/bin/sh

aws lambda update-function-code --function-name blog-reader --zip-file fileb://function.zip --profile iam-admin
