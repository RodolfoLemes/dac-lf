#!/bin/bash
APP_DIR="app"

ZIP_FILE="lambda_package.zip"

IAC_DIR="iac"

source .venv/bin/activate

pip install -r requirements.txt

mkdir -p dist

cp -r app/* dist/

cp -r .venv/lib/python3.8/site-packages/* dist/

cd dist

zip -r ../$ZIP_FILE . || { echo "Failed to create zip file"; exit 1; }

cd ..

FILENAME=$(basename $ZIP_FILE)

echo "Deploying $FILENAME"

cd $IAC_DIR || { echo "Directory $IAC_DIR not found"; exit 1; }

terraform init

terraform apply -auto-approve -var="lambda_filename=../$FILENAME" 
